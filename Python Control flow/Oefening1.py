getal1 = int(input("Geef een getal 1."))
getal2 = int(input("Geef een getal 2."))

print(f"Is waarde 1 groter dan waarde 2? {"Ja" if getal1 > getal2 else "Nee"}")

print(f"Is waarde 1 kleiner dan waarde 2? {"Ja" if getal1 < getal2 else "Nee"}")

print(f"Is waarde 1 gelijk aan waarde 2? {"Ja" if getal1 == getal2 else "Nee"}")

print(f"Is waarde 1 groter dan waarde 2 en groter dan 10? {"Ja" if getal1 > getal2 and getal1 > 10 else "Nee"}")

print(f"Is waarde 2 groter dan 5 en waarde 1 kleiner dan 2? {"Ja" if getal2 > 5 and getal1 > 2 else "Nee"}")

print(f"Is waarde 1 kleiner dan 10 en niet groter dan 5? {"Ja" if getal1 < 10 and not getal1 > 5 else "Nee"}")
