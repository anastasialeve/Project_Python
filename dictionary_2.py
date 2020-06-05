population = {
    'Berlin': 3748148,
    'Hamburg': 1822445,
    'München': 1471508,
    'Cologne': 1085664,
    'Frankfurt': 753056,
}

b = population.get("Berlin")
print("Berlin", b)

# update einfügen

population.update({"Berlin" : 20000000, "Dortmund": 50000})

# k ist key, v ist value
for k, v in population.items():
    print(k, v)

pairs = population.items()
print(pairs)

deutschland = {
    "berlin": {
        "neukölln": 3,
        "kreuzberg": 4
    }
}
print(deutschland)
deutschland["berlin"].update({"kreuzberg": 14})
print(deutschland)

# eintrag löschen , pop holt der Wert und löscht den Eintrag
berlin = population.pop("Berlin")
print("berlin", berlin)

del population ["Dortmund"]
population["Frankfurt"] = 0
print(population)

