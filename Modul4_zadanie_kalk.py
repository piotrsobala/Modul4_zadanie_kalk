import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def dodawanie(a, b, lista):
    return a + b + lista

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b, lista):
    return a * b * lista

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

wybor = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

liczba1 = float(input("Podaj składnik 1: "))
liczba2 = float(input("Podaj składnik 2: "))


if wybor == '1':
    try:
        items = input("Możesz podać więcej liczb. Rozdziel je przecinkiem: ")
        items_new = items.split(',')
        lista = 0
        for item in items_new:
            lista += float(item)
    except ValueError:
        pass      
    logging.info("Dodaję %s i %s i %s." % (liczba1, liczba2, items))
    print("Wynik dodawania:", dodawanie(liczba1, liczba2, lista)) 
    
    
    
elif wybor == '2':
    logging.info("Odejmuję %s i %s." % (liczba1, liczba2))
    print("Wynik odejmowania:", odejmowanie(liczba1, liczba2))
elif wybor == '3':
    try:
        items= input("Możesz podać więcej liczb. Rozdziel je przecinkiem ")
        items_new = items.split(',')
        lista = 1
        for item in items_new:
            lista *= float(item)
    except ValueError:
        pass
    logging.info("Mnożę %s i %s i %s." % (liczba1, liczba2, items))
    print("Wynik mnożenia:", mnozenie(liczba1, liczba2, lista))
    
elif wybor == '4':
    logging.info("Dzielę %s i %s." % (liczba1, liczba2))
    print("Wynik dzielenia:", dzielenie(liczba1, liczba2))
else:
    print("Błędny wybór działania")
    
exit()