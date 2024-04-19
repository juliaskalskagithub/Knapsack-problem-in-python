# import potrzbnych bibliotek
import random
import pandas as pd
import numpy as np
import time
import os

# Ścieżka do folderu, w którym znajdują się pliki Excel
folder_path = 'C:/Users/kryst/Desktop/Studia/IV semestr/Optymalizacja dyskretna - projekt'

# Usunięcie wszystkich plików Excel z folderu
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)

lista1 = []
lista2 = []
lista3 = []
lista4 = []
pl1 = []
pl2 = []
pl3 = []
pl4 = []

# generowanie skorelowanych wag i cen
def generuj_dane(liczba_rekordow):
    dane = []
    for i in range(1, liczba_rekordow+1):
        waga = random.randint(1, 50)
        cena = waga * random.randint(1, 30)
        nazwa = "p" + str(i)
        dane.append((nazwa, waga, cena))
    return dane
    

# przedmioty = ['Zegarek', 'Kurtka', 'Książka', 'Radio', 'Termos', 'Laptop']
# ceny_przedmiotow = [20, 15, 8, 35, 13, 200]
# waga_przedmiotow = [3, 4, 6, 6, 1, 7]
#ramka = pd.DataFrame({'Przedmiot':przedmioty, 'Cena':ceny_przedmiotow, 'Waga [kg]':waga_przedmiotow})
linia = "-" * 80

# wczytanie danych z pliku csv oraz ustawienie pojemności plecaka
#ramka = pd.read_excel('problem_plecakowy.xlsx', header=0)



# Algorytm zachłanny I - cena posortowana nierosnąco
def algorytm_zachlanny_cena(ramka, pojemnosc_plecaka):
    start=time.time()
    obciazenie_plecaka = 0
    cena = 0
    plecak = []
    # posortowanie przedmiotów względem wartości
    posortowane_cena = ramka.sort_values('Cena', ascending=False, ignore_index=True)

    for i in range(0, zakres):
        #print(posortowane_cena.iloc[i]['Przedmiot'])
        # sprawdzanie czy przedmiot mieści się w plecaku, następnie dodanie wagi do obciążenia, przedmiotu do plecaka oraz ceny do wartości
        if obciazenie_plecaka + posortowane_cena.iloc[i]['Waga [kg]'] <= pojemnosc_plecaka:
            obciazenie_plecaka = obciazenie_plecaka + posortowane_cena.iloc[i]['Waga [kg]']
            cena = cena + posortowane_cena.iloc[i]['Cena']
            plecak.append(posortowane_cena.iloc[i]['Przedmiot']) 
    wynik = f'\n\nAlgorytm zachłanny - wersja pierwsza (sortowanie po wartości): \n\n{posortowane_cena}\n\nPrzedmioty dodane do plecaka: {plecak}\
          \nWartość plecaka: {cena} \nWaga plecaka: {obciazenie_plecaka} \n\n{linia}' 
    stop=time.time()
    czas=stop-start  
    print("czas", czas)
    lista1.append(czas)
    komorka = f'Wartość: {cena}, Obciążenie plecaka: {obciazenie_plecaka}'
    pl1.append(komorka)
    return wynik
     


# Algorytm zachłanny II - waga posortowana niemalejąco
def algorytm_zachlanny_waga(ramka, pojemnosc_plecaka):
    start = time.time()
    # posortowanie przedmiotow względem wagi
    posortowane_waga = ramka.sort_values('Waga [kg]', ascending=True, ignore_index=True)

    obciazenie_plecaka = 0
    cena = 0
    plecak = []

    for i in range(0, zakres):
        #print(posortowane_waga.iloc[i]['Przedmiot'])
        # sprawdzanie czy przedmiot mieści się w plecaku, następnie dodanie wagi do obciążenia, przedmiotu do plecaka oraz ceny do wartości
        if obciazenie_plecaka + posortowane_waga.iloc[i]['Waga [kg]'] <= pojemnosc_plecaka:
            obciazenie_plecaka = obciazenie_plecaka + posortowane_waga.iloc[i]['Waga [kg]']
            cena = cena + posortowane_waga.iloc[i]['Cena']
            plecak.append(posortowane_waga.iloc[i]['Przedmiot'])
        else:
            break
            
    wynik = f'\n\nAlgorytm zachłanny - wersja druga (sortowanie po wadze): \n\n{posortowane_waga}\n\n\
        Przedmioty dodane do plecaka: {plecak} \nWartość plecaka: {cena} \nWaga plecaka: {obciazenie_plecaka}\n\n{linia}' 
    stop=time.time()
    czas=stop-start  
    print("czas", czas)
    lista2.append(czas)  
    komorka = f'Wartość: {cena}, obciążenie: {obciazenie_plecaka}'
    pl2.append(komorka)    
    return wynik


# Algorytm zachłanny III - wartość na jednostkę masy posortowana nierosnąco
def algorytm_zachlanny_waga_cena(ramka, pojemnosc_plecaka):
    start = time.time()
    # dodanie kolumny zawierającej cenę na jednostkę masy
    ramka['Wartosc na jednostke masy'] = ramka['Cena']/ramka['Waga [kg]']
    # posortowanie przedmiotów względem wartości na jednostkę masy
    posortowane_waga_cena = ramka.sort_values('Wartosc na jednostke masy', ascending=False, ignore_index=True)

    obciazenie_plecaka = 0
    cena = 0
    plecak = []

    for i in range(0, zakres):
        #print(posortowane_waga_cena.iloc[i]['Przedmiot'])
        # sprawdzanie czy przedmiot mieści sie w plecaku, następnie dodanie wagi do obciązenia, przedmiotu do plecaka oraz ceny do wartości
        if obciazenie_plecaka + posortowane_waga_cena.iloc[i]['Waga [kg]'] <= pojemnosc_plecaka:
            obciazenie_plecaka = obciazenie_plecaka + posortowane_waga_cena.iloc[i]['Waga [kg]']
            cena = cena + posortowane_waga_cena.iloc[i]['Cena']
            plecak.append(posortowane_waga_cena.iloc[i]['Przedmiot'])
            
    wynik = f'\n\nAlgorytm zachłanny - wersja trzecia (nierosnąco względem wartości na jednostkę masy): \n\n{posortowane_waga_cena}\n\n\
        Przedmioty dodane do plecaka: {plecak} \nWartość plecaka: {cena} \nWaga plecaka: {obciazenie_plecaka}\n\n{linia}'   
    stop=time.time()
    czas=stop-start  
    print("czas", czas)
    lista3.append(czas)
    komorka = f'Wartość: {cena}, obciążenie: {obciazenie_plecaka}'
    pl3.append(komorka)     
    return wynik



# Programowanie dynamiczne
def programowanie_dynamiczne(ramka, pojemnosc_plecaka):
    start = time.time()
    # posortowanie przedmiotów względem wagi
    posortowane_waga = ramka.sort_values('Waga [kg]', ascending=True, ignore_index=True)
    # zdefiniowanie dwuwymiarowej listy o wymiarach odpowiadających dlugości listy przedmiotów + 1 oraz pojemności plecaka +1, zawierającej same 0
    K = [[0]*(pojemnosc_plecaka+1) for i in range(zakres+1)]
    
    # dodanie do tablicy K wartości cen które są maksymalne dla określonej wagi
    for i in range(zakres+1):
        for j in range(pojemnosc_plecaka+1):
            # pierwszy wiersz i pierwszą kolumnę wypełniamy 0
            if i == 0 or j == 0:
                K[i][j] = 0
            elif posortowane_waga.iloc[i-1]['Waga [kg]'] <= j:
                # sprawdzamyy czy dołozenie innego przedmiotu zwiekszy wartosc
                K[i][j] = max(posortowane_waga.iloc[i-1]['Cena'] + K[i-1][j-posortowane_waga.iloc[i-1]['Waga [kg]']], K[i-1][j])
            else:
                # wykonuje sie wtedy gdy nie mozemy dolozyc danej rzeczy bo przekroczy wage
                K[i][j] = K[i-1][j]


    
    plecak = []
    obciazenie_plecaka = 0

    # wyświetlenie tablicy K
    print('\n\nProgramowanie dynamiczne: \n\nTablica K:')
    for i in range(zakres+1):
        for j in range(pojemnosc_plecaka+1):
            print('{:4}'.format(K[i][j]), end=' ')
        print()

    #print('\n\nMacierz przejść: \n\nTablica G:')

    G=K

    # zdefiniowanie dwuwymiarowej tablicy G z wartościami 0
    G = [[0 for i in range(len(K[0]))] for j in range(len(K))] 

    # stworzenie zero jedynkowej macierzy przejść
    for i in range(1,pojemnosc_plecaka+1,1):
        # słownik przechowujący pierwsze wystąpienie każdej wartości
        pierwsze_wystapienia = {}  
        for j in range(1,zakres+1,1):
            wartosc = K[j][i]
            # jeśli wartość jest równa 0, ustawiamy w tablicy G wartość 0
            if wartosc == 0:
                G[j][i] = 0
            # jeśli wartość już wystąpiła wcześniej w kolumnie, ustawiamy 0
            elif wartosc in pierwsze_wystapienia:  
                G[j][i] = 0
            # jeśli wartość po raz pierwszy wystąpiła w kolumnie, ustawiamy 1 i zapisujemy jej indeks
            else:  
                G[j][i] = 1
                pierwsze_wystapienia[wartosc] = j
    #print(pierwsze_wystapienia)

    # wyświetlenie tablicy G
    #for i in range(zakres+1):
     #   for j in range(pojemnosc_plecaka+1):
      #      print('{:4}'.format(G[i][j]), end=' ')
       # print()

    
    suma = 0
    # obliczenie sumy komórek tablicy G
    for i in range(1,pojemnosc_plecaka+1,1):
            for j in range(1,zakres+1,1):
                suma= suma + G[j][i]

    #print(suma)

    # stworzenie macierzy G z tablicy G
    G = np.array(G)
    #print(G)


    while suma > 0:
        suma=0
        # print(G.shape)
        # przypisanie wymiarów macierzy G
        num_rows, num_cols = G.shape
        # print(num_rows)
        # print(num_cols)
        # przypisanie ostatniej komorki macierzy G
        komorka = G[num_rows-1][num_cols-1]
        # znalezienie przedmiotu odpowiadajacemu numerowi wierszu, w którym się znajdujemy
        przedmiot = posortowane_waga.iloc[num_rows-2]['Waga [kg]']
        # sprawdzenie czy przypisana komórka ma wartość 1, jeśli tak to usunięcie wiersza, w którym się znajdujemy i liczby kolumn odpowiadającą wadze przedmiotu
        if komorka == 1:
            G = np.delete(G,-1, 0)
            G = np.delete(G, np.s_[-przedmiot:], 1)
            # dodanie przedmiotu do plecaka i zwiększenie jego obciążenia
            plecak.append(posortowane_waga.iloc[num_rows-2]['Przedmiot'])
            obciazenie_plecaka = obciazenie_plecaka + przedmiot
        else:
            # usunięcie wiersza, w którym się znajdujemy
            G = np.delete(G, -1, 0)

        #print(num_rows)
        #print(num_cols)

        # obliczenie sumy komórek w macierzy
        num_rows, num_cols = G.shape
        for i in range(0,num_cols,1):
            for j in range(0,num_rows,1):
                suma = suma + G[j][i]
        #print(f"Suma komórek w poniższej macierzy: {suma}")
        #print(G)

    
    wynik = f'\n\nPrzedmioty dodane do plecaka: {plecak} \nWartość plecaka: {K[zakres][pojemnosc_plecaka]} \nWaga plecaka: {obciazenie_plecaka}\n\n{linia}' 
    stop=time.time()
    czas=stop-start  
    print("czas", czas)
    lista4.append(czas)
    komorka = f'Wartość: {K[zakres][pojemnosc_plecaka]}, obciążenie: {obciazenie_plecaka}'
    pl4.append(komorka)    
    return wynik

# wywołanie funkcji
pojemnosc_plecaka = int(input("Podaj pojemność plecaka: "))
liczba_przedmiotow = int(input("Podaj liczbę przedmiotów: "))
liczba_iteracji = int(input("Podaj ile razy mają wylosować się przedmioty: "))
for i in range(liczba_iteracji):
    # Wywołanie funkcji generującej przedmioty
    dane = generuj_dane(liczba_przedmiotow)
    # Tworzenie ramki danych
    ramka = pd.DataFrame(dane, columns=["Przedmiot", "Waga [kg]", "Cena"])
    output_path = os.path.join(folder_path, f'losowanie{i+1}.xlsx')
    ramka.to_excel(output_path, index=False)
    print('Nasze przedmioty: \n\n', ramka, '\n\n', linia)
    
# wyznaczenie długości listy przedmiotów
    zakres = len(list(ramka.iterrows()))
    print(algorytm_zachlanny_cena(ramka, pojemnosc_plecaka))
    print(algorytm_zachlanny_waga(ramka, pojemnosc_plecaka))
    print(algorytm_zachlanny_waga_cena(ramka, pojemnosc_plecaka))
    print(programowanie_dynamiczne(ramka, pojemnosc_plecaka))
nazwy_wierszy = ['Losowanie {}'.format(i)  for i in range(1,liczba_iteracji + 1)]
podsumowanie2 = pd.DataFrame({'Algorytm_zachłanny_1':pl1, 'Algorytm_zachłanny_2':pl2, 'Algorytm_zachłanny_3':pl3, 'Algorytm_dokładny':pl4}, index=nazwy_wierszy)
print(podsumowanie2)
print('\n')
podsumowanie = pd.DataFrame({'Algorytm_zachłanny_1':lista1, 'Algorytm_zachłanny_2':lista2, 'Algorytm_zachłanny_3':lista3, 'Algorytm_dokładny':lista4}, index=nazwy_wierszy)
print(podsumowanie)
