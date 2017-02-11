from click._compat import raw_input
import tkinter

def print_menu():
    print("Vyberte si jednu moznost")
    print("***********")
    print("(S) sucet")
    print("(O) odcitanie")
    print("(N) nasobenie")
    print("(D) delenie")
    print("(x) koniec")
    print("***********")

def get_option():
    return raw_input()

def print_cisla():
    print("Zadaj dva cisla")

def scitanie():
    print_cisla()
    a = float(raw_input())
    b = float(raw_input())
    return a + b

def odcitanie():
    print_cisla()
    a = float(raw_input())
    b = float(raw_input())
    return a - b

def nasobenie():
    print_cisla()
    a = float(raw_input())
    b = float(raw_input())
    return a * b

def delenie():
    print_cisla()
    a = float(raw_input())
    b = float(raw_input())
    return a / b

def decide(char):
    res = -1
    if(char=='S' or char == 's'):
        res = scitanie()
    elif(char=='O' or char == 'o'):
        res = odcitanie()
    elif(char=='N' or char == 'n'):
        res = nasobenie()
    elif(char=='D' or char == 'd'):
        res = delenie()
    elif(char=='X' or char == 'x'):
        exit(1)
    else:
        print("Nespravne zadane pismeno")
        return
    print("Vysledok je: ", res)

def main():
    while(1):
        print_menu()
        decide(get_option())
    


if __name__ == '__main__':
    main()