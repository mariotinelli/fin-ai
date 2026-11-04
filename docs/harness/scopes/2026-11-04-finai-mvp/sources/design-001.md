# Source: FinAI-Controle-Financeiro.zip

- Source ID: `design-001`
- Type: referência visual
- Origin: C:/Users/maari/Downloads/FinAI-Controle-Financeiro.zip
- Original SHA-256: `d7fec0da8d116208b921ee8cb152b8c3710cf4a7500e30aca6d7b43270dddbd5`
- Extraction: Leitura integral dos três arquivos UTF-8 com zipfile, sem execução ou extração dos originais

## Extracted content

Referência exclusivamente visual, conforme defini??o posterior do usuário. Os comportamentos execut?veis não são requisitos funcionais aprovados. Tr?s ?reas visuais: Visão geral, Transa??es e Assistente. Formul?rios e di?logos de detalhe, edição, exclusão e proposta no chat; estados vazios, erro e processamento.

### Arquivo: index.html

````
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#145C46"><title>FinAI — Suas finanças, com clareza</title>
<style>
/* OD-LAYOUT-PRIMITIVES v1 — structure only: display, flex/grid, overflow, wrapping, ratio. */
@layer od-layout {
  :where(.od-stack,.od-row,.od-row-top,.od-cluster,.od-grid,.od-field,.od-stat,.od-cell,.od-tile) > :where(*) { min-width: 0; }
  .od-stack { display:flex; flex-direction:column; gap:var(--od-gap,8px); }
  .od-row { display:flex; align-items:center; gap:var(--od-gap,8px); }
  .od-row-top { display:flex; align-items:flex-start; gap:var(--od-gap,8px); }
  .od-cluster { display:flex; flex-wrap:wrap; align-items:center; gap:var(--od-gap,8px); }
  .od-fill { flex:1 1 0; min-width:0; } .od-fixed { flex:none; }
  .od-grid { display:grid; gap:var(--od-gap,12px); grid-template-columns:repeat(var(--od-cols,3),minmax(0,1fr)); }
  .od-stat,.od-field,.od-cell { display:grid; gap:var(--od-gap,2px); }
  :where(.od-stat,.od-field,.od-cell)>:where(*) { display:block; }
  .od-tile { display:grid; grid-template-rows:auto 1fr; } .od-tile>:where(*) {display:block;}
  .od-media { display:block; width:100%; height:auto; aspect-ratio:var(--od-ratio,auto); }
  .od-media-cover {object-fit:cover;}
  .od-truncate {display:block;max-width:100%;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}
  .od-clamp-2,.od-clamp-3 {display:-webkit-box;-webkit-box-orient:vertical;overflow:hidden;overflow-wrap:anywhere;}
  .od-clamp-2 {-webkit-line-clamp:2;} .od-clamp-3 {-webkit-line-clamp:3;}
  .od-lines-2 {min-height:calc(2 * 1.4em);} .od-nowrap {white-space:nowrap;}
  .od-keep {word-break:keep-all;overflow-wrap:anywhere;}
  .od-screen {display:grid;grid-template-rows:auto minmax(0,1fr) auto;height:100%;}
  .od-scroll {overflow-y:auto;overscroll-behavior:contain;min-height:0;}
  .od-rail {display:flex;gap:var(--od-gap,8px);overflow-x:auto;scroll-snap-type:x proximity;scrollbar-width:none;padding-inline:var(--od-rail-pad,16px);scroll-padding-inline:var(--od-rail-pad,16px);}
  .od-rail::-webkit-scrollbar {display:none;} .od-rail>:where(*) {flex:none;scroll-snap-align:start;}
  .od-rail>:where(:last-child) {margin-inline-end:var(--od-rail-pad,16px);}
  .od-spacer {flex:none;visibility:hidden;pointer-events:none;} .od-touch {min-width:44px;min-height:44px;}
}
/* /OD-LAYOUT-PRIMITIVES v1 */
:root{--bg:#F5F7F8;--surface:#fff;--ink:#172622;--muted:#52615C;--green:#145C46;--positive:#146345;--negative:#A12B36;--line:#D6DFDB;--tint:#E4F0E9;--focus:#1D5DB0;--s1:4px;--s2:8px;--s3:16px;--s4:24px;--s5:32px;--s6:48px;--s7:64px;--radius:8px;--panel:16px;--body:16px;--small:14px;--h3:20px;--h2:24px;--h1:40px;--enter:200ms;--exit:150ms;--shadow:0 16px 48px #17262220;--icon:20px;--sidebar:240px}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:var(--body)/1.5 system-ui,sans-serif}button,input,select,textarea{font:inherit}button,a,input,select,textarea{-webkit-tap-highlight-color:transparent}button,a{touch-action:manipulation}button{cursor:pointer}button:disabled{cursor:not-allowed;opacity:.55}button,input,select,textarea{border-radius:var(--radius)}button{border:0}a{color:var(--green)}:focus-visible{outline:3px solid var(--focus);outline-offset:4px}h1,h2,h3,p{margin:0}h1{font:400 clamp(32px,3vw,40px)/1.2 Georgia,serif;letter-spacing:-1px}h2{font-size:var(--h3);font-weight:600}h3{font-size:var(--body)}svg{display:block;width:var(--icon);height:var(--icon);flex:none;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}.hidden,[hidden]{display:none!important}.muted{color:var(--muted)}.small{font-size:var(--small)}.positive{color:var(--positive)}.negative{color:var(--negative)}.eyebrow{text-transform:uppercase;letter-spacing:2px;font-size:12px;font-weight:700}.number{font-variant-numeric:tabular-nums}.btn{min-height:44px;padding:var(--s2) var(--s3);display:inline-flex;align-items:center;justify-content:center;gap:var(--s2);font-weight:600;white-space:nowrap;background:var(--green);color:white;transition:opacity var(--enter) ease-out}.btn.secondary{background:white;color:var(--ink);border:1px solid var(--line)}.btn.ghost{color:var(--green);background:transparent}.btn.danger{background:var(--negative)}.icon-btn{display:inline-flex;align-items:center;justify-content:center;min-width:44px;min-height:44px;background:transparent;color:var(--muted)}.text-btn{color:var(--green);background:none;padding:var(--s2) 0;min-height:44px;font-weight:600;display:inline-flex;gap:var(--s2);align-items:center}.badge{display:inline-flex;align-items:center;gap:var(--s2);border:1px solid var(--line);border-radius:var(--radius);padding:var(--s1) var(--s2);font-size:12px;font-weight:600;white-space:nowrap}.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:block}.app{display:grid;grid-template-columns:var(--sidebar) minmax(0,1fr);min-height:100vh}.sidebar{padding:var(--s5) var(--s4);background:white;border-right:1px solid var(--line);display:flex;flex-direction:column;position:sticky;top:0;height:100vh;gap:var(--s6)}.brand{display:flex;align-items:center;gap:var(--s2);text-decoration:none;color:var(--ink);font-size:28px;font-weight:700;letter-spacing:-1px}.brand-mark{display:flex;align-items:center;justify-content:center;width:40px;height:40px;background:var(--green);color:white;border-radius:12px}.brand-mark svg{width:24px;height:24px}.brand-ai{font-weight:400;color:var(--green)}nav{display:flex;flex-direction:column;gap:var(--s2)}.nav-link{display:flex;align-items:center;gap:var(--s3);min-height:48px;padding:var(--s2) var(--s3);border-radius:var(--radius);text-decoration:none;color:var(--muted);font-weight:500}.nav-link.active{background:var(--tint);color:var(--green);font-weight:650}.nav-caption{margin:0 var(--s3) var(--s3);font-size:11px;color:var(--muted);letter-spacing:2px;font-weight:600}.sidebar-bottom{margin-top:auto}.local-note{padding:var(--s3);border:1px solid var(--line);border-radius:var(--radius);font-size:var(--small);color:var(--muted)}.local-note strong{display:block;color:var(--ink);margin-bottom:var(--s2);font-weight:600}.profile{margin-top:var(--s4);padding-top:var(--s4);border-top:1px solid var(--line);--od-gap:12px}.avatar{display:flex;align-items:center;justify-content:center;background:var(--bg);border:1px solid var(--line);width:40px;height:40px;border-radius:50%;color:var(--green);font-size:var(--small);font-weight:650}.workspace{min-width:0}.topbar{min-height:80px;border-bottom:1px solid var(--line);background:var(--surface);padding:var(--s3) var(--s5);display:flex;align-items:center;justify-content:space-between;gap:var(--s3)}.breadcrumb{display:flex;align-items:center;gap:var(--s3);font-size:var(--small)}.breadcrumb span:first-child{color:var(--muted)}.top-right{display:flex;align-items:center;gap:var(--s3)}main{max-width:1440px;margin:auto;padding:var(--s5);min-width:0}.page-head{display:flex;align-items:center;justify-content:space-between;gap:var(--s4);margin-bottom:var(--s5)}.page-head p{color:var(--muted);margin-top:var(--s2)}.actions{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s3)}.month-control{display:flex;align-items:center;gap:var(--s2);padding:0 var(--s3);min-height:44px;background:white;border:1px solid var(--line);border-radius:var(--radius)}.month-control input{border:0;background:none;padding:var(--s2) 0;color:var(--ink);min-width:0;width:150px}.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s4);margin-bottom:var(--s4)}.stat-card{border:1px solid var(--line);border-radius:var(--panel);padding:var(--s4);background:white;min-width:0}.stat-card.balance{background:var(--green);color:white;border-color:var(--green)}.stat-label{display:flex;justify-content:space-between;align-items:center;gap:var(--s2);font-size:var(--small);font-weight:500}.stat-symbol{display:flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:var(--radius);background:var(--tint);color:var(--green)}.balance .stat-symbol{background:#ffffff18;color:white}.stat-value{font-size:clamp(20px,2.2vw,32px);font-weight:600;letter-spacing:-1px;line-height:1.4;margin:var(--s3) 0 var(--s2);overflow-wrap:anywhere}.stat-foot{font-size:12px;color:var(--muted)}.balance .stat-foot{color:#D6E9DF}.overview-grid{display:grid;grid-template-columns:minmax(0,1.65fr) minmax(280px,1fr);gap:var(--s4);margin-bottom:var(--s4)}.panel{border:1px solid var(--line);background:white;border-radius:var(--panel);padding:var(--s4);min-width:0}.panel-head{display:flex;align-items:center;justify-content:space-between;gap:var(--s3);margin-bottom:var(--s4)}.panel-head p{font-size:var(--small);color:var(--muted);margin-top:var(--s1)}.legend{display:flex;gap:var(--s3);font-size:12px;flex-wrap:wrap}.legend span{display:flex;align-items:center;gap:var(--s2)}.legend i{display:block;width:8px;height:8px;border-radius:2px;background:var(--green)}.legend .out i{background:#A12B36}.graph{min-height:184px;display:flex;flex-direction:column;justify-content:center}.chart-empty{padding:var(--s4) 0;text-align:center;background:repeating-linear-gradient(to bottom,transparent,transparent 47px,#E9EEEB 47px,#E9EEEB 48px);display:grid;justify-items:center;gap:var(--s2)}.chart-empty svg{width:32px;height:32px;color:var(--green)}.chart-empty p{font-size:var(--small);max-width:320px;background:white;padding:0 var(--s2);color:var(--muted)}.bar-row{display:grid;grid-template-columns:80px minmax(0,1fr);gap:var(--s3);align-items:center;margin-bottom:var(--s4);font-size:var(--small)}.bar-track{background:var(--bg);height:12px;border-radius:4px;margin-top:var(--s2)}.bar{height:100%;background:var(--green);border-radius:4px}.bar.expense{background:var(--negative)}.graph-foot{display:flex;justify-content:space-between;gap:var(--s3);border-top:1px solid var(--line);padding-top:var(--s3);margin-top:var(--s3);font-size:var(--small)}.assistant-teaser{background:var(--tint);border:1px solid #CEDFD4;padding:var(--s4);border-radius:var(--panel);display:flex;flex-direction:column;align-items:flex-start;gap:var(--s3)}.assistant-symbol{width:40px;height:40px;background:white;border-radius:12px;display:flex;align-items:center;justify-content:center;color:var(--green)}.assistant-teaser h2{font:400 28px/1.2 Georgia,serif;max-width:240px}.assistant-teaser p{font-size:var(--small);color:var(--muted)}.example-message{background:#ffffffa6;padding:var(--s3);font-size:var(--small);border-radius:var(--radius);width:100%;color:var(--green)}.assistant-teaser .text-btn{margin-top:auto}.empty-state{display:grid;justify-items:center;text-align:center;gap:var(--s2);padding:var(--s5) var(--s3)}.empty-icon{width:48px;height:48px;display:flex;align-items:center;justify-content:center;background:var(--bg);border:1px solid var(--line);border-radius:12px;color:var(--muted);margin-bottom:var(--s2)}.empty-state p{color:var(--muted);max-width:400px;font-size:var(--small)}.list-head,.transaction{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr) 104px minmax(120px,1fr) 48px;gap:var(--s3);align-items:center}.list-head{font-size:12px;color:var(--muted);padding:var(--s2) 0 var(--s3);border-bottom:1px solid var(--line)}.transaction{padding:var(--s3) 0;border-bottom:1px solid var(--line);font-size:var(--small)}.transaction:last-child{border-bottom:0}.tx-title{display:flex;align-items:center;gap:var(--s3);min-width:0}.tx-icon{display:flex;justify-content:center;align-items:center;width:40px;height:40px;background:var(--bg);border-radius:var(--radius);flex:none}.tx-description{padding:0;border:0;background:none;color:var(--ink);text-align:left;font-weight:600;max-width:100%;min-height:44px}.tx-amount{text-align:right;font-weight:650;white-space:nowrap}.category-pill{display:inline-block;background:var(--bg);border-radius:var(--radius);padding:var(--s1) var(--s2);font-size:12px;max-width:100%}.footer-note{display:flex;align-items:center;justify-content:space-between;gap:var(--s3);font-size:12px;color:var(--muted);margin-top:var(--s4)}.filters{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr) minmax(0,1fr);gap:var(--s3);margin-bottom:var(--s4)}label{display:block;font-size:var(--small);font-weight:600;margin-bottom:var(--s2)}input,select,textarea{width:100%;min-height:44px;border:1px solid var(--line);background:white;padding:var(--s2) var(--s3);color:var(--ink)}textarea{resize:vertical}input[aria-invalid=true]{border-color:var(--negative)}.pagination{display:flex;align-items:center;justify-content:space-between;gap:var(--s3);margin-top:var(--s4);font-size:var(--small)}.notice{padding:var(--s3);border:1px solid var(--negative);color:var(--negative);background:white;border-radius:var(--radius);margin-bottom:var(--s4)}.notice a{color:var(--negative)}.error{display:block;color:var(--negative);font-size:var(--small);margin-top:var(--s1)}dialog{border:1px solid var(--line);border-radius:var(--panel);padding:var(--s5);max-width:560px;width:calc(100% - 32px);max-height:calc(100dvh - 48px);overflow:auto;background:white;color:var(--ink);box-shadow:var(--shadow)}dialog::backdrop{background:#17262265}dialog h2{font:400 28px/1.25 Georgia,serif}.dialog-head{display:flex;justify-content:space-between;align-items:center;gap:var(--s3);margin-bottom:var(--s4)}.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:var(--s3)}.full{grid-column:1/-1}.dialog-actions{display:flex;justify-content:flex-end;flex-wrap:wrap;gap:var(--s2);margin-top:var(--s4)}.detail-list{display:grid;grid-template-columns:100px minmax(0,1fr);gap:var(--s3);margin:var(--s4) 0}.detail-list dt{color:var(--muted)}.detail-list dd{margin:0;overflow-wrap:anywhere}.chat-layout{display:grid;grid-template-columns:minmax(0,1fr) 256px;gap:var(--s4)}.chat-panel{background:white;border:1px solid var(--line);border-radius:var(--panel);display:grid;grid-template-rows:auto minmax(240px,1fr) auto;min-height:560px;max-height:calc(100dvh - 240px)}.chat-top{display:flex;align-items:center;gap:var(--s3);padding:var(--s3) var(--s4);border-bottom:1px solid var(--line)}.chat-messages{padding:var(--s4);display:flex;flex-direction:column;gap:var(--s3);overflow:auto;scroll-behavior:smooth}.message{max-width:90%;align-self:flex-start;white-space:pre-wrap;overflow-wrap:anywhere;border-radius:var(--radius);padding:var(--s3);background:var(--bg);font-size:var(--small)}.message.user{align-self:flex-end;background:var(--green);color:white}.message p{white-space:pre-wrap}.message .dialog-actions{margin-top:var(--s3);justify-content:flex-start}.message strong{display:block;margin-bottom:var(--s2)}.chat-compose{padding:var(--s3) var(--s4);border-top:1px solid var(--line)}.compose-row{display:flex;gap:var(--s2);align-items:flex-end}.compose-row textarea{min-height:48px;max-height:120px}.compose-row button{min-height:48px}.chat-hint{font-size:12px;color:var(--muted);margin-top:var(--s2)}.chat-guide{display:flex;flex-direction:column;gap:var(--s4);padding:var(--s2) 0}.chat-guide p{font-size:var(--small);color:var(--muted)}.suggestion{display:block;text-align:left;background:white;color:var(--green);border:1px solid var(--line);padding:var(--s3);border-radius:var(--radius);width:100%;margin-top:var(--s2);font-size:var(--small);min-height:44px}.toast{position:fixed;bottom:var(--s4);left:50%;transform:translateX(-50%);padding:var(--s3) var(--s4);color:white;background:var(--ink);border-radius:var(--radius);box-shadow:var(--shadow);max-width:calc(100% - 32px);z-index:10;font-size:var(--small)}.skip{position:fixed;top:8px;left:8px;background:white;padding:8px;z-index:20;transform:translateY(-150%)}.skip:focus{transform:none}@media(hover:hover){.btn:hover{opacity:.88}.nav-link:hover{background:var(--bg);color:var(--green)}.nav-link.active:hover{background:var(--tint)}.icon-btn:hover{background:var(--tint);color:var(--green)}.text-btn:hover,.tx-description:hover{text-decoration:underline}.suggestion:hover{background:var(--tint)}}
@media(min-width:1440px){main{padding:var(--s6)}.topbar{padding-inline:var(--s6)}}
@media(max-width:1200px){:root{--sidebar:208px}.sidebar{padding-inline:var(--s3)}main{padding:var(--s4)}.page-head{align-items:flex-start;flex-direction:column}.chat-layout{grid-template-columns:minmax(0,1fr) 208px}.stat-card{padding:var(--s3)}}
@media(max-width:1023px){.app{grid-template-columns:1fr}.sidebar{position:static;height:auto;padding:var(--s3) var(--s4);border-right:0;border-bottom:1px solid var(--line);flex-direction:row;align-items:center;gap:var(--s4)}.sidebar nav{flex-direction:row;margin-left:auto;gap:var(--s2)}.sidebar-bottom,.nav-caption,.topbar{display:none}.nav-link{gap:var(--s2);padding:var(--s2) var(--s3)}.chat-panel{max-height:680px}.overview-grid{grid-template-columns:minmax(0,1.4fr) minmax(260px,1fr)}}
@media(max-width:767px){.sidebar{flex-direction:column;align-items:stretch;gap:var(--s3);padding:var(--s3)}.brand{align-self:center;font-size:24px}.sidebar nav{margin:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}.nav-link{justify-content:center;padding:var(--s2);font-size:12px;gap:var(--s2)}.nav-link svg{width:16px;height:16px}main{padding:var(--s4) var(--s3)}.page-head{gap:var(--s4);margin-bottom:var(--s4)}.page-head p{font-size:var(--small)}.actions{width:100%;gap:var(--s2);justify-content:space-between}.actions .btn{font-size:var(--small)}.month-control{padding-inline:var(--s2)}.month-control input{width:136px}.stats{grid-template-columns:1fr 1fr;gap:var(--s3)}.balance{grid-column:1/-1}.stat-value{font-size:clamp(20px,5.4vw,32px)}.stat-card.balance .stat-value{font-size:32px}.overview-grid{grid-template-columns:1fr;gap:var(--s3)}.panel{padding:var(--s3)}.assistant-teaser h2{max-width:none}.assistant-teaser{padding:var(--s4)}.list-head{display:none}.transaction{grid-template-columns:minmax(0,1fr) auto 44px;gap:var(--s2)}.tx-category,.tx-date{display:none}.tx-icon{display:none}.tx-amount{font-size:12px}.filters{grid-template-columns:1fr 1fr}.filters>div:first-child{grid-column:1/-1}.chat-layout{grid-template-columns:1fr}.chat-guide{order:-1;padding:0;gap:var(--s2)}.chat-guide .guide-text,.chat-guide .scope-note{display:none}.suggestions{display:grid;grid-template-columns:1fr 1fr;gap:var(--s2)}.suggestion{margin:0;padding:var(--s2);font-size:12px}.chat-panel{min-height:480px;max-height:none;height:620px}.chat-messages{padding:var(--s3)}.chat-compose{padding:var(--s3)}.chat-compose label{font-size:12px}.chat-top{padding:var(--s3)}.footer-note{align-items:flex-start;flex-direction:column;gap:var(--s2)}dialog{padding:var(--s4)}.panel-head{flex-wrap:wrap}.form-grid{grid-template-columns:1fr}.full{grid-column:auto}.message{max-width:96%}.message .btn{font-size:12px}.toast{bottom:var(--s3)}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
</style>
</head>
<body>
<a href="#main" class="skip">Pular para o conteúdo</a>
<svg aria-hidden="true" style="display:none"><defs>
<symbol id="i-mark" viewBox="0 0 24 24"><path d="M5 18V6h14M5 12h10M10 18l4-4 3 2 4-6"/></symbol>
<symbol id="i-grid" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></symbol>
<symbol id="i-arrows" viewBox="0 0 24 24"><path d="M3 7h17m-4-4 4 4-4 4M21 17H4m4-4-4 4 4 4"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24"><path d="M21 11a8 8 0 0 1-8 8H5l-4 3 2-7a8 8 0 1 1 18-4Z"/><path d="M8 10h8m-8 4h5"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="M12 4v16m-6-6 6 6 6-6"/></symbol>
<symbol id="i-up" viewBox="0 0 24 24"><path d="M12 20V4m-6 6 6-6 6 6"/></symbol>
<symbol id="i-wallet" viewBox="0 0 24 24"><path d="M20 7H5a2 2 0 0 1 0-4h13v4M3 5v14a2 2 0 0 0 2 2h15V7m0 5h-6v5h6"/><path d="M16 14.5h1"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M4 12h16m-6-6 6 6-6 6"/></symbol>
<symbol id="i-lock" viewBox="0 0 24 24"><rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3m-4 5v2"/></symbol>
<symbol id="i-chart" viewBox="0 0 24 24"><path d="M4 3v17h17M8 15v-4m5 4V6m5 9v-6"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><path d="m6 6 12 12M6 18 18 6"/></symbol>
<symbol id="i-edit" viewBox="0 0 24 24"><path d="m15 4 5 5M4 20l5-1L21 7a2 2 0 0 0-4-4L5 15l-1 5Z"/></symbol>
<symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4m10-4v4M3 11h18"/></symbol>
</defs></svg>
<div class="app">
<aside class="sidebar"><a class="brand" href="#overview" aria-label="FinAI — início"><span class="brand-mark"><svg><use href="#i-mark"/></svg></span><span>fin<span class="brand-ai">ai</span></span></a><nav aria-label="Navegação principal"><p class="nav-caption">SEU FINANCEIRO</p><a class="nav-link active" href="#overview" data-page="overview"><svg aria-hidden="true"><use href="#i-grid"/></svg>Visão geral</a><a class="nav-link" href="#transactions" data-page="transactions"><svg aria-hidden="true"><use href="#i-arrows"/></svg>Transações</a><a class="nav-link" href="#assistant" data-page="assistant"><svg aria-hidden="true"><use href="#i-chat"/></svg>Assistente</a></nav><div class="sidebar-bottom"><div class="local-note"><strong>Seu espaço pessoal</strong>Seus registros ficam salvos apenas neste navegador.</div><div class="profile od-row"><span class="avatar">EU</span><div class="od-field"><strong class="small">Minhas finanças</strong><span class="small muted">Conta local</span></div></div></div></aside>
<div class="workspace"><header class="topbar"><div class="breadcrumb"><span>Meu espaço</span><span aria-hidden="true">/</span><strong id="breadcrumb">Visão geral</strong></div><div class="top-right"><span class="badge"><span class="dot"></span>Armazenamento local</span><span class="avatar" aria-hidden="true">EU</span></div></header>
<main id="main" tabindex="-1"><div id="storage-error" class="notice" role="alert" hidden></div>
<div class="page-head"><div><h1 id="page-title">Seu dinheiro, com clareza.</h1><p id="page-subtitle">Um olhar simples para cuidar da sua vida financeira.</p></div><div class="actions"><label class="month-control" id="month-wrap"><svg aria-hidden="true"><use href="#i-calendar"/></svg><input type="month" id="month" aria-label="Mês de referência"></label><button class="btn" id="new-transaction"><svg aria-hidden="true"><use href="#i-plus"/></svg>Nova transação</button></div></div>
<section id="overview" aria-label="Visão geral">
<div class="stats"><article class="stat-card balance"><div class="stat-label">Saldo geral<span class="stat-symbol"><svg aria-hidden="true"><use href="#i-wallet"/></svg></span></div><div class="od-stat"><strong class="stat-value number" id="balance">R$ 0,00</strong><span class="stat-foot">Todas as suas movimentações</span></div></article><article class="stat-card"><div class="stat-label">Receitas do mês<span class="stat-symbol"><svg aria-hidden="true"><use href="#i-down"/></svg></span></div><div class="od-stat"><strong class="stat-value number" id="income">R$ 0,00</strong><span class="stat-foot" id="income-count">Nenhuma receita registrada</span></div></article><article class="stat-card"><div class="stat-label">Despesas do mês<span class="stat-symbol"><svg aria-hidden="true"><use href="#i-up"/></svg></span></div><div class="od-stat"><strong class="stat-value number" id="expense">R$ 0,00</strong><span class="stat-foot" id="expense-count">Nenhuma despesa registrada</span></div></article></div>
<div class="overview-grid"><section class="panel"><div class="panel-head"><div><h2>Balanço do mês</h2><p id="chart-month"></p></div><div class="legend"><span><i></i>Receitas</span><span class="out"><i></i>Despesas</span></div></div><div class="graph" id="graph"></div><div class="graph-foot"><span class="muted">Resultado do mês</span><strong class="number" id="month-result">R$ 0,00</strong></div></section><aside class="assistant-teaser"><div class="od-row" style="width:100%;justify-content:space-between"><span class="assistant-symbol"><svg aria-hidden="true"><use href="#i-chat"/></svg></span><span class="badge">Assistente simulado</span></div><h2>Suas finanças.<br>Uma boa conversa.</h2><p>Registre um gasto ou consulte seus números do jeito que você fala.</p><div class="example-message">“Gastei R$ 35 no almoço hoje”</div><button class="text-btn" id="open-chat">Conversar com o assistente<svg aria-hidden="true"><use href="#i-arrow"/></svg></button></aside></div>
<section class="panel"><div class="panel-head"><div><h2>Últimas movimentações</h2><p>Os registros mais recentes do seu histórico.</p></div><a class="text-btn" href="#transactions">Ver todas<svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div><div id="recent"></div></section>
</section>
<section id="transactions" hidden aria-label="Transações"><div class="panel"><div class="filters"><div><label for="search">Buscar descrição</label><input type="search" id="search" placeholder="O que você procura?"></div><div><label for="type-filter">Tipo</label><select id="type-filter"><option value="">Todos os tipos</option><option value="income">Receitas</option><option value="expense">Despesas</option></select></div><div><label for="category-filter">Categoria</label><select id="category-filter"><option value="">Todas as categorias</option></select></div></div><div class="od-row" style="justify-content:space-between;margin-bottom:16px"><span class="small muted" id="filter-count"></span><button class="text-btn" id="clear-filters">Limpar filtros</button></div><div id="history"></div><div class="pagination" id="pagination" hidden><button class="btn secondary" id="prev-page">Anterior</button><span id="page-count"></span><button class="btn secondary" id="next-page">Próxima</button></div></div></section>
<section id="assistant" hidden aria-label="Assistente financeiro"><div class="chat-layout"><div class="chat-panel"><div class="chat-top"><span class="assistant-symbol" style="background:var(--tint)"><svg aria-hidden="true"><use href="#i-chat"/></svg></span><div class="od-field od-fill"><strong>Assistente FinAI</strong><span class="small muted">Respostas a partir dos seus registros</span></div><span class="badge">Simulado</span></div><div class="chat-messages" id="messages" role="log" aria-label="Conversa com o assistente" aria-live="polite"></div><form id="chat-form" class="chat-compose"><label for="chat-input">Sua mensagem</label><div class="compose-row"><textarea id="chat-input" rows="1" maxlength="500" placeholder="Ex.: Gastei R$ 35 no almoço" required></textarea><button class="btn" id="send-message" aria-label="Enviar mensagem"><svg aria-hidden="true"><use href="#i-up"/></svg></button></div><p class="chat-hint">Assistente por regras, sem IA real. Todo registro pede sua confirmação.</p></form></div><aside class="chat-guide"><div class="guide-text"><p class="eyebrow" style="margin-bottom:16px">CONVERSE COM SEUS NÚMEROS</p><h2>Por onde começar?</h2><p style="margin-top:8px">Use uma sugestão ou escreva com suas palavras.</p></div><div class="suggestions"><button class="suggestion" data-suggest="Qual é meu saldo?">Qual é meu saldo?</button><button class="suggestion" data-suggest="Quanto gastei este mês?">Quanto gastei este mês?</button><button class="suggestion" data-suggest="Quais são minhas últimas movimentações?">Últimas movimentações</button><button class="suggestion" data-suggest="Gastei R$ 35 no almoço hoje">Registrar um gasto</button></div><div class="scope-note"><svg aria-hidden="true" style="color:var(--green);margin-bottom:16px"><use href="#i-lock"/></svg><h3>Você tem o controle.</h3><p style="margin-top:8px">Revise valor, categoria e data antes de confirmar. Nenhum registro é criado sem sua autorização.</p></div></aside></div></section>
<footer class="footer-note"><span>FinAI · Um passo de cada vez, suas finanças em dia.</span><span class="od-row"><svg aria-hidden="true" style="width:16px;height:16px"><use href="#i-lock"/></svg>Dados salvos neste navegador</span></footer>
</main></div></div>
<dialog id="transaction-dialog" aria-labelledby="form-title"><div class="dialog-head"><h2 id="form-title">Nova transação</h2><button class="icon-btn" data-close="transaction-dialog" aria-label="Fechar formulário"><svg><use href="#i-close"/></svg></button></div><form id="transaction-form" novalidate><p class="small muted" style="margin-bottom:24px">Todos os campos são obrigatórios.</p><div id="form-summary" class="notice" role="alert" hidden></div><div class="form-grid"><div><label for="tx-type">Tipo</label><select id="tx-type" required><option value="expense">Despesa</option><option value="income">Receita</option></select></div><div><label for="tx-value">Valor (R$)</label><input id="tx-value" inputmode="decimal" placeholder="0,00" required aria-describedby="value-error"><span id="value-error" class="error"></span></div><div class="full"><label for="tx-description">Descrição</label><input id="tx-description" maxlength="120" placeholder="Ex.: Almoço" required aria-describedby="description-error"><span id="description-error" class="error"></span></div><div><label for="tx-category">Categoria</label><select id="tx-category" required></select></div><div><label for="tx-date">Data</label><input type="date" id="tx-date" required aria-describedby="date-error"><span id="date-error" class="error"></span></div></div><div class="dialog-actions"><button type="button" class="btn secondary" data-close="transaction-dialog">Cancelar</button><button class="btn" id="save-transaction">Salvar transação</button></div></form></dialog>
<dialog id="detail-dialog" aria-labelledby="detail-title"><div class="dialog-head"><h2 id="detail-title">Detalhes da transação</h2><button class="icon-btn" data-close="detail-dialog" aria-label="Fechar detalhes"><svg><use href="#i-close"/></svg></button></div><dl id="detail-content" class="detail-list"></dl><div class="dialog-actions"><button class="btn secondary" id="delete-transaction">Excluir</button><button class="btn" id="edit-transaction">Editar transação</button></div></dialog>
<dialog id="delete-dialog" aria-labelledby="delete-title"><h2 id="delete-title">Excluir esta transação?</h2><p style="margin-top:16px">O registro será removido do histórico e dos totais. Esta ação não pode ser desfeita.</p><div class="dialog-actions"><button class="btn secondary" data-close="delete-dialog">Cancelar</button><button class="btn danger" id="confirm-delete">Excluir transação</button></div></dialog>
<div class="toast" id="toast" role="status" hidden></div>
<script>
'use strict';
const $=id=>document.getElementById(id), esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const icon=name=>`<svg aria-hidden="true"><use href="#i-${name}"/></svg>`;
const cats={income:['Salário','Freelance','Rendimentos','Outras receitas'],expense:['Alimentação','Moradia','Transporte','Saúde','Educação','Lazer','Compras','Outras despesas']};
const KEY='finai.transactions.v1', norm=s=>String(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim();
function localDate(d=new Date()){return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`}
const today=()=>localDate(), fmt=n=>new Intl.NumberFormat('pt-BR',{style:'currency',currency:'BRL'}).format(n/100), dateFmt=s=>s.split('-').reverse().join('/');
function validDate(s){if(!/^\d{4}-\d{2}-\d{2}$/.test(s))return false;const d=new Date(s+'T12:00:00');return !isNaN(d)&&localDate(d)===s&&Number(s.slice(0,4))>=1900}
function money(raw){let s=String(raw).trim().replace(/R\$/gi,'').replace(/\s/g,'');if(!s||!/^\d+(?:[.,]\d+)*$/.test(s))return null;if(s.includes(',')){if(!/^\d{1,3}(?:\.\d{3})*,\d{1,2}$/.test(s)&&!/^\d+,\d{1,2}$/.test(s))return null;s=s.replace(/\./g,'').replace(',','.')}else if(/^\d{1,3}(?:\.\d{3})+$/.test(s)){s=s.replace(/\./g,'')}else if(!/^\d+(?:\.\d{1,2})?$/.test(s))return null;const n=Math.round(Number(s)*100);return Number.isSafeInteger(n)&&n>0&&n<=99999999999?n:null}
function storageError(message){$('storage-error').textContent=message;$('storage-error').hidden=false}
let records=[],readBlocked=false;
try{const raw=localStorage.getItem(KEY);if(raw!==null){const data=JSON.parse(raw);if(!Array.isArray(data)||!data.every(x=>x&&typeof x.id==='string'&&['income','expense'].includes(x.type)&&typeof x.description==='string'&&x.description.trim()&&Number.isSafeInteger(x.value)&&x.value>0&&validDate(x.date)&&cats[x.type].includes(x.category))||new Set(data.map(x=>x.id)).size!==data.length)throw Error('data');records=data}}catch(e){readBlocked=true;storageError('Não foi possível ler os dados locais. Para proteger registros existentes, o salvamento está bloqueado. Verifique as permissões do navegador e reabra a página. Os totais abaixo não representam dados recuperados.')}
function persist(next){if(readBlocked){notify('Salvamento bloqueado: não foi possível ler os dados existentes.');return false}try{localStorage.setItem(KEY,JSON.stringify(next));records=next;$('storage-error').hidden=true;return true}catch(e){storageError('Não foi possível salvar. Libere espaço ou permita o armazenamento neste navegador e tente novamente. A alteração não foi aplicada.');return false}}
function uid(){return globalThis.crypto?.randomUUID?.()||Date.now().toString(36)+'-'+Math.random().toString(36).slice(2)}
let toastTimer;function notify(t){$('toast').textContent=t;$('toast').hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('toast').hidden=true,4500)}
let page=1,editId=null,detailId=null,chatCorrection=false,pending=null,proposalVersion=0,chatBusy=false;
$('month').value=today().slice(0,7);
Object.values(cats).flat().forEach(c=>{const o=new Option(c,c);$('category-filter').add(o)});
function sum(items,type){return items.filter(x=>!type||x.type===type).reduce((n,x)=>n+x.value,0)}
function monthLabel(m){if(!m)return'Todo o histórico';return new Intl.DateTimeFormat('pt-BR',{month:'long',year:'numeric'}).format(new Date(m+'-01T12:00:00'))}
function sorted(items){return [...items].sort((a,b)=>b.date.localeCompare(a.date)||(b.created||0)-(a.created||0))}
function empty(title,text,action){return `<div class="empty-state"><span class="empty-icon">${icon('wallet')}</span><h3>${esc(title)}</h3><p>${esc(text)}</p>${action?'<button class="text-btn" data-new>Registrar primeira transação '+icon('plus')+'</button>':''}</div>`}
function list(items){if(!items.length)return empty('Tudo começa com um registro','Adicione uma receita ou despesa para acompanhar seu dinheiro.',true);return `<div class="list-head"><span>Descrição</span><span>Categoria</span><span>Data</span><span style="text-align:right">Valor</span><span></span></div>`+items.map(t=>`<div class="transaction"><div class="tx-title"><span class="tx-icon ${t.type==='income'?'positive':'negative'}">${icon(t.type==='income'?'down':'up')}</span><button class="tx-description od-truncate" data-detail="${esc(t.id)}">${esc(t.description)}</button></div><div class="tx-category"><span class="category-pill">${esc(t.category)}</span></div><span class="tx-date muted">${dateFmt(t.date)}</span><span class="tx-amount number ${t.type==='income'?'positive':'negative'}">${t.type==='income'?'+':'−'} ${fmt(t.value)}</span><button class="icon-btn" data-detail="${esc(t.id)}" aria-label="Ver detalhes de ${esc(t.description)}">${icon('arrow')}</button></div>`).join('')}
function render(){const m=$('month').value,monthly=records.filter(t=>!m||t.date.startsWith(m)),inc=sum(monthly,'income'),out=sum(monthly,'expense');$('balance').textContent=readBlocked?'Indisponível':fmt(sum(records,'income')-sum(records,'expense'));$('income').textContent=readBlocked?'—':fmt(inc);$('expense').textContent=readBlocked?'—':fmt(out);for(const type of ['income','expense']){const n=monthly.filter(x=>x.type===type).length;$(`${type}-count`).textContent=n?`${n} ${type==='income'?(n===1?'receita registrada':'receitas registradas'):(n===1?'despesa registrada':'despesas registradas')}`:`Nenhuma ${type==='income'?'receita':'despesa'} registrada`}$('chart-month').textContent=monthLabel(m);$('month-result').textContent=readBlocked?'—':fmt(inc-out);$('month-result').className='number '+(inc-out<0?'negative':'positive');const max=Math.max(inc,out,1);$('graph').innerHTML=monthly.length?['income','expense'].map(type=>`<div class="bar-row"><span>${type==='income'?'Receitas':'Despesas'}</span><div><strong class="number">${fmt(type==='income'?inc:out)}</strong><div class="bar-track"><div class="bar ${type==='expense'?'expense':''}" style="width:${(type==='income'?inc:out)/max*100}%"></div></div></div></div>`).join(''):`<div class="chart-empty">${icon('chart')}<strong>Seu próximo passo aparece aqui.</strong><p>Registre suas movimentações para comparar receitas e despesas.</p></div>`;$('recent').innerHTML=list(sorted(records).slice(0,5));renderHistory()}
function renderHistory(){const m=$('month').value,q=norm($('search').value),type=$('type-filter').value,cat=$('category-filter').value;const rows=sorted(records.filter(t=>(!m||t.date.startsWith(m))&&(!type||t.type===type)&&(!cat||t.category===cat)&&norm(t.description).includes(q)));const pages=Math.max(1,Math.ceil(rows.length/50));page=Math.min(page,pages);$('filter-count').textContent=`${rows.length} ${rows.length===1?'transação':'transações'} · ${monthLabel(m)}`;$('history').innerHTML=rows.length?list(rows.slice((page-1)*50,page*50)):records.length?empty('Nenhuma transação encontrada','Altere o mês ou limpe os filtros para consultar outros registros.',false):empty('Seu histórico começa aqui','Registre sua primeira movimentação manualmente ou pelo assistente.',true);$('pagination').hidden=pages<=1;$('page-count').textContent=`${page} de ${pages}`;$('prev-page').disabled=page===1;$('next-page').disabled=page===pages}
const titles={overview:['Seu dinheiro, com clareza.','Um olhar simples para cuidar da sua vida financeira.','Visão geral'],transactions:['Cada movimento conta.','Organize, encontre e acompanhe suas receitas e despesas.','Transações'],assistant:['Vamos falar de dinheiro.','Registre e consulte suas finanças em uma conversa simples.','Assistente']};
const scrolls={};let current='overview';function route(){scrolls[current]=window.scrollY;const requested=location.hash.slice(1);const p=titles[requested]?requested:'overview';current=p;Object.keys(titles).forEach(k=>$(k).hidden=k!==p);document.querySelectorAll('[data-page]').forEach(a=>{a.classList.toggle('active',a.dataset.page===p);if(a.dataset.page===p)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});$('page-title').textContent=titles[p][0];$('page-subtitle').textContent=titles[p][1];$('breadcrumb').textContent=titles[p][2];$('month-wrap').hidden=p==='assistant';window.scrollTo(0,scrolls[p]||0)}
window.addEventListener('hashchange',route);$('open-chat').onclick=()=>location.hash='assistant';$('month').onchange=()=>{if(!$('month').value)$('month').value=today().slice(0,7);page=1;render()};['search','type-filter','category-filter'].forEach(id=>$(id).addEventListener(id==='search'?'input':'change',()=>{page=1;renderHistory()}));$('clear-filters').onclick=()=>{$('search').value='';$('type-filter').value='';$('category-filter').value='';$('month').value='';page=1;render()};$('prev-page').onclick=()=>{page--;renderHistory()};$('next-page').onclick=()=>{page++;renderHistory()};
function categoryOptions(type,selected){$('tx-category').replaceChildren(...cats[type].map(c=>new Option(c,c,false,c===selected)))}
function resetErrors(){['value','description','date'].forEach(k=>{$(`${k}-error`).textContent='';$(`tx-${k}`).removeAttribute('aria-invalid')});$('form-summary').hidden=true}
function openForm(t=null,correction=false){editId=correction?null:t?.id||null;chatCorrection=correction;resetErrors();$('form-title').textContent=correction?'Corriger le registre':editId?'Editar transação':'Nova transação';if(correction)$('form-title').textContent='Revisar proposta';$('tx-type').value=t?.type||'expense';categoryOptions($('tx-type').value,t?.category);$('tx-value').value=t?.value?(t.value/100).toFixed(2).replace('.',','):'';$('tx-description').value=t?.description||'';$('tx-date').value=t?.date||today();$('save-transaction').textContent=correction?'Revisar no chat':'Salvar transação';$('transaction-dialog').showModal()}
$('new-transaction').onclick=()=>openForm();$('tx-type').onchange=()=>categoryOptions($('tx-type').value);document.addEventListener('click',e=>{const close=e.target.closest('[data-close]');if(close)$(close.dataset.close).close();if(e.target.closest('[data-new]'))openForm();const d=e.target.closest('[data-detail]');if(d)openDetail(d.dataset.detail)});
function fieldError(k){let msg='';if(k==='value'&&money($('tx-value').value)===null)msg='Informe um valor maior que zero, até R$ 999.999.999,99.';if(k==='description'&&!$('tx-description').value.trim())msg='Dê um nome à movimentação, como “Almoço”.';if(k==='date'&&!validDate($('tx-date').value))msg='Escolha uma data válida a partir de 1900.';$(`${k}-error`).textContent=msg;$(`tx-${k}`).setAttribute('aria-invalid',String(!!msg));return msg}
['value','description','date'].forEach(k=>$(`tx-${k}`).addEventListener('blur',()=>fieldError(k)));
$('transaction-form').onsubmit=async e=>{e.preventDefault();const errors=['value','description','date'].filter(k=>fieldError(k));if(errors.length){$('form-summary').innerHTML='<strong>Confira os campos abaixo:</strong><br>'+errors.map(k=>`<a href="#tx-${k}" data-field="tx-${k}">${esc($(`${k}-error`).textContent)}</a>`).join('<br>');$('form-summary').hidden=false;$(`tx-${errors[0]}`).focus();return}const t={id:editId||uid(),type:$('tx-type').value,value:money($('tx-value').value),description:$('tx-description').value.trim(),category:$('tx-category').value,date:$('tx-date').value,created:records.find(x=>x.id===editId)?.created||Date.now()};if(chatCorrection){pending=t;$('transaction-dialog').close();location.hash='assistant';showProposal();return}const b=$('save-transaction');b.disabled=true;b.textContent='Salvando…';await new Promise(r=>setTimeout(r,180));const ok=persist(editId?records.map(x=>x.id===editId?t:x):[...records,t]);b.disabled=false;b.textContent='Salvar transação';if(ok){$('transaction-dialog').close();render();notify(editId?'Transação atualizada.':'Transação registrada.')}};
$('form-summary').onclick=e=>{const a=e.target.closest('[data-field]');if(a){e.preventDefault();$(a.dataset.field).focus()}};
function openDetail(id){const t=records.find(x=>x.id===id);if(!t)return;detailId=id;$('detail-content').innerHTML=[['Descrição',t.description],['Tipo',t.type==='income'?'Receita':'Despesa'],['Valor',fmt(t.value)],['Categoria',t.category],['Data',dateFmt(t.date)]].map(([k,v])=>`<dt>${k}</dt><dd>${esc(v)}</dd>`).join('');$('detail-dialog').showModal()}
$('edit-transaction').onclick=()=>{const t=records.find(x=>x.id===detailId);$('detail-dialog').close();if(t)openForm(t)};$('delete-transaction').onclick=()=>$('delete-dialog').showModal();$('confirm-delete').onclick=()=>{if(persist(records.filter(x=>x.id!==detailId))){$('delete-dialog').close();$('detail-dialog').close();render();notify('Transação excluída.')}};
function addMessage(text,role='assistant'){const el=document.createElement('div');el.className='message '+role;el.textContent=text;$('messages').append(el);$('messages').scrollTop=$('messages').scrollHeight;return el}
function invalidateProposals(){document.querySelectorAll('[data-proposal]').forEach(b=>b.disabled=true);proposalVersion++}
function cancelProposal(){pending=null;invalidateProposals();addMessage('Proposta cancelada. Nenhuma transação foi registrada.')}
function showProposal(){invalidateProposals();const version=proposalVersion;const p={...pending};const el=addMessage('');const strong=document.createElement('strong');strong.textContent='Confira antes de registrar';el.append(strong);const body=document.createElement('p');body.textContent=`${p.type==='income'?'Receita':'Despesa'} · ${fmt(p.value)}\n${p.description}\nCategoria: ${p.category}\nData: ${dateFmt(p.date)}`;el.append(body);const actions=document.createElement('div');actions.className='dialog-actions';for(const [label,action,cls] of [['Confirmar','confirm','btn'],['Corrigir','correct','btn secondary'],['Cancelar','cancel','btn secondary']]){const b=document.createElement('button');b.textContent=label;b.className=cls;b.dataset.proposal=String(version);b.onclick=()=>{if(version!==proposalVersion||!pending)return;if(action==='cancel')cancelProposal();else if(action==='correct')openForm(pending,true);else{if(readBlocked){addMessage('Não consigo registrar enquanto o armazenamento estiver indisponível.');return}const record={...pending,id:uid(),created:Date.now()};if(persist([...records,record])){pending=null;invalidateProposals();render();addMessage(`Registrado: ${record.description}, ${fmt(record.value)}. Seu dashboard já foi atualizado.`)}else addMessage('Não consegui salvar no navegador. A proposta continua pendente; tente confirmar novamente depois de liberar o armazenamento.')}};actions.append(b)}el.append(actions);$('messages').scrollTop=$('messages').scrollHeight}
const categoryRules=[['Alimentação',/almoc|jantar|comida|mercado|restaurante|lanche|cafe|padaria|aliment/],['Moradia',/aluguel|condominio|energia|luz|agua|internet|moradia/],['Transporte',/uber|onibus|gasolina|combustivel|taxi|metro|transporte/],['Saúde',/farmacia|remedio|medico|consulta|saude/],['Educação',/curso|livro|escola|faculdade|educacao/],['Lazer',/cinema|show|passeio|netflix|lazer/],['Compras',/roupa|sapato|compras|presente/],['Salário',/salario/],['Freelance',/freelance|freela/],['Rendimentos',/rendimento|dividendo|juros/]];
function inferCategory(s,type){return categoryRules.find(([c,re])=>cats[type].includes(c)&&re.test(norm(s)))?.[0]||cats[type].at(-1)}
function parseDate(text){const n=norm(text);const numeric=n.match(/\b(\d{1,2})\/(\d{1,2})(?:\/(\d{4}))?\b/),iso=n.match(/\b\d{4}-\d{2}-\d{2}\b/);if(iso)return{date:validDate(iso[0])?iso[0]:null,invalid:!validDate(iso[0])};if(numeric){const s=`${numeric[3]||new Date().getFullYear()}-${numeric[2].padStart(2,'0')}-${numeric[1].padStart(2,'0')}`;return{date:validDate(s)?s:null,invalid:!validDate(s)}}if(/\bontem\b/.test(n)){const d=new Date();d.setDate(d.getDate()-1);return{date:localDate(d)}}if(/\bhoje\b/.test(n))return{date:today()};if(/amanha|semana|mes passado|segunda|terca|quarta|quinta|sexta|sabado|domingo|dia\s+\d|janeiro|fevereiro|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro/.test(n))return{invalid:true};return{}}
function parseValue(text){let s=text.replace(/\b\d{4}-\d{2}-\d{2}\b/g,'').replace(/\b\d{1,2}\/\d{1,2}(?:\/\d{4})?\b/g,'').replace(/dia\s+\d+/gi,'');if(/(?:^|\s)-\s*(?:R\$\s*)?\d/i.test(s))return null;const match=s.match(/R\$\s*(\d+(?:[.,]\d+)*)/i)||s.match(/\b(\d+(?:[.,]\d+)*)\s*reais\b/i)||s.match(/\b(\d+(?:[.,]\d+)*)\b/);return match?money(match[1]):null}
function descriptionFrom(text){let s=text.replace(/\b\d{4}-\d{2}-\d{2}\b/g,'').replace(/\b\d{1,2}\/\d{1,2}(?:\/\d{4})?\b/g,'').replace(/R\$\s*\d+(?:[.,]\d+)*/gi,'').replace(/\b\d+(?:[.,]\d+)*\s*(?:reais)?\b/gi,'').replace(/\b(hoje|ontem|gastei|paguei|recebi|ganhei|registre|registrar|adicione|adicionar|uma|um|despesa|receita|de|em|no|na|com|por|valor|foi)\b/gi,' ').replace(/[?!.,;:]/g,' ').replace(/\s+/g,' ').trim();return s? s.charAt(0).toUpperCase()+s.slice(1,120):null}
function completePending(){if(!pending.type){addMessage('Essa movimentação é uma receita ou uma despesa?');return}if(!pending.value){addMessage('Qual é o valor? Informe, por exemplo, R$ 35,00.');return}if(!pending.description){addMessage('Qual é a descrição? Por exemplo: almoço, aluguel ou salário.');return}if(pending.needsDate){addMessage('Informe uma data válida no formato DD/MM/AAAA, ou diga “hoje”.');return}pending.date=pending.date||today();pending.category=pending.category||inferCategory(pending.description,pending.type);showProposal()}
function query(text){const n=norm(text);if(readBlocked){addMessage('Não posso consultar seus números porque os registros locais não puderam ser lidos. Verifique o aviso de armazenamento.');return}if(/saldo/.test(n)){addMessage(`Seu saldo geral é ${fmt(sum(records,'income')-sum(records,'expense'))}, considerando todas as ${records.length} movimentações cadastradas.${records.length?'':' Você ainda não registrou nenhuma transação.'}`);return}if(/ultim|movimentac|historico|transac/.test(n)&&!/(quanto|total|gastei|recebi)/.test(n)){const last=sorted(records).slice(0,5);addMessage(last.length?'Últimas movimentações, considerando todo o histórico:\n'+last.map(t=>`${dateFmt(t.date)} · ${t.description} · ${t.type==='income'?'+':'−'} ${fmt(t.value)}`).join('\n'):'Você ainda não tem movimentações registradas. Para começar, diga “Gastei R$ 35 no almoço hoje”.');return}let m=today().slice(0,7),day=null,all=/todo o historico|todos os registros|desde o inicio/.test(n);const date=parseDate(text);if(/mes passado|mes anterior/.test(n)){const d=new Date();d.setDate(1);d.setMonth(d.getMonth()-1);m=localDate(d).slice(0,7)}else if(date.date){day=date.date}else if(date.invalid){addMessage('Para essa consulta, informe “este mês”, “mês passado”, “hoje”, “ontem” ou uma data DD/MM/AAAA.');return}const namedMonth=/janeiro|fevereiro|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro/.test(n);if(namedMonth){addMessage('Consigo consultar este mês, mês passado ou uma data específica no formato DD/MM/AAAA. Qual período você quer?');return}let items=records.filter(t=>all||day?t.date===day||all:t.date.startsWith(m));const category=Object.values(cats).flat().find(c=>n.includes(norm(c)))||categoryRules.find(([,r])=>r.test(n))?.[0];if(category)items=items.filter(t=>t.category===category);const type=/receita|recebi|ganhei|entrou|entrada/.test(n)?'income':'expense';const total=sum(items,type);const period=all?'todo o histórico':day?dateFmt(day):monthLabel(m);const count=items.filter(t=>t.type===type).length;addMessage(`${type==='income'?'Receitas':'Despesas'}${category?' em '+category:''} · ${period}\nTotal: ${fmt(total)} em ${count} ${count===1?'registro':'registros'}.${count?'':' Não há movimentações correspondentes cadastradas.'}`)}
function handle(text){const n=norm(text);if(/^(cancelar|cancela|esquece)$/.test(n)){if(pending)cancelProposal();else addMessage('Não há uma proposta pendente.');return}if(pending){if(/^(confirmar|confirmo|sim)$/.test(n)){addMessage('Use o botão Confirmar na proposta revisada para registrar. Se ainda faltam campos, complete as informações primeiro.');return}if(/^(quanto|qual|quais|como|mostr|liste|consult)/.test(n)){addMessage('Há uma movimentação pendente. Confirme ou cancele a proposta antes de iniciar uma consulta.');return}invalidateProposals();const d=parseDate(text);const type=/receita|recebi|ganhei|entrada/.test(n)?'income':/despesa|gastei|paguei|saida/.test(n)?'expense':null;if(type&&pending.type!==type){pending.type=type;pending.category=null}const v=parseValue(text);if(v)pending.value=v;if(d.date){pending.date=d.date;pending.needsDate=false}else if(d.invalid)pending.needsDate=true;if(!pending.description){const desc=descriptionFrom(text);if(desc&&!/^(receita|despesa|hoje)$/i.test(desc))pending.description=desc}const cat=Object.values(cats).flat().find(c=>norm(c)===n);if(cat&&pending.type&&cats[pending.type].includes(cat))pending.category=cat;completePending();return}if(/^(quanto|qual|quais|como|mostr|liste|consult)|\b(saldo|total|historico|ultimas|resumo)\b/.test(n)||/gastei.*\?|recebi.*\?/.test(n)){query(text);return}const type=/\b(recebi|ganhei|receita|entrada)\b/.test(n)?'income':/\b(gastei|paguei|despesa|gasto|saida)\b/.test(n)?'expense':null;if(type||/registr|adicion|lanc/.test(n)){const d=parseDate(text);pending={type,value:parseValue(text),description:descriptionFrom(text),date:d.date||today(),needsDate:!!d.invalid,category:null};completePending();return}addMessage('Posso registrar receitas e despesas ou consultar seus números. Tente “Recebi R$ 3.000 de salário”, “Gastei R$ 35 no almoço” ou “Quanto gastei este mês?”. Não entendi sua última mensagem com segurança.')}
async function send(text){if(chatBusy||!text.trim())return;chatBusy=true;$('send-message').disabled=true;addMessage(text,'user');$('chat-input').value='';const progress=addMessage('Processando mensagem…');await new Promise(r=>setTimeout(r,220));progress.remove();try{handle(text)}catch(e){addMessage('Não consegui interpretar essa mensagem. Tente uma frase simples ou use Nova transação.')}chatBusy=false;$('send-message').disabled=false;$('chat-input').focus()}
$('chat-form').onsubmit=e=>{e.preventDefault();send($('chat-input').value)};$('chat-input').addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();send($('chat-input').value)}});document.querySelectorAll('[data-suggest]').forEach(b=>b.onclick=()=>send(b.dataset.suggest));
window.addEventListener('storage',e=>{if(e.key===KEY){storageError('Os registros foram alterados em outra aba. Reabra esta página antes de salvar para evitar sobrescrever alterações.');readBlocked=true;render()}});
addMessage('Olá! Vamos organizar suas finanças?\n\nSou o assistente simulado do FinAI. Posso registrar receitas e despesas com sua confirmação ou consultar os dados que você cadastrou.\n\nExperimente: “Gastei R$ 35 no almoço hoje”.');render();route();
</script>
</body></html>

````

### Arquivo: DESIGN-HANDOFF.md

````
# d5659f24-e48f-439f-bda3-af5cf97f4591 implementation handoff

This archive is the source of truth for turning the design into production code. Start from `index.html`, then preserve the visual system, responsive behavior, and interactions found in the exported files.

## Implementation target
- Build production UI from the exported design, not a loose reinterpretation.
- Preserve typography scale, spacing rhythm, color tokens, border radii, shadows, motion timing, and component states.
- Replace static placeholders only when the target app has real data or functional equivalents.
- Keep generated product UI free of OpenDesign chrome, preview labels, or design-process annotations.
- Treat this handoff as a visual contract: if implementation choices conflict, match the exported pixels and behavior first, then refactor internals.

## Source map
- Primary entry: `index.html`
- HTML screens detected: 1
- Stylesheets detected: 0
- Script/component files detected: 0
- Supporting assets detected: 0

## Responsive contract
Validate the implementation across this 2025–2026 viewport matrix:
- Mobile compact: 360×800
- Mobile standard: 390×844
- Mobile large: 430×932
- Foldable / small tablet: 600×960
- Tablet portrait: 820×1180
- Tablet landscape: 1024×768
- Laptop: 1366×768
- Desktop: 1440×900
- Wide desktop: 1920×1080

For responsive web exports, treat these as a modern breakpoint system for one adaptive web experience, not three fixed screenshots. Do not split responsive web into unrelated native app screens unless the project explicitly includes native targets. Use semantic layout thresholds, fluid `clamp()` type/spacing, and container queries where component width matters more than viewport width. Preserve any CSS media queries, container queries, fluid `clamp()` scales, and layout changes already present in the exported files.

## Design fidelity contract
- Extract reusable tokens before writing components: background, surface, foreground, muted text, border, accent, radius, shadow, spacing, type scale, and motion duration/easing.
- Map product screens, in-app modules/components, optional landing page, and optional OS widget surfaces before coding. Keep these surfaces separate in the target architecture.
- Match layout geometry: max-widths, gutters, grid columns, card proportions, sticky/fixed elements, and viewport-specific navigation.
- Preserve real copy, labels, and data shown in the export. Do not replace specific text with generic marketing filler.
- Preserve interactive affordances: hover, focus, pressed, disabled, loading, validation, copy/share, tab/accordion, modal/sheet, and keyboard states where present.
- Preserve accessibility semantics when converting: headings stay hierarchical, controls remain buttons/links/inputs, focus states stay visible.
- Do not keep prototype-only annotations, frame labels, or OpenDesign chrome in the production UI.

## CJX-ready UX contract
- Use `DESIGN-MANIFEST.json` as the machine-readable map for screens, app modules, OS widgets, landing pages, tokens, interactions, and viewport checks.
- Screen-file-first: when multiple user-facing surfaces exist, implement each HTML screen as its own route/file. Treat `index.html` as a launcher/overview when the manifest marks it that way, not as a combined final UI.
- If `landing.html`, app screens, platform screens, or OS widget files exist, preserve those boundaries in the target app instead of merging them into one page.
- A single self-contained `index.html` is acceptable only when the export truly contains one user-facing screen and its CSS/JS are structured enough to extract tokens, components, states, and behavior.
- If separate `css/` or `js/` files exist, treat them as source of truth for token/component/interactions before porting to React, Vue, SwiftUI, Compose, or another target stack.
- In-app modules/components are product UI blocks inside the app. OS widgets are home-screen/lock-screen/quick-access surfaces outside the app. Do not merge those concepts.

## Color and brand contract
- Use the exported design tokens and product/domain context as the color source of truth.
- Do not introduce warm beige / cream / peach / pink / orange-brown background washes unless they are already explicit brand/reference colors in the export.
- No obvious token stylesheet was detected; sample colors from the entry file and convert them into named tokens before coding.

## Implementation sequence for AI coding tools
1. Open `index.html` and `DESIGN-MANIFEST.json`; identify every screen file, launcher/overview file, app module, and interaction before coding.
2. If multiple HTML screens exist, map them to separate routes/surfaces first; do not merge `landing.html`, product app screens, platform screens, or OS widgets into one route.
3. Extract a token table from CSS/root styles and inline styles before building framework components.
4. Build product screens and domain-specific in-app modules from largest layout regions down to controls; avoid starting with isolated atoms that lose spatial intent.
5. Port responsive behavior across the modern viewport matrix and test each semantic breakpoint before cleanup.
6. Port interactions and states, then replace static placeholders only with real app data or functional equivalents.
7. Keep optional landing page and OS widget surfaces as separate surfaces if present.
8. Compare final screenshots against the export at 360×800, 390×844, 430×932, 820×1180, 1024×768, 1366×768, 1440×900, and 1920×1080 before declaring done.

## Entry points
- `index.html`

## Styles
- None detected

## Scripts/components
- None detected

## Assets and supporting files
- None detected

## Coding checklist for AI tools
1. Inspect `index.html` and `DESIGN-MANIFEST.json` first and identify reusable components before coding.
2. Implement each user-facing screen file as its own route/surface; keep launcher, landing, app, platform, and OS widget files separate.
3. Extract design tokens into the target stack: colors, type scale, spacing, radius, shadows, and motion.
4. Implement layout with real 2025–2026 responsive breakpoints, fluid type/spacing, and container-query-aware component behavior; test with no horizontal overflow.
5. Preserve interactive controls, hover/focus/pressed states, form behavior, validation, and copy actions where present.
6. Implement domain-specific in-app modules with real states; do not flatten them into generic cards.
7. Keep landing page, product screens, and OS widget/quick-access surfaces separate when present.
8. Confirm the production result visually matches the exported design before refactoring internals.
9. Reject implementation shortcuts that flatten the design into generic cards, generic gradients, placeholder stats, or framework-default typography.
10. If a detail is ambiguous, keep the exported HTML/CSS/JS behavior rather than inventing a new pattern.

````

### Arquivo: DESIGN-MANIFEST.json

````
{
  "schema": "open-design.design-manifest.v1",
  "title": "d5659f24-e48f-439f-bda3-af5cf97f4591",
  "entryFile": "index.html",
  "sourceFiles": {
    "all": [
      "index.html"
    ],
    "html": [
      "index.html"
    ],
    "css": [],
    "scriptsAndComponents": [],
    "assets": []
  },
  "screens": [
    {
      "file": "index.html",
      "role": "screen",
      "implementationNote": "Preserve visual hierarchy, responsive behavior, and interactive states from this screen."
    }
  ],
  "screenFilePolicy": {
    "mode": "screen-file-first",
    "entryFileRole": "primary-screen",
    "rules": [
      "Each distinct user-facing screen or surface must be delivered and implemented as its own file/route.",
      "If a landing page is present or requested, keep it in landing.html and do not merge it into the product app screen.",
      "When multiple HTML screens exist, index.html is a launcher/overview only; it must not be treated as the combined final UI.",
      "Keep product app screens, landing pages, platform screens, and OS widget surfaces separate in production code."
    ]
  },
  "appModules": [
    "Identify domain-specific in-app modules from the exported UI; do not reduce them to generic cards.",
    "For each major module, implement purpose, default/loading/empty/error/success states, and responsive behavior.",
    "Keep app modules separate from OS home-screen widgets in the production component model."
  ],
  "osWidgets": [
    "If the export includes home-screen, lock-screen, Live Activity, tablet glance, or Android widget surfaces, implement them as platform quick-access surfaces outside the app UI.",
    "If none are present, do not invent OS widgets unless the product requirements request them."
  ],
  "landingPage": {
    "detection": "Inspect files and screen names for a marketing/landing page surface. If present, keep it separate from product app screens.",
    "requiredSections": [
      "hero",
      "value props",
      "product proof/screenshots",
      "feature proof",
      "CTA"
    ]
  },
  "tokens": {
    "source": [
      "index.html"
    ],
    "required": [
      "background",
      "surface",
      "foreground",
      "muted text",
      "border",
      "accent",
      "radius",
      "shadow",
      "spacing",
      "type scale",
      "motion"
    ],
    "note": "Extract/freeze tokens before framework implementation so coding tools do not substitute default theme colors or typography."
  },
  "interactions": {
    "source": [
      "index.html"
    ],
    "requiredStates": [
      "default",
      "hover",
      "focus",
      "active",
      "disabled",
      "loading",
      "empty",
      "error",
      "success"
    ],
    "requiredBehaviors": [
      "forms/validation where present",
      "tabs/filters where present",
      "dialogs/sheets/drawers where present",
      "copy/generate/share actions where present",
      "player or quick controls where present"
    ],
    "note": "If the prototype is static, derive missing behavior from visible controls and document it before coding."
  },
  "responsiveViewports": [
    {
      "name": "mobile-compact",
      "width": 360,
      "height": 800,
      "category": "mobile",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "mobile-standard",
      "width": 390,
      "height": 844,
      "category": "mobile",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "mobile-large",
      "width": 430,
      "height": 932,
      "category": "mobile",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "foldable-small-tablet",
      "width": 600,
      "height": 960,
      "category": "foldable-tablet",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "tablet-portrait",
      "width": 820,
      "height": 1180,
      "category": "tablet",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "tablet-landscape",
      "width": 1024,
      "height": 768,
      "category": "tablet",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "laptop",
      "width": 1366,
      "height": 768,
      "category": "desktop",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "desktop",
      "width": 1440,
      "height": 900,
      "category": "desktop",
      "mustAvoidHorizontalScroll": true
    },
    {
      "name": "wide",
      "width": 1920,
      "height": 1080,
      "category": "wide",
      "mustAvoidHorizontalScroll": true
    }
  ],
  "implementationChecklist": [
    "Open entryFile first and map screens, modules, tokens, and interactions.",
    "Extract tokens before writing framework components.",
    "Implement app-specific modules with real states instead of generic card grids.",
    "Preserve or rebuild JS interactions for meaningful UX actions.",
    "Validate screenshots at desktop/tablet/mobile viewports with no horizontal overflow.",
    "Keep landing pages, in-app modules, and OS widgets as separate implementation surfaces."
  ]
}
````


