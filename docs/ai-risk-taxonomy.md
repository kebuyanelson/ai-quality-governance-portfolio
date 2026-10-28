# AI Risk Taxonomy

This taxonomy provides a consistent way to evaluate AI use cases from intake through monitoring.

## Core categories

### Privacy & data protection
Risks: exposure, misuse, or unauthorized use of personal/sensitive data.  
Controls: data minimization, privacy review, access controls, retention rules.

### Fairness & bias
Risks: discriminatory or materially inconsistent outcomes.  
Controls: bias testing, scenario testing, subgroup monitoring.

### Transparency & explainability
Risks: inability to understand, justify, or communicate AI outcomes.  
Controls: documentation, explainability methods, user disclosures.

### Security
Risks: unauthorized access, prompt injection, model abuse, system compromise.  
Controls: RBAC, encryption, secure development, monitoring, red-team testing.

### Reliability & safety
Risks: hallucinations, model drift, unstable performance, unsafe outputs.  
Controls: evaluation thresholds, guardrails, human oversight, monitoring.

### Operational & third-party
Risks: vendor changes, outages, weak monitoring, unclear accountability.  
Controls: inventory, vendor assessment, change management, incident processes.

## GenAI-specific considerations
- Hallucinations and unsupported outputs
- Prompt injection and jailbreaks
- Sensitive data leakage
- Retrieval/grounding quality
- User over-reliance
- Model/vendor version changes

## Lifecycle operationalization
1. Intake
2. Risk tiering
3. Design and validation
4. Approval / go-live readiness
5. Monitoring
6. Material-change reassessment

## Audit evidence examples
- Risk assessment
- AI inventory record
- Test and validation evidence
- Model/system documentation
- Monitoring dashboard
- Incident and remediation log
