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
    ambigui = "Il1O0" #da evitare se opzione attiva
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password +=(secrets.choice(string.ascii_uppercase)) if use_upper == True else ""
    password +=secrets.choice(string.ascii_lowercase)  if use_lower == True else ""
    password +=secrets.choice(string.digits)  if use_digits == True else ""
    password += secrets.choice(string.punctuation) if use_symbols == True else ""
    minimo = len(password) #cosi non sovrascriviamo i caratteri appena messi
    if avoid_ambiguous :
        for i in ambigui :
            pool = pool.replace(i,"") #rimpiazza i caratteri ambigui della pool con ""
    for i in range(length-minimo) :
        password +=secrets.choice(pool)
    return password



def build_alphabet(length, use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous) :
    use_upper = True if use_upper.lower() == "y" or use_upper == "" else False
    use_lower = True if use_lower.lower() == "y" or use_lower == "" else False
    use_digits = True if use_digits.lower() == "y" or use_digits == "" else False
    use_symbols = True if use_symbols.lower() == "y" or use_symbols == "" else False
    avoid_ambiguous = True if avoid_ambiguous.lower() == "y" else False
    return length, use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous



def __main__():
    print("""\n\n$ python password_generator.py
=== Password generator ===
1) Profilo default (12 caratteri, tutti i set, visualizza a schermo)
2) Profilo custom\n""")
    scelta=input("Scelta : ")
    if scelta=="1":
        print(f"Password : {generate_password()}")
    elif scelta=="2":
        # qua lasciamo scelta all'utente su quali caratteri usare
        length = int(input("Lunghezza password : "))
        use_upper = input("Maiuscole Y/n : ")
        use_lower = input("Minuscole Y/n : ")
        use_digits = input("Numeri Y/n : ")
        use_symbols = input("Simboli Y/n : ")
        avoid_ambiguous = input("Caratteri ambigui y/N : ")
        build_alphabet(length, use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous)
    else:
        print("Scelta non valida")
    print("\nPassword generata!\n")


if __name__ == "__main__":
    __main__()
