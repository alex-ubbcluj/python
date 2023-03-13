from Domain.obiect import creeaza_obiect, get_ID


def adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lst):
    """
    adauga un obiect intr-o lista
    param. ID: int (nenul)
    param. nume: string (nenul)
    param. descriere: string (nenul)
    param. pret_achizitie: float (exact 4 caractere)
    param. locatie: string (exact 4 caractere)
    param. lst: lista de obiecte
    return: o lista ce contine atat elementele vechi cat si noul obiect
    """
    if ID < 1:
        raise ValueError("ID-ul nu poate fi nenul sau negativ!")
    if get_by_ID(ID, lst) is not None:
        raise ValueError("ID-ul introdus exista deja!")
    if len(nume) == 0:
        raise ValueError("Numele nu poate fi nenul!")
    if len(descriere) == 0:
        raise ValueError("Descrierea nu poate fi nenula!")
    if pret_achizitie < 0:
        raise ValueError("Pretul de achizitie nu poate fi negativ!")
    if pret_achizitie.is_integer() is True and len(str(int(pret_achizitie))) != 4:
        raise ValueError("Pretul de achizitie trebuie sa aiba exact 4 cifre!")
    if pret_achizitie.is_integer() is False and len(str(pret_achizitie).replace(".", "")) != 4:
        raise ValueError("Pretul de achizitie trebuie sa aiba exact 4 cifre!")
    if len(locatie) != 4:
        raise ValueError("Locatia trebuie sa aiba exact 4 caractere!")
    obiect = creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie)
    return lst + [obiect]


def get_by_ID(ID, lst):
    """
    param ID: int
    param lst: lista de obiecte
    return: obiectul cu ID-ul introdus sau None, daca nu exista
    """
    for obiect in lst:
        if get_ID(obiect) == ID:
            return obiect
    return None


def sterge_obiect(ID, lst):
    """
    sterge din lista obiectul cu ID-ul introdus
    param. ID: ID-ul obiectului ce trebuie sters
    param. lst: o lista de obiecte
    return: lista fara obiectul cu ID-ul introdus
    """
    if get_by_ID(ID, lst) is None:
        raise ValueError("Obiectul cu ID-ul introdus nu exista!")
    return [obiect for obiect in lst if get_ID(obiect) != ID]


def modifica_obiect(ID, nume, descriere, pret_achizitie, locatie, lst):
    """
    modifica obiectul cu ID-ul introdus
    param. ID: int (nenul)
    param. nume: string (nenul)
    param. descriere: string (nenul)
    param. pret_achizitie: float (exact 4 caractere)
    param. locatie: string (exact 4 caractere)
    param. lst: lista de obiecte
    return: o lista in care obiectul cu ID-ul introdus este modificat
    """
    if get_by_ID(ID, lst) is None:
        raise ValueError("Obiectul cu ID-ul introdus nu exista!")
    if len(nume) == 0:
        raise ValueError("Numele nu poate fi nenul!")
    if len(descriere) == 0:
        raise ValueError("Descrierea nu poate fi nenula!")
    if pret_achizitie < 0:
        raise ValueError("Pretul de achizitie nu poate fi negativ!")
    if pret_achizitie.is_integer() is True and len(str(int(pret_achizitie))) != 4:
        raise ValueError("Pretul de achizitie trebuie sa aiba exact 4 cifre!")
    if pret_achizitie.is_integer() is False and len(str(pret_achizitie).replace(".", "")) != 4:
        raise ValueError("Pretul de achizitie trebuie sa aiba exact 4 cifre!")
    if len(locatie) != 4:
        raise ValueError("Locatia trebuie sa aiba exact 4 caractere!")
    new_lst = []
    for obiect in lst:
        if obiect == get_by_ID(ID, lst):
            obiect_nou = creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie)
            new_lst.append(obiect_nou)
        else:
            new_lst.append(obiect)
    return new_lst
