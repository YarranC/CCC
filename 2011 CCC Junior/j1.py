# Which Alien?

a = int(input("How many antennas?\n"))
e = int(input("How many eyes?\n"))

if a >= 3 and e <= 4:
    print("TroyMartian")
if a <= 6 and e >= 2:
    print("VladSaturnian")
if a <= 2 and e <= 3:
    print("GraemeMercurian")
