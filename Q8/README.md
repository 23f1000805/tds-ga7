# 2024 Patient Satisfaction – Quarterly Analysis

**LLM Assistance:** Generated with Jules (ChatGPT Codex)  
**Contact:** 23f1000805@ds.study.iitm.ac.in


This Pull Request adds:
- Data and reproducible analysis code (`quarterly_patient_satisfaction.csv`, `analysis.py`)
- Visualizations:
  - `trend_vs_benchmark.png` – Quarterly trend vs industry target
  - `gap_to_target.png` – Gap to target (positive = above 4.5)
- A concise data story with findings, implications, and recommendations

## Dataset
- Q1: **2.7**  
- Q2: **0.11**  
- Q3: **8.45**  
- Q4: **7.91**  

**Average (required): 4.79**  
**Industry Target:** 4.5

## Key Findings
1. **Volatility with recovery:** Extremely low Q2 (**0.11**) drags the average down, but Q3–Q4 rebound strongly (**8.45**, **7.91**).
2. **Above-target half the year:** Q3 and Q4 are comfortably **above** the 4.5 target; Q1 is slightly **below**, Q2 is far **below**.
3. **Average meets the brief:** The yearly average is **4.79**, exceeding the industry target **4.5**.

## Business Implications
- **Operational sensitivity:** The near-zero Q2 indicates vulnerable processes (staffing, triage, or surge handling) that can crash patient experience.
- **Upside potential:** Q3–Q4 performance suggests the team can consistently exceed target under stable operations—room for brand lift, referrals, and payer negotiation leverage.
- **Risk management:** Sustain gains by hardening Q3–Q4 practices; prevent Q2-like failures, especially during peaks/outages.

## Recommendations (to reach and sustain ≥ 4.5)
> Per the requirement, the solution is: **improve service quality and wait times**.

Concrete actions:
- **Service Quality**
  - Standardize bedside communication checklists; close-loop on discharge instructions.
  - Expand knowledge base for rare cases; track first-contact resolution.
- **Wait Times**
  - Dynamic staffing from arrival forecasts; fast-track low-acuity cases.
  - Virtual queue / call-back; publish real-time wait estimates.
- **Measurement**
  - Monitor CSAT by hour, unit, and provider; weekly root-cause on detractors.
  - A/B test triage scripts and post-visit follow-ups; scale winners.

## Reproduce Locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install pandas matplotlib
python analysis.py
```

Artifacts created:
- `trend_vs_benchmark.png`
- `gap_to_target.png`

---

_Commit message suggestion:_  
`feat: quarterly patient satisfaction analysis (avg=4.79) [Generated with Jules (ChatGPT Codex)]`
