# coding=utf8
import random
def casino():
    secret = random.randint(0,100)
    while True:
        print("Tippe eine Zahl: ")
        guess = int(raw_input())
        if secret==guess:
            print "Korrekt getippt"
            secret = random.randint(0, 100)
        else:
            print "Falsch getippt"
            if guess > secret:
                print("Die getippte Nummer ist zu groß.")
            elif guess < secret:
                print("Die getippte Nummer ist zu klein.")
        decision = raw_input("Möchtest du weitermachen? Ja / Nein ").lower()
        if decision == 'ja':
            print("...")
        elif decision == 'nein':
            print("Einen schönen Tag dir!")
            break
        else:
            print("Eingabewert " + decision + " kann nicht verarbeitet werden.")
            print("Programm wird abgebrochen.")
            break

def main():
    casino()

if __name__ == '__main__':
    main()