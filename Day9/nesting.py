# Nesting Dictionary

# Nesting list in dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting dictionary in dictionary
travel_log = {
    "France": {"cities_vistied": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_vistied": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

print(travel_log)

# Nesting dictionary in list
travel_log = {
    {
        "country": "France",
        "cities_vistied": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_vistied": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
