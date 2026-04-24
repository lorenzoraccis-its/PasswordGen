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
    password=[]
    ambigui = "Il1O0" #da evitare se opzione attiva
    pool = ""
    if use_upper :
        pool+=string.ascii_uppercase
    if use_lower :
        pool+=string.ascii_lowercase
    if use_digits :
        pool+=string.digits
    if use_symbols :
        pool+=string.punctuation
    password.append((secrets.choice(string.ascii_uppercase))) if use_upper == True else ""
    password.append(secrets.choice(string.ascii_lowercase))  if use_lower == True else ""
    password.append(secrets.choice(string.digits))  if use_digits == True else ""
    password.append(secrets.choice(string.punctuation)) if use_symbols == True else ""
    minimo = len(password) #cosi non sovrascriviamo i caratteri appena messi
    if avoid_ambiguous :
        for i in ambigui :
            pool = pool.replace(i,"") #rimpiazza i caratteri ambigui della pool con ""
    for i in range(length-minimo) :
        password.append(secrets.choice(pool))
        secrets.SystemRandom().shuffle(password)
    mischiata = "".join(password)
    return mischiata



def build_alphabet() :
    length = int(input("Lunghezza password : "))
    upper = input("Maiuscole Y/n : ")
    lower = input("Minuscole Y/n : ")
    digits = input("Numeri Y/n : ")
    symbols = input("Simboli Y/n : ")
    ambiguous = input("Caratteri ambigui Y/n : ")
    use_upper = True if upper.lower() == "y" or upper == "" else False
    use_lower = True if lower.lower() == "y" or lower == "" else False
    use_digits = True if digits.lower() == "y" or digits == "" else False
    use_symbols = True if symbols.lower() == "y" or symbols == "" else False
    avoid_ambiguous = True if ambiguous.lower() == "y" or ambiguous == "" else False
    print("\nPassword generata!\n")
    return length, use_upper, use_lower, use_digits, use_symbols, avoid_ambiguous



def __main__():
    print("""\n\n$ python password_generator.py
=== Password generator ===
1) Profilo default (12 caratteri, tutti i set)
2) Profilo custom\n""")
    scelta=input("Scelta : ")
    if scelta=="1":
        print(f"Password : {generate_password()}")
    elif scelta=="2":
        # qua lasciamo scelta all'utente su quali caratteri usare
        print(f"Password : {generate_password(*build_alphabet())}")
    else:
        print("Scelta non valida")

if __name__ == "__main__":
    __main__()
