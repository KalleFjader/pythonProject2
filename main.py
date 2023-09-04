import random

print("STEN - SAX - PÅSE")

choice = ['sten', 'sax', 'påse']

def main():
    spelare = 0             # Variabeln börjar från noll
    dator = 0               # Variabeln börjar från noll
    rounds = int(input("Hur många poäng för att vinna? "))          # Här anges hur många poäng spelet ska spelas till.
    while spelare < rounds and dator < rounds:                      # Loopen håller på enda till endera datorn
        computer = random.choice(choice)                            # eller spelaren nått max poäng.
        user = int(input("Gör ditt val:\n1: sten\n2: sax\n3: påse\n"))
        resultat = checkResults(user, computer)                     # resultat" antar det returnerade värdet från
        if resultat == 1:                                           # checkResults-funktionen
            spelare = spelare + 1
        elif resultat == 2:
            dator = dator + 1
    Results(spelare, dator)

def checkResults(user, computer):
    userWin = 1
    computerWin = 2
    if user == 1 and computer == 'sten' or user == 2 and computer == 'sax' or user == 3 and computer == 'påse':
        print("Oavgjort")
    elif user == 1 and computer == 'sax' or user == 2 and computer == 'påse' or user == 3 and computer == 'sten':
        print("Du vann!")
        return userWin
    else:
        print("Datorn vann!")
        return computerWin

def Results(anvandare, system):             # Vår egen funktion som skriver ut resultatet.
    print("Resultatet")
    print(10 * "*")
    print("Användare:", anvandare)
    print("Dator:", system)

main()