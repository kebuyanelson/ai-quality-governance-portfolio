import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="AI Quality & Governance Portfolio", layout="wide")

BASE = Path(__file__).parent
findings = pd.read_csv(BASE / "data" / "sample_findings.csv")
use_cases = pd.read_csv(BASE / "data" / "sample_use_cases.csv")

st.title("AI Quality & Governance Portfolio")
st.caption(
    "A portfolio prototype demonstrating AI product delivery, human-in-the-loop review, "
    "risk-based governance, operational KPIs, and post-deployment oversight."
)

page = st.sidebar.radio(
    "Explore",
    ["Quality Review", "AI Portfolio", "Governance KPIs", "Risk Taxonomy", "About"]
)

if page == "Quality Review":
    st.subheader("Human-in-the-loop Quality Review")
    severity = st.multiselect(
        "Severity",
        options=sorted(findings["severity"].unique()),
        default=sorted(findings["severity"].unique())
    )
    min_conf = st.slider("Minimum AI confidence", 0.0, 1.0, 0.0, 0.05)
    df = findings[findings["severity"].isin(severity) & (findings["confidence"] >= min_conf)].copy()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Findings", len(df))
    c2.metric("High/Critical", int(df["severity"].isin(["High", "Critical"]).sum()))
    c3.metric("Avg confidence", f"{df['confidence'].mean():.0%}" if len(df) else "0%")
    c4.metric("Pending review", int((df["review_status"] == "Pending").sum()))

    for _, row in df.iterrows():
        with st.expander(f"{row['finding_id']} · {row['severity']} · {row['finding_type']}"):
            a, b = st.columns([2, 1])
            with a:
                st.markdown(f"**Item:** {row['item_name']}")
                st.markdown(f"**AI finding:** {row['finding_summary']}")
                st.markdown(f"**Evidence:** {row['evidence_reference']}")
                st.markdown(f"**Recommendation:** {row['recommendation']}")
            with b:
                st.markdown(f"**Confidence:** {row['confidence']:.0%}")
                st.markdown(f"**Risk flag:** {row['risk_flag']}")
                st.selectbox(
                    "Human decision",
                    ["Pending", "Accept", "Reject", "Needs more evidence"],
                    key=f"d_{row['finding_id']}"
                )
                st.text_area("Reviewer rationale", key=f"n_{row['finding_id']}")
                st.caption("Prototype only: decisions are not persisted.")

elif page == "AI Portfolio":
    st.subheader("AI Use-Case Portfolio")
    st.dataframe(use_cases, use_container_width=True, hide_index=True)

    total = len(use_cases)
    approved = (use_cases["status"] == "Approved").sum()
    high_control = ((use_cases["risk_tier"] == "High") & (use_cases["controls_complete"] == "Yes")).sum()
    monitored = (use_cases["monitoring_status"] == "Active").sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Use cases", total)
    c2.metric("Approved", int(approved))
    c3.metric("High-risk with controls", int(high_control))
    c4.metric("Active monitoring", int(monitored))

    st.markdown("#### Example intake-to-monitoring lifecycle")
    st.markdown(
        "Intake → Risk classification → Data & control review → Evaluation → Human oversight "
        "→ Approval → Deployment → Monitoring → Recertification"
    )

elif page == "Governance KPIs":
    st.subheader("Governance KPI Framework")
    kpis = pd.DataFrame([
        ["Business", "Reviewed & approved use cases", "Measures whether AI activity enters the formal governance process."],
        ["Business", "Time to governance decision", "Measures whether governance is enabling delivery efficiently."],
        ["Business", "High-risk use cases with required controls", "Shows whether risk-based controls are implemented in practice."],
        ["Business", "Audit / regulatory issue rate", "Tracks repeated control gaps and governance effectiveness over time."],
        ["Technical", "Performance vs approved thresholds", "Checks whether systems remain within approved operating ranges."],
        ["Technical", "Drift rate", "Tracks data, concept, or model drift after deployment."],
        ["Technical", "Fairness stability", "Monitors subgroup performance where fairness is relevant."],
        ["Technical", "Groundedness / hallucination rate", "Measures unsupported or fabricated GenAI outputs."],
        ["Operational", "AI inventory completeness", "Measures visibility of the enterprise AI estate."],
        ["Operational", "Documentation completeness", "Tracks completeness of key governance evidence."],
        ["Operational", "Monitoring coverage", "Measures the percentage of AI systems under active monitoring."],
        ["Operational", "Recertification completion rate", "Tracks scheduled reviews and material-change reassessments."],
        ["Maturity", "Stakeholder governance sentiment", "Measures whether governance is clear, usable, trusted, and enabling."]
    ], columns=["Category", "KPI", "Why it matters"])
    st.dataframe(kpis, use_container_width=True, hide_index=True)

elif page == "Risk Taxonomy":
    st.subheader("AI Risk Taxonomy")
    risks = pd.DataFrame([
        ["Privacy & data protection", "Sensitive-data exposure, inappropriate data use", "Minimization, access controls, privacy review"],
        ["Fairness & bias", "Disparate or discriminatory outcomes", "Bias testing, scenario testing, subgroup monitoring"],
        ["Transparency & explainability", "Outputs cannot be understood or justified", "Documentation, explainability, disclosures"],
        ["Security", "Prompt injection, unauthorized access, model abuse", "RBAC, encryption, secure development, monitoring"],
        ["Reliability & safety", "Hallucinations, drift, unsafe outputs", "Guardrails, evaluation, red-team testing, monitoring"],
        ["Operational & third-party", "Vendor changes, outages, weak monitoring", "Inventory, vendor reviews, change management"]
    ], columns=["Risk category", "Example risk", "Example controls"])
    st.dataframe(risks, use_container_width=True, hide_index=True)

    st.markdown("#### GenAI-specific considerations")
    st.markdown(
        "- Prompt injection and jailbreak attempts\n"
        "- Sensitive-data leakage through prompts or retrieval\n"
        "- Retrieval quality and grounding\n"
        "- User over-reliance on model output\n"
        "- Vendor model/version changes"
    )

elif page == "About":
    st.subheader("About this portfolio")
    st.markdown("""
This repository is a **portfolio demonstration** of how I think about enterprise AI delivery and governance.

It is intentionally built with:
- synthetic data,
- no employer or client confidential information,
- no proprietary source code,
- no claims that this prototype is a production system.

The goal is to show how I connect:
**business requirements → AI workflow → risk controls → human oversight → evaluation → release readiness → monitoring → measurable value**.

The accompanying repository also includes two sanitized case studies:
1. Financial-services ML fraud detection with human oversight and post-deployment monitoring.
2. Enterprise R&D AI/ML platform governance with lifecycle controls and GenAI safeguards.
""")
