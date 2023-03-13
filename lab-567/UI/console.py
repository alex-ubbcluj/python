from copy import deepcopy
from Domain.obiect import to_string, get_pret_achizitie
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.functionalitati import concatenare_str, ordonare_cresc_dupa_pret, pret_max_fiecare_locatie, suma_fiecare_locatie, mutare_obiecte


def print_meniu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locație în alta")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("6. Afisarea celui mai mare preț pentru fiecare locație")
    print("7. Afisarea obiectelor ordonate crescător după prețul de achiziție")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare obiecte")
    print("b. Back")


def console_adauga_obiect(lst, undo_list, redo_list):
    try:
        ID = int(input("Introduceti ID-ul: "))
        nume = input("Introduceti numele: ")
        descriere = input("Introduceti descrierea: ")
        pret_achizitie = float(input("Introduceti pretul de achizitie: "))
        locatie = input("Introduceti locatia: ")
        rezultat = adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lst)
        undo_list.append(lst)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lst


def console_sterge_obiect(lst, undo_list, redo_list):
    try:
        ID = int(input("Introduceti ID-ul obiectului de sters: "))
        rezultat = sterge_obiect(ID, lst)
        undo_list.append(lst)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lst


def console_modifica_obiect(lst, undo_list, redo_list):
    try:
        ID = int(input("Introduceti ID-ul obiectului de modificat: "))
        nume = input("Introduceti noul nume: ")
        descriere = input("Introduceti noua descriere: ")
        pret_achizitie = float(input("Introduceti noul pret de achizitie: "))
        locatie = input("Introduceti noua locatie: ")
        rezultat = modifica_obiect(ID, nume, descriere, pret_achizitie, locatie, lst)
        undo_list.append(lst)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lst


def console_mutare_obiect(lst, undo_list, redo_list):
    try:
        old_loc = input("Introduceti locatia obiectelor pe care vreti sa le mutati: ")
        new_loc = input("Introduceti noua locatie: ")
        rezultat = deepcopy(lst)
        rezultat = mutare_obiecte(old_loc, new_loc, rezultat)
        undo_list.append(lst)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    except RuntimeError as re:
        print("Atentie! {}".format(re))
        return lst


def console_concatenare_str(lst, undo_list, redo_list):
    try:
        string = input("Introduceti stringul: ")
        console_pret = float(input("Introduceti un pret: "))
        rezultat = deepcopy(lst)
        for obiect in rezultat:
            if get_pret_achizitie(obiect) > console_pret:
                concatenare_str(obiect, string)
        undo_list.append(lst)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lst


def console_pret_max_fiecare_locatie(lst):
    rezultat = pret_max_fiecare_locatie(lst)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim de {}".format(locatie, rezultat[locatie]))


def console_ordonare_cresc_dupa_pret(lst):
    show_all(ordonare_cresc_dupa_pret(lst))


def console_suma_fiecare_locatie(lst):
    rezultat = suma_fiecare_locatie(lst)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor de {}".format(locatie, rezultat[locatie]))


def show_all(lst):
    for obiect in lst:
        print(to_string(obiect))


def run_meniu(lst):
    undo_list = []
    redo_list = []
    while True:
        print_meniu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1": 
            lst = console_adauga_obiect(lst, undo_list, redo_list)
        elif optiune == "2": 
            lst = console_sterge_obiect(lst, undo_list, redo_list)
        elif optiune == "3": 
            lst = console_modifica_obiect(lst, undo_list, redo_list)
        elif optiune == "4":
            lst = console_mutare_obiect(lst, undo_list, redo_list)
        elif optiune == "5":
            lst = console_concatenare_str(lst, undo_list, redo_list)
        elif optiune == "6":
            console_pret_max_fiecare_locatie(lst)
        elif optiune == "7":
            console_ordonare_cresc_dupa_pret(lst)
        elif optiune == "8":
            console_suma_fiecare_locatie(lst)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lst)
                lst = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lst)
                lst = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            show_all(lst)
        elif optiune == "b":
            break
        else: 
            print("Optiune invalida!")
