temp = int(input("Geef de temperatuur in."))

if temp < 10:
    print("koud")
elif temp > 9 and temp < 11:
    print("nice")
elif temp > 19 and temp < 31:
    print("'t word warm")
elif temp > 30:
    print("zeer warm")