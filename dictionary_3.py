gerichte = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
laender = ["Italien", "Deutschland", "Spanien", "USA"]

zippy = zip(laender, gerichte)
print(zippy)
for x in zippy:
    print("-", x)

#    oder, nur eim mal zip benutzen, sie können sich verbrauchen
#print(zippy.__next__())
#print(zippy.__next__())
#print(zippy.__next__())
#print(zippy.__next__())

zippy = zip(laender, gerichte)
d = dict(zippy)
print(d)
