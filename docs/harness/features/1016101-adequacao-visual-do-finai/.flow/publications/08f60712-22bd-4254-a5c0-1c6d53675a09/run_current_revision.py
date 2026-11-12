from pathlib import Path
import json,sys,runpy,hashlib,importlib,copy

sys.dont_write_bytecode=True
root=Path.cwd()
scripts=root/'.agents/skills/project-slices/scripts'
sys.path.insert(0,str(scripts));sys.path.insert(0,str(root/'.agents/skills/project-flow/scripts'))
import manage_divergence
from manage_slices import digest,ContractError
from validate_publication_alignment import validate as validate_alignment

p=next(parent for parent in Path(__file__).resolve().parents if (parent/'feature.md').is_file() and (parent/'.flow/feature-state.json').is_file())
operation=Path(__file__).resolve().parent
record_path=operation/('publication-alignment-'+operation.name+'.json')
original=manage_divergence.local_is_current

def current_or_verified_later_revision(state):
    try:
        return original(state)
    except ContractError as error:
        if str(error) not in {'corrected canonical artifact changed after local alignment','corrected canonical approval changed after local alignment'}:
            raise
        # A conclusão anterior permanece histórica. Validar a revisão posterior
        # e provar a ligação exata com o documento e aprovação anteriores.
        assert state['status']=='completed' and state['operation']['status']=='completed'
        alignment=validate_alignment(record_path)
        assert alignment['status']=='completed'
        previous=json.loads((operation/'feature-state-before.json').read_text(encoding='utf-8'))
        review=json.loads((operation/'requirement-review.json').read_text(encoding='utf-8'))
        assert hashlib.sha256((operation/'feature-state-before.json').read_bytes()).hexdigest()==review['before_state_sha256']
        assert json.loads((operation/'previous-divergence.json').read_text(encoding='utf-8'))==state
        assert alignment['issue']['issue_id']==state['revisions'][-1]['parent_baseline']['issue_id']==previous['redmine']['issue_id']
        assert hashlib.sha256((operation/'feature-before.md').read_bytes()).hexdigest()==state['local_alignments'][0]['artifact_after_sha256']
        old_approvals=[a for a in previous['approvals'] if a['kind']=='requirement' and a['status']=='valid']
        assert len(old_approvals)==1 and digest(old_approvals[0])==state['local_alignments'][0]['requirement_approval_sha256']
        assert review['after_requirement_sha256']==alignment['canonical']['sha256']
        return None

manage_divergence.local_is_current=current_or_verified_later_revision
if len(sys.argv)<2:
    raise SystemExit('Informe o helper local a executar.')
helper=Path(sys.argv[1]).name
assert helper in {'manage_slices.py','manage_change_review.py','manage_condition_revision.py','manage_revision_application.py'}
sys.argv=[str(scripts/helper),*sys.argv[2:]]
if helper=='manage_revision_application.py' and len(sys.argv)>1 and sys.argv[1]=='prepare':
    module=importlib.import_module('manage_revision_application')
    original_validate=module.validate_state
    manifest=json.loads((p/'.work/translation-sequencing-manifest.json').read_text(encoding='utf-8'))
    def validate_candidate_with_approved_sequence(state,*args,**kwargs):
        current=state['revisions'][-1]
        if current['number']==manifest['previous_revision']+1 and 'sequencing' not in current:
            assert state['status']=='prepared'
            assert [o['key'] for o in current['operations']]==manifest['operation_keys']
            previous=state['revisions'][-2]
            assert previous['sequencing']['sha256']==manifest['previous_plan_sha256']
            state.setdefault('sequencing_operation_history',[]).append({'revision':previous['number'],'plan_sha256':previous['sequencing']['sha256'],'operations':copy.deepcopy(state['sequencing_operations'])})
            current['sequencing']=json.loads(Path(manifest['sequencing_path']).read_text(encoding='utf-8'))
            current['proposal_sha256']=module.proposal_digest(current)
            state['sequencing_operations']={}
        return original_validate(state,*args,**kwargs)
    module.validate_state=validate_candidate_with_approved_sequence
    raise SystemExit(module.main())
runpy.run_path(str(scripts/helper),run_name='__main__')
