from Domain.obiect import creeaza_obiect, get_descriere, get_ID, get_locatie
from Logic.CRUD import adauga_obiect
from Logic.functionalitati import concatenare_str, ordonare_cresc_dupa_pret, pret_max_fiecare_locatie, suma_fiecare_locatie, mutare_obiecte


def test_mutare_obiecte():
    lst = []
    lst = adauga_obiect(1, "obiect test 1", "descriere 1", 4000.0, "LOC1", lst)
    lst = adauga_obiect(2, "obiect test 2", "descriere 2", 1000.0, "LOC2", lst)
    lst = adauga_obiect(3, "obiect test 3", "descriere 3", 3000.0, "LOC2", lst)
    lst = adauga_obiect(4, "obiect test 4", "descriere 4", 2000.0, "LOC1", lst)
    lst = mutare_obiecte("LOC1", "LOC2", lst)
    assert get_locatie(lst[0]) == "LOC2"
    assert get_locatie(lst[3]) == "LOC2"


def test_concatenare_str():
    obiect = creeaza_obiect(256, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099.0, "C503")
    string = " string de test"
    concatenare_str(obiect, string)
    assert get_descriere(obiect) == "23.8'', Full HD, 144Hz string de test"


def test_pret_max_fiecare_locatie():
    lst = []
    lst = adauga_obiect(1, "obiect test 1", "descriere 1", 4000.0, "LOC1", lst)
    lst = adauga_obiect(2, "obiect test 2", "descriere 2", 1000.0, "LOC2", lst)
    lst = adauga_obiect(3, "obiect test 3", "descriere 3", 3000.0, "LOC2", lst)
    lst = adauga_obiect(4, "obiect test 4", "descriere 4", 2000.0, "LOC1", lst)
    rezultat = pret_max_fiecare_locatie(lst)
    assert rezultat["LOC1"] == 4000.0
    assert rezultat["LOC2"] == 3000.0


def test_ordonare_cresc_dupa_pret():
    lst = []
    lst = adauga_obiect(1, "obiect test 1", "descriere 1", 4000.0, "----", lst)
    lst = adauga_obiect(2, "obiect test 2", "descriere 2", 1000.0, "----", lst)
    lst = adauga_obiect(3, "obiect test 3", "descriere 3", 3000.0, "----", lst)
    lst = adauga_obiect(4, "obiect test 4", "descriere 4", 2000.0, "----", lst)
    lst = ordonare_cresc_dupa_pret(lst)
    assert get_ID(lst[0]) == 2
    assert get_ID(lst[1]) == 4
    assert get_ID(lst[2]) == 3
    assert get_ID(lst[3]) == 1


def test_suma_fiecare_locatie():
    lst = []
    lst = adauga_obiect(1, "obiect test 1", "descriere 1", 4000.0, "LOC1", lst)
    lst = adauga_obiect(2, "obiect test 2", "descriere 2", 1000.0, "LOC2", lst)
    lst = adauga_obiect(3, "obiect test 3", "descriere 3", 3000.0, "LOC2", lst)
    lst = adauga_obiect(4, "obiect test 4", "descriere 4", 2000.0, "LOC1", lst)
    rezultat = suma_fiecare_locatie(lst)
    assert rezultat["LOC1"] == 6000.0
    assert rezultat["LOC2"] == 4000.0
