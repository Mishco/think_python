from click._compat import raw_input

def main():
    cele = float(raw_input("Zadajte tri realne cisla: "))
    # prve = float(raw_input("Zadajte tri realne cisla\n"))
    # druhe = float(raw_input())
    # tretie = float(raw_input())
    # priemer = prve + druhe + tretie
    priemer = cele[0] + cele[1] + cele[2]
    priemer = priemer / 3
    print("Priemer cisel", prve, druhe, tretie, " je: ", priemer)

if __name__ == "__main__":
    main()
