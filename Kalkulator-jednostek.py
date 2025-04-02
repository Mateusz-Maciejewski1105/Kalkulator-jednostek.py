def Zamiana_Jednostek (wartosc,przypisana):
    return wartosc*przypisana

opcja="t"
while opcja=="t":
    print("*******************KALKULATOR JEDNOSTEK******************")
    print("1.Zamiana mocy na kW (kilo Wat) na KM (konie mechaniczne)")
    print("2.Zamiana długości km (kilometr) na m (metr)")
    print("3.Zamiana wagi kg (kilogram) na g (gram)")
    print("4.Zamiana prędkości km/h (kilometr na godzinę) na m/s (metr na sekundę)")
    print("5.Zamiana litr na cm^3 (centymetr sześcienny)")
    print("6.Wyznacz pierwiastki rzeczywiste rownania kwadratowego")
    print("7.Wskaż największą liczbę rzeczywistą z 3 wprowadzonych przez użytkownika")
    print("0.Koniec")
    wybor=int(input('Którą opcję wybierasz?'))

    if (wybor==1):
        liczbaUzytkownika=float(input("Wpisz liczbę którą chcesz zamienić: "))
        wartosc=1.36
        wynik = Zamiana_Jednostek(wartosc,liczbaUzytkownika)
        print("Wartość podana: " + str(liczbaUzytkownika) + " kW, wartość wyliczona: " + str(wynik) + " KM")
        
    elif (wybor==2):
        liczbaUzytkownika=float(input("Wpisz liczbę którą chcesz zamienić: "))
        wartosc=1000
        wynik=Zamiana_Jednostek(wartosc,liczbaUzytkownika)
        print("Wartość podana: " + str(liczbaUzytkownika) + " km, wartość wyliczona: " + str(wynik) + " m")
        
    elif (wybor==3):
        liczbaUzytkownika=float(input("Wpisz liczbę którą chcesz zamienić: "))
        wartosc=1000
        wynik=Zamiana_Jednostek(wartosc,liczbaUzytkownika)
        print("Wartość podana: " + str(liczbaUzytkownika) + " kg, wartość wyliczona: " + str(wynik) + " g")
        
    elif (wybor==4):
        liczbaUzytkownika=float(input("Wpisz liczbę którą chcesz zamienić: "))
        wartosc=11.389
        wynik=Zamiana_Jednostek(wartosc,liczbaUzytkownika)
        print("Wartość podana: " + str(liczbaUzytkownika) + " km/h, wartość wyliczona: " + str(wynik) + " m/s")
        
    elif (wybor==5):
        liczbaUzytkownika=float(input("Wpisz liczbę którą chcesz zamienić: "))
        wartosc=1000
        wynik=Zamiana_Jednostek(wartosc,liczbaUzytkownika)
        print("Wartość podana: " + str(liczbaUzytkownika) + " l, wartość wyliczona: " + str(wynik) + " cm^3")

    elif (wybor==6):
        print("Musisz podać wartości a,b,c w równaniu kwadratowym: ")
        print("ax^2+bx+c")
        a=int(input("Podaj wartość a: "))
        if(a==0):
            print("Otrzymaliśmy równanie liniowe, a nie kwadratowe")
        else:
            b=int(input("Podaj wartość b: "))
            c=int(input("Podaj wartość c: "))
            delta=(b*b)-4*a*c
            if(delta<0):
                print("Równanie nie posiada miejsc zerowych")
            elif(delta==0):
                miejsceZerowe=-b/(2*a)
                print("Równanie posiada jedno miejsce zerowe i jest nim: " + str(miejsceZerowe))
            else:
                import math
                pierwiastekDelta=math.sqrt(delta)
                miejsceZerowePierwsze=(-b-pierwiastekDelta)/(2*a)
                miejsceZeroweDrugie=(-b+pierwiastekDelta)/(2*a)
                print("Równanie posiada dwa miejsca zerowe i są nim: " + str(miejsceZerowePierwsze) + " oraz " + str(miejsceZeroweDrugie))

    elif (wybor==7):
        pierwsza=float(input("Podaj pierwszą liczbę: "))
        najwieksza=pierwsza
        ktora="pierwsza"
        druga=float(input("Podaj drugą liczbę: "))
        if(najwieksza<druga):
            najwieksza=druga
            ktora="druga"
        trzecia=float(input("Podaj trzecią liczbę: "))
        if(najwieksza<trzecia):
            najwieksza=trzecia
            ktora="trzecia"
        print("Najwiekszą liczbą jest liczba " + str(najwieksza) + " jest to liczba podana jako: " + ktora)
    elif (wybor==0):
        exit()
    else:
        print("Nie rozpoznano liczby!")
    
    opcja=(input("Czy chcesz jeszcze raz? (t/n):")).lower()
    if(opcja=="n"):
        exit()
    else:
        print("Nie rozpoznano litery proszę o podanie t - tak lub n - nie")
        opcja="t"
