
travel_log = [
    {"Country": "America",
     "Visited": ["Chicago", "New York", "LA"],
     "total_visit": 0,
     },
    {"Country": "Indonesia",
     "Visited": ["Jakarta", "Bogor", "Depok"],
     "total_visit": 10,
     },
]


def add_new_country(country, city, visited):
    add = {"Country": country, "Visited": city, "total_visit": visited}
    travel_log.append(add)



add_new_country ("Russia", ["Moscow", "Saint_Petersburg", "Samara"], 2)

print(travel_log)