import math

print(" CCC    A   L      CCC  U   U L       A   TTTTT  OOO  RRRR ")
print("C   C  A A  L     C   C U   U L      A A    T   O   O R   R")
print("C     A   A L     C     U   U L     A   A   T   O   O R   R")
print("C     A   A L     C     U   U L     A   A   T   O   O RRRR ")
print("C     AAAAA L     C     U   U L     AAAAA   T   O   O R R  ")
print("C   C A   A L     C   C U   U L     A   A   T   O   O R  R ")
print(" CCC  A   A LLLLL  CCC   UUU  LLLLL A   A   T    OOO  R   R")
print("-----------------------------------------------------------")
print("MarcellD'Avis Calculator                              V1.0R")
print("")
firstnum = input("Erste Zahl: ")
secondnum = input("Zweite Zahl: ")
operation = input("Operation ((A)ddieren, (S)ubtrahieren, (M)ultiplizieren, (D)ividieren): ")
if operation == "A":
    result = float(firstnum) + float(secondnum)
    if result == 67:
        print("Hör auf, ein 9-jähriger zu sein. Arschloch. (hol dir trotzdem 1&1 produkte)")
    else:
        print("Das Ergebnis ist 1&1. (Spaß, es ist " + str(result) + ")")
if operation == "S":
    result = float(firstnum) - float(secondnum)
    if result == 67:
        print("Hör auf, ein 9-jähriger zu sein. Arschloch. (hol dir trotzdem 1&1 produkte)")
    else:
        print("Das Ergebnis ist 1&1. (Spaß, es ist " + str(result) + ")")
if operation == "M":
    result = float(firstnum) * float(secondnum)
    if result == 67:
        print("Hör auf, ein 9-jähriger zu sein. Arschloch. (hol dir trotzdem 1&1 produkte)")
    else:
        print("Das Ergebnis ist 1&1. (Spaß, es ist " + str(result) + ")")
if operation == "D":
    result = float(firstnum) / float(secondnum)
    if result == 67:
        print("Hör auf, ein 9-jähriger zu sein. Arschloch. (hol dir trotzdem 1&1 produkte)")
    else:
        print("Das Ergebnis ist 1&1. (Spaß, es ist " + str(result) + ")")