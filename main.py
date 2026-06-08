print("1=Addition")
print("2=Subtraktion")

val = input("Välj 1 för addition eller 2 för subtraktion: ")
tal1 = int(input("Skriv det första talet: "))
tal2 = int(input("Skriv det andra talet: "))

if val == "1":
    print("Resultat:", tal1 + tal2)
if val == "2":
    print("Resultat:", tal1 - tal2)

