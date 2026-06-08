while True:
    print("1=Addition")
    print("2=Subtraktion")

    val = input("Välj 1 för addition eller 2 för subtraktion: ")
    tal1 = int(input("Skriv det första talet: "))
    tal2 = int(input("Skriv det andra talet: "))

    if val == "1":
        print("Resultat:", tal1 + tal2)
    elif val == "2":
        print("Resultat:", tal1 - tal2)
    else:
        print("Ogiltigt val. Välj 1 eller 2.")

    again = input("Vill du köra igen? (j/n): ").strip().lower()
    if again != "j" and again != "ja":
        print("Avslutar kalkylatorn.")
        break
    
    