travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["paris", "lille", "dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stttgart"]
}, 
]

def add_new_country(country,visits,cities):
    travel_log.append({"country": country,"visits": visits,"cities": cities})

add_new_country("Russia",2,["moscow","saint petersburg"])
print(travel_log)