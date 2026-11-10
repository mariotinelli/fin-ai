# Technical inspection

## Follow effective behavior

Inspect only paths relevant to task decisions and criteria. Identify implementation, configuration, bootstrapping, providers/plugins and installed versions that can affect the result. Missing application configuration does not prove a dependency supplies none.

Trace the path to the observable effect. Check overrides and relevant differences between production, development and tests. Cite file and symbol, or command and sanitized result, for claims supporting current state, architecture and risks. Distinguish code reading from executed verification; never expose credentials or dump sensitive configuration.

For a relevant external dependency, check success, failure and unavailability in installed code or compatible documentation. Describe the actual outcome; if it conflicts with the requirement, present the necessary decision and impact. Do not invent fallback behavior or policy changes to finish the plan. Record what cannot be confirmed as uncertainty.

**Complete when:** each decisive claim has a traceable source, relevant environment conditions are explicit, and no hypothesis is presented as confirmed behavior.

## Inspect applicable visual evidence

For an interface delivery, inspect the declared design and current rendered UI or explain access limits. Identify applicable screens/states, approved field/action adaptations, supplied assets/tokens and the actual differences from existing components. Reuse behavior and implementation where suitable while adapting appearance to the primary visual source. A supplied CSS value is evidence; a hidden breakpoint guessed from a screenshot is not. New user-visible differences need requirement alignment, while component/CSS mechanisms remain implementation decisions.

Identify how development and read-only validation can compare the rendered result with the reference, including environment prerequisites, relevant viewport/state and accessible evidence. Use existing project/browser tools; do not prescribe a new dependency merely to compare appearance. Backend-only phases can defer visual verification to their identified UI consumer phase.

**Complete when:** applicable visual sources, current differences, authorized adaptations and a feasible comparison method are explicit, or the specific missing evidence/product decision blocks readiness.

## Check solution reach

Before proposing a default, global configuration or shared-component change, locate consumers and compare affected behavior with approved scope, including environment differences. Record relevant consumers and supporting evidence in architecture or risks.

If a proposal changes out-of-scope behavior, prefer a localized application preserving necessary sharing. If broader reach is required, present impact and the pending product decision before declaring architecture ready. Declaring a flow out of scope does not neutralize changes to it; adapting its fixtures does not demonstrate functional preservation either. A shared change is valid when its effects are authorized or inspection supports preservation of other consumers.

**Complete when:** the solution's actual reach matches task boundaries, and external effects are preserved with evidence or await an explicit decision.

## Discover verifiers and prerequisites

Expand aggregate scripts until relevant verifiers, options and configuration are identified. Include formatting, static analysis, refactoring in check mode, types, tests and coverage where present; do not impose another stack's tools. Consult relevant CI without claiming unverified equivalence.

Check required runtime, package managers and coverage support. Distinguish commands that only check from commands that fix files. Identify a reproducible execution path in the project and Ralph environments; do not reduce requirements or install dependencies to bypass a blocked baseline.

**Complete when:** the complete command, its composition and prerequisites are known, and its effects allow initial observation without modifying tracked files.
