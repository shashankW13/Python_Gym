travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

for country, city in travel_log.items():
    travel_log[country] = {'cities_visited': city}

print(travel_log[1])