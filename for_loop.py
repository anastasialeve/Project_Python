for value in ["Moskau", "Berlin", "Tokyo"]:
    print(value)
    print(type(value))
    print(id(value))

for buchstabe in "string":
    print(buchstabe)

print(30*"*")

 # break beändet die Aktion
name = "melone"
for buchstabe in name:
    if buchstabe =="l":
        break
    print(buchstabe)

print(30 * "*")

 # continue bedeutet, dass aws noch unten geschrieben wird nicht gemacht, sonst an diese stelle geht sie zum Anfang
name = "melone"
for buchstabe in name:
    if buchstabe =="l":
        continue
    print(buchstabe)