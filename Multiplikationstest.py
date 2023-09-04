import random

print("Välkommen till multiplikationstestet!")

def main():
    poang = 0
    val = int(input("Hur många frågor vill du svara på? "))
    s_grad = int(input("Välj svårighetsgrad:\n1: Lätt\n2: Medelsvår\n3: Svår"))
    if s_grad == 1:
        for runda in range(val):
            n1 = random.randrange(1, 11)
            n2 = random.randrange(1, 11)
            print("Vad är", n1, "gånger", n2, "?")
            svar = int(input())
            resultat = mult_maskin(svar, n1, n2)
            if resultat == 1:
                poang += 1
    if s_grad == 2:
        for runda in range(val):
            n1 = random.randrange(3, 13)
            n2 = random.randrange(3, 13)
            print("Vad är", n1, "gånger", n2, "?")
            svar = int(input())
            resultat = mult_maskin(svar, n1, n2)
            if resultat == 1:
                poang += 1
    if s_grad == 3:
        for runda in range(val):
            n1 = random.randrange(3, 21)
            n2 = random.randrange(3, 21)
            print("Vad är", n1, "gånger", n2, "?")
            svar = int(input())
            resultat = mult_maskin(svar, n1, n2)
            if resultat == 1:
                poang += 1
    Resultat(poang, val)
def mult_maskin(svar, n1, n2):
    ratt_svar = 1
    if svar == n1 * n2:
        print("Rätt svar!")
        return ratt_svar
    else:
        print("Du svarade fel, rätt svar är ", n1 * n2)

def Resultat(poang_antal, val):
    procent = poang_antal / val * 100
    if procent >= 90:
        vitsord = "Utmärkt"
    elif procent < 90 and procent >= 70:
        vitsord = "Bra"
    elif procent < 70 and procent >= 50:
        vitsord = "Ok"
    elif procent < 50 and procent >= 0:
        vitsord = "Du måste öva mera!"
    print()
    print("Du svarade rätt på", poang_antal, "utav", val, "frågor")
    print("Det ger dig vitsordet: ", vitsord)

main()