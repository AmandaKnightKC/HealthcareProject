# Healthcare Marketplace Enrollment Analysis (2020–2022)

This project looks at how enrollment in ACA Marketplace plans changed over time, with a focus on the period after the American Rescue Plan Act (ARPA) was introduced in 2021. The goal is to understand how subsidies and plan selection shifted in the years following the policy change.

---

## Note on Time Period

This analysis focuses on Marketplace enrollment and affordability trends from 2020 to 2022 — a period significantly influenced by the COVID-19 pandemic and temporary policy changes under the American Rescue Plan Act (ARPA). As such, the patterns observed (e.g., spikes in enrollment, expanded subsidies, shifts in plan choices) reflect behavior during an emergency policy environment. This project does not attempt to generalize these trends beyond this window, but rather examines how key Marketplace metrics responded to extraordinary economic and policy conditions.

---

## Data Sources

Data is pulled from the CMS Marketplace Open Enrollment Period Public Use Files (PUFs):

- State-Level Enrollment (2020–2022)
- Metal-Level Enrollment
- Rate and Plan Attributes (Marketplace General PUFs)

Reference PDFs and dictionaries are stored locally in `/docs`.

---

## Key Questions

- How did total enrollment change from 2020 to 2022?
- What impact did ARPA have on subsidy levels and premium affordability?
- Did certain metal levels (e.g., Silver) see more growth than others?
- Are there noticeable trends by state?

---

## Tools

- SQL (MySQL)
- Python (Pandas, data loading)
- Tableau (planned visuals)
- Git / GitHub

---

## Structure

```
HealthcareProject/
├── scripts/ # Python and SQL code
├── data/ # Raw CSVs (gitignored)
├── notebooks/ # Exploratory work
├── docs/ # Reference PDFs
├── notes.md # Planning notes
├── queries.md # SQL tracking
└── .gitignore
```

---

## Status

This is a work in progress. Data is mostly cleaned, and I’m currently exploring trends in enrollment and subsidy levels. Final visualizations and takeaways are coming soon.

---

## Source

All data from CMS:  
[https://www.cms.gov/marketplace/resources/data/public-use-files](https://www.cms.gov/marketplace/resources/data/public-use-files)

---

## Contact

Amanda Knight  
🌐 [amandaknightkc.github.io](https://amandaknightkc.github.io)  
📬 Contact via GitHub profile or portfolio
