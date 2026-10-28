# UAT and Evaluation Plan

## Business validation
- Reviewer can understand the finding.
- Supporting evidence is visible.
- Severity and confidence are understandable.
- Reviewer can record a decision and rationale.
- High-risk findings are easy to identify and escalate.

## AI evaluation
A production implementation should define a labeled evaluation set and agreed thresholds for:
- precision / false positives,
- recall / missed issues,
- evidence grounding,
- reviewer override rate,
- review time,
- escalation rate,
- inter-reviewer agreement.

## Negative tests
- Unsupported finding with high confidence
- Correct evidence attached to the wrong finding
- Missing evidence
- Sensitive data exposed in output
- Low-confidence high-severity finding
- Duplicate findings
- Attempted approval without required rationale

## Example release criteria
- No unresolved critical defects
- Business UAT completed
- Security/privacy requirements completed
- Human oversight tested
- Monitoring metrics defined
- Audit fields available
