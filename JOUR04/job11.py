def time_to_text(minutes):
    if minutes < 0:
        print("Le nombre de minutes ne peut pas être négatif.")
        return
    
    heures = minutes // 60
    reste_minutes = minutes % 60
    
    print(f"{heures} heures et {reste_minutes} minutes")


time_to_text(50)  
time_to_text(1500) 
time_to_text(1546)
time_to_text(150) 
