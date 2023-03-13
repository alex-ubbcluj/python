def creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie):
    """
    creeaza un dictionar ce reprezinta un obiect
    param. ID: int (nenul)
    param. nume: string (nenul)
    param. descriere: string (nenul)
    param. pret_achizitie: float (exact 4 caractere)
    param. locatie: string (exact 4 caractere)
    return: un dictionar ce contine un obiect
    """
    return {"id": ID, "nume": nume, "descriere": descriere, "pret": pret_achizitie, "locatie": locatie}


def get_ID(obiect):
    """
    obiect: dictionar ce contine un obiect
    return: ID-ul obiectului
    """
    return obiect["id"]


def get_nume(obiect):
    """
    obiect: dictionar ce contine un obiect
    return: numele obiectului
    """
    return obiect["nume"]


def get_descriere(obiect):
    """
    obiect: dictionar ce contine un obiect
    return: descrierea obiectului
    """
    return obiect["descriere"]


def get_pret_achizitie(obiect):
    """
    obiect: dictionar ce contine un obiect
    return: pretul de achizitie al obiectului
    """
    return obiect["pret"]


def get_locatie(obiect):
    """
    obiect: dictionar ce contine un obiect
    return: locatia obiectului
    """
    return obiect["locatie"]


def to_string(obiect):
    return "ID: {}, Nume: {}, Descriere: {}, Pret de achizitie: {}, Locatie: {}".format(get_ID(obiect), get_nume(obiect), get_descriere(obiect), get_pret_achizitie(obiect), get_locatie(obiect))
