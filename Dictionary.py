en_de = {
    "house" : "Haus",
    "cat":"Katze",
    "black":"schwarz"
}
print(en_de)

# auf dictionary zugreifen per Schlüssel
print(en_de["house"])

# Fehler Schlüssel existiert nicht
# print(en_de["dog"])

if "dog" in en_de:
    print("der Schlüssel Dog ist im Dict enthalten")

person = {
    "name": {
        "first_name": "Benno",
        "last_name": "Müller",
    },
    "hobbies": {
        "Skifahren",
        "Mathe",
        "Mathe",
    },
    "age": 23,
}
print(person)
print(person.get("name", None).get("first_name", None))

print(person["name"]["first_name"])

print(person["name"]["first_name"])

# ============================================================================
import morsecode
x = morsecode.morse("Hallo")
print(x)


