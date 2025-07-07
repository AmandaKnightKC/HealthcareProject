# 🩺 Healthcare Data Analysis Notes

**Project Source**: Centers for Medicare & Medicaid Services  
**Primary Datasets**:  

- Marketplace Open Enrollment Period PUFs <https://www.cms.gov/data-research/statistics-trends-and-reports/marketplace-products>
  - FOCUS: Who enrolled, in what plans, and how much they paid during the annual open enrollment window.
  - enrollment-level data
  - Includes subsidy info (average advance premium tax credit- APTC)
  - Can be segmented by state, county, zip, metal tier
  - best for trend analysis over years (ARPA impact)
  - Comparing plan updates across geographies
  - analyzing affordability and subsidy effect

- Marketplace General Public Use Files (PUFs)
 <https://www.cms.gov/marketplace/resources/data/public-use-files>

  - FOCUS: Details about the plans themselves — what they cover, how much they cost, who offers them, and where.
  - Plan-level structure and pricing
  - not tied to enrollment volumes
  - Data includes: Premiums by age and family type, Deductibles and copays, Benefits offered, Carrier and service area
  - Example datasets:
    - Rate PUF – Premiums by plan ID, age, and region
    - Plan Attributes PUF – Cost-sharing and coverage features
    - Service Area PUF – Where insurers offer plans
  - Best for:
    - Comparing plan designs and pricing
    - Analyzing insurer participation and competitiveness
    - Evaluating benefit richness vs. cost

Benefits PUF – Services covered (e.g., mental health, maternity)

- Plan Attributes PUFs: 2020, 2021, 2022
- OEP State-Level PUFs: 2020, 2021, 2022
- OEP County-Level PUFs: 2020, 2021, 2022

## 2020–2022 OEP PUFs

---

## 🎯 Project Focus

Using CMS data to analyze:

- Health insurance **enrollment patterns across states**
- **Premium costs** and plan tiers (Bronze, Silver, Gold, Platinum)
- The impact of **subsidies** on affordability
- **Differences in plan structure** and cost-sharing over time

This project supports a healthcare data analyst job application by showcasing SQL, aggregation, segmentation, and policy impact analysis.

---

## 📊 Key Datasets

### 🟦 Marketplace Open Enrollment PUFs

- **State-Level PUF**: Enrollment totals, plan selections, subsidies by state
- **County/ZIP/Metal Level PUFs**: More granular breakdowns
- **Use Case**: Trends in health plan adoption, enrollment per capita, and subsidy effects

### 🟨 Marketplace General PUFs

- **Rate PUF**: Premium pricing by age, plan, insurer
- **Plan Attributes PUF**: Deductibles, copays, network design
- **Benefits PUF**: Service-level details (e.g., mental health, maternity)
- **Use Case**: Cost structure analysis, coverage quality, insurer comparison

---

**Goal**: Assess the effect of the American Rescue Plan Act (ARPA) on insurance enrollment behavior and affordability.

### Key Comparisons

- **Total enrollment**: Pre-ARPA (e.g., 2020) vs Post-ARPA (2021–2024)
- **Average premiums and subsidies**: Before and after ARPA’s enhanced subsidies
- **Metal tier selection shifts**: Are more consumers choosing Silver/Gold due to affordability improvements?
- **State-level disparities**: Which states saw the largest enrollment increases post-ARPA?

### Suggested Metrics

- % change in enrollment (2020 → 2021–2024)
- Avg monthly premium before vs after
- % of enrollees receiving subsidies (and average subsidy amount)
- Uptake of Silver plans before and after ARPA

### Potential Data Joins

- `State-Level PUF` with `Rate PUF` and `Metal Level PUF` by year and plan ID
