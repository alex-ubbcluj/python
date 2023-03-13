from Domain.obiect import get_ID, get_nume, get_descriere, get_pret_achizitie, get_locatie
from Logic.CRUD import adauga_obiect, get_by_ID, sterge_obiect, modifica_obiect


def test_adauga_obiect():
    lst = []
    lst = adauga_obiect(33, "Frigider Samsung", "Clasa energetica A+, volum 384L", 1949.0, "C004", lst)
    lst = adauga_obiect(256, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099.0, "C503", lst)
    assert len(lst) == 2
    assert get_ID(lst[1]) == 256
    assert get_nume(lst[1]) == "Monitor Dell"
    assert get_descriere(lst[1]) == "23.8'', Full HD, 144Hz"
    assert get_pret_achizitie(lst[1]) == 1099.0
    assert get_locatie(lst[1]) == "C503"


def test_get_by_ID():
    lst = []
    lst = adauga_obiect(33, "Frigider Samsung", "Clasa energetica A+, volum 384L", 1949.0, "C004", lst)
    lst = adauga_obiect(256, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099.0, "C503", lst)
    assert get_ID(get_by_ID(256, lst)) == 256
    assert get_nume(get_by_ID(256, lst)) == "Monitor Dell"
    assert get_descriere(get_by_ID(256, lst)) == "23.8'', Full HD, 144Hz"
    assert get_pret_achizitie(get_by_ID(256, lst)) == 1099.0
    assert get_locatie(get_by_ID(256, lst)) == "C503"


def test_sterge_obiect():
    lst = []
    lst = adauga_obiect(33, "Frigider Samsung", "Clasa energetica A+, volum 384L", 1949.0, "C004", lst)
    lst = adauga_obiect(256, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099.0, "C503", lst)
    lst = sterge_obiect(33, lst)
    assert len(lst) == 1
    assert get_by_ID(33, lst) is None
    assert get_ID(lst[0]) == 256
    assert get_nume(lst[0]) == "Monitor Dell"
    assert get_descriere(lst[0]) == "23.8'', Full HD, 144Hz"
    assert get_pret_achizitie(lst[0]) == 1099.0
    assert get_locatie(lst[0]) == "C503"


def test_modifica_obiect():
    lst = []
    lst = adauga_obiect(33, "Frigider Samsung", "Clasa energetica A+, volum 384L", 1949.0, "C004", lst)
    lst = modifica_obiect(33, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099.0, "C503", lst)
    assert get_ID(lst[0]) == 33
    assert get_nume(lst[0]) == "Monitor Dell"
    assert get_descriere(lst[0]) == "23.8'', Full HD, 144Hz"
    assert get_pret_achizitie(lst[0]) == 1099.0
    assert get_locatie(lst[0]) == "C503"
