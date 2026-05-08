
--  mortality trend month

 select Pond_ID,
		monthname(Date) as months,
        sum(Mortality_Count) as mortality
 from farm_data
 
 group by months , Pond_ID
 order by mortality desc;