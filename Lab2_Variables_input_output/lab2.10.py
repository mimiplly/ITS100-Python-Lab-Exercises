#ITS100 Lecture2 Variables Input Output Lab2.10
print(">>>======= REstART =======")
print(">>>")
ITS = input("enter grade from ITS100: ")
EL = input("enter grade from EL171: ")
SCS = input("enter grade from SCS183: ")
ITS, EL, SCS = float(ITS), float(EL), float(SCS)
GPA = (ITS + EL + SCS) / 3
print("Your GPA is %.2f" % GPA)