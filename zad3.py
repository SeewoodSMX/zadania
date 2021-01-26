print("Podaj słowo")
x = input()
i = 3
print("Zgadnij słowo, próby:", i)
word = input()
if x == word:
    print("Gratulacje, zgadłeś!")
else:
    while word != x:
        i -= 1
        print("Pomyłka, pozostało prób:", i)
        print("Zgadnij słowo")
        if i <= 0:
            print("Przegrałeś!")
            break
        word = input()
    else:
        print("Gratulacje, zgadłeś!")
