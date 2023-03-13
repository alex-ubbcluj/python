from Domain.obiect import creeaza_obiect, get_ID, get_nume, get_descriere, get_pret_achizitie, get_locatie


def test_creeaza_obiect():
    obiect = creeaza_obiect(256, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099.0, "C503")
    assert get_ID(obiect) == 256
    assert get_nume(obiect) == "Monitor Dell"
    assert get_descriere(obiect) == "23.8'', Full HD, 144Hz"
    assert get_pret_achizitie(obiect) == 1099.0
    assert get_locatie(obiect) == "C503"
