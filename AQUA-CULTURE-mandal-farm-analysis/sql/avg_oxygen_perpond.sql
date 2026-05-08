

-- avg_oxygen_perpond 

select Pond_ID ,
	round(avg(Dissolved_Oxygen_mgl),2) as average_oxygen,
    round(avg(Ammonia_ppm),2) as average_ammonia,
    sum(Mortality_Count) as total_mortality
    
    from farm_data
group by Pond_ID
Order by total_mortality desc;