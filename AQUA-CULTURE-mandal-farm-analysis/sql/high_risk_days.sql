

-- high risk days

 SELECT Date, Pond_ID, Water_Temp_C,
               Dissolved_Oxygen_mgL, Ammonia_ppm,
               Mortality_Count
        FROM farm_data
        WHERE Dissolved_Oxygen_mgL < 4.0
           OR Ammonia_ppm > 0.5
           OR Water_Temp_C > 32
        ORDER BY Date DESC;
        
        