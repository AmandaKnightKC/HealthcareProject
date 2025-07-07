SHOW TABLES;
DESCRIBE 2022_oep_state_level_public_use_file;
CREATE VIEW state_enrollment_summary_2022 AS
SELECT State_Abrvtn AS state,
    Pltfrm AS platform,
    Cnsmr AS total_enrollees,
    New_Cnsmr AS new_enrollees,
    Tot_Renrl AS returning_enrollees,
    Avg_Prm AS avg_premium_before_APTC,
    Avg_Prm_Aftr_APTC AS avg_premium_after_APTC,
    APTC_Cnsmr AS consumers_with_APTC,
    APTC_Cnsmr_Avg_APTC AS avg_APTC_amount,
    APTC_Cnsmr_Avg_Prm_Aftr_APTC AS avg_net_premium_with_APTC,
    FPL_100_150,
    FPL_150_200,
    FPL_200_250,
    FPL_250_300,
    FPL_300_400,
    FPL_400_500,
    FPL_GT500
FROM 2022_oep_state_level_public_use_file;
SELECT *
FROM state_enrollment_summary_2022
ORDER BY total_enrollees DESC;