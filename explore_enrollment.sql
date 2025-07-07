SHOW TABLES;
DESCRIBE table_name;
-- top 10 states by consumer count
SELECT State_Abrvtn,
    SUM(Cnsmr) AS Total_Consumers
FROM 2020_oep_state_level_public_use_file
GROUP BY State_Abrvtn
ORDER BY Total_Consumers DESC
LIMIT 10;
-- percent eligible for financial assistance
-- Aplctn_Sbmtd = Number of applications submitted
-- This refers to total application forms submitted, regardless of how many people were included on the form.
-- Indvdl_Aplctn_Sbmtd = Number of individuals included on submitted applications
-- This counts each person listed across all applications. An application could represent 1 person (a single applicant) or a family with multiple individuals.
SELECT State_Abrvtn,
    Sum(FA_Elgbl) / SUM(indvdl_aplctn_sbmtd) * 100 AS Percent_Eligible_for_Financial_Assistance
FROM 2020_oep_state_level_public_use_file
GROUP BY State_Abrvtn
ORDER BY Percent_Eligible_for_Financial_Assistance DESC
LIMIT 10;
SELECT State_Abrvtn,
    SUM(FA_Elgbl) AS Eligible,
    SUM(Indvdl_Aplctn_Sbmtd) AS Applicants
FROM 2020_oep_state_level_public_use_file
GROUP BY State_Abrvtn
ORDER BY Applicants ASC;