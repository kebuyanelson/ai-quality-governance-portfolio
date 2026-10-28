# AI Quality & Governance Portfolio

A portfolio project demonstrating how enterprise AI initiatives can move from **business requirements and AI-generated outputs** into **human review, measurable outcomes, governance controls, release readiness, and ongoing monitoring**.

This repository is designed to show product, delivery, and governance thinking rather than to present a production AI model.

## What this repository demonstrates

- AI product/workflow design
- Human-in-the-loop review
- Risk-based AI governance
- Use-case intake and lifecycle controls
- AI governance KPIs
- Post-deployment monitoring concepts
- UAT and release-readiness thinking
- Executive and business-value framing
- Responsible AI controls for ML, GenAI, and agentic systems

## Live prototype

The Streamlit app includes five views:

1. **Quality Review** — review AI-generated findings with evidence, severity, confidence, and human disposition.
2. **AI Portfolio** — view use cases across risk tier, status, controls, and monitoring.
3. **Governance KPIs** — see business, technical, operational, and maturity metrics.
4. **Risk Taxonomy** — review core AI risk categories and example controls.
5. **About** — explains the purpose and limitations of the portfolio.

## Product scenario

A Quality team uses AI to identify possible issues in business documentation. The AI does **not** make the final decision.

A reviewer needs to:
- understand what the AI found,
- inspect supporting evidence,
- assess confidence and severity,
- accept, reject, or request more evidence,
- document rationale,
- escalate higher-risk items,
- support release-readiness decisions,
- and generate data that can be used to improve the system over time.

## AI lifecycle represented

```text
Intake
  ↓
Risk classification
  ↓
Data & control review
  ↓
Evaluation
  ↓
Human oversight
  ↓
Approval
  ↓
Deployment
  ↓
Monitoring
  ↓
Recertification / material-change review
```

## Repository structure

```text
.
├── app.py
├── data/
│   ├── sample_findings.csv
│   └── sample_use_cases.csv
├── docs/
│   ├── product_requirements.md
│   ├── ai-risk-taxonomy.md
│   ├── governance-kpis.md
│   ├── uat-and-evaluation.md
│   └── architecture-and-controls.md
├── case-studies/
│   ├── financial-services-ml-fraud.md
│   └── enterprise-ai-platform-governance.md
├── requirements.txt
└── README.md
```

## Run locally

```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

## Portfolio-safe design

All data in this repository is synthetic.

The case studies are intentionally generalized and sanitized. They describe patterns and responsibilities from prior experience without publishing client data, employer-confidential materials, internal source code, proprietary model assets, or confidential implementation details.

## Author

Kebuya Nelson Rohwoh  
AI Strategy, Governance & Delivery
