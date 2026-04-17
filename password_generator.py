import secrets
import string

#caratteri disponibili : maiuscole,minuscole,numeri,punteggiatura
#password da 12 car, tutti i tipi di car almeno una volta
#se tutti i set sono False o se lenght è minore del numero di set abilitati = ValueError


def generate_password(
    length: int = 12,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
) -> str:
    password=""
    lun = 0
    upper = secrets.choice(string.ascii_uppercase) if use_upper == True else ""
    lun +=1 if use_upper == True else lun
    lower = secrets.choice(string.ascii_lowercase)
    digits = secrets.choice(string.digits)
    symbols = secrets.choice(string.punctuation)
    for i in range(length) :
        pass









def build_alphabet(length, use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous) :
    use_upper = True if use_upper.lower() == "y" or "" else False
    use_lower = True if use_lower.lower() == "y" or "" else False
    use_digits = True if use_digits.lower() == "y" or "" else False
    use_symbols = True if use_symbols.lower() == "y" or "" else False
    avoid_ambiguous = True if avoid_ambiguous.lower() == "y" else False
    return length, use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous





def __main__():
    print("""\n\n$ python password_generator.py
=== Password generator ===
1) Profilo default (12 caratteri, tutti i set, visualizza a schermo)
2) Profilo custom\n""")
    scelta=input("Scelta : ")
    if scelta=="1":
        generate_password()
    elif scelta=="2":
        # qua lasciamo scelta all'utente su quali caratteri usare
        length = int(input("Lunghezza password : "))
        use_upper = input("Maiuscole Y/n : ")
        use_lower = input("Minuscole Y/n : ")
        use_digits = input("Numeri Y/n : ")
        use_symbols = input("Simboli Y/n : ")
        avoid_ambiguous = input("Caratteri ambigui y/N : ")
        build_alphabet(use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous)
    else:
        print("Scelta non valida")


if __name__ == "__main__":
    __main__()
