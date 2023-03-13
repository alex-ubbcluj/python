from Service.client_service import ClientService
from Service.tranzactie_service import TranzactieService


class Console:
    def __init__(self, client_service: ClientService,
                 tranzactie_service: TranzactieService):
        self.client_service = client_service
        self.tranzactie_service = tranzactie_service

    def run_meniu(self):
        while True:
            print("1. Adauga client")
            print("2. Adauga tranzactie")
            print("3. Afișarea clienților ordonați descrescător "
                  "după numărul de vocale (a,e,i,o,u) din nume")
            print("4. Afișarea tuturor tranzacțiilor "
                  "care sunt considerate periculoase")
            print("5. Export Json")
            print("a1. Afiseaza toti clientii")
            print("a2. Afiseaza toate tranzactiile")
            print("x. Exit")
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                self.adauga_client()
                self.afiseaza(self.client_service.get_all())
            elif optiune == "2":
                self.adauga_tranzactie()
                self.afiseaza(self.tranzactie_service.get_all())
            elif optiune == "3":
                self.afiseaza(
                    self.client_service.ordoneaza_descrescator_numar_vocale())
            elif optiune == "4":
                self.afiseaza(
                    self.tranzactie_service.determina_tranzactii_periculoase())
            elif optiune == "5":
                self.ui_export_json()
            elif optiune == "a1":
                self.afiseaza(self.client_service.get_all())
            elif optiune == "a2":
                self.afiseaza(self.tranzactie_service.get_all())
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def adauga_client(self):
        try:
            id_client = input("Dati id-ul clientului: ")
            nume = input("Dati numele clientului: ")
            cnp = input("Dati CNP-ul clientului: ")
            sold_initial = float(input("Dati soldul initial: "))
            self.client_service.adauga(id_client, nume, cnp, sold_initial)
        except Exception as e:
            print(e)

    def adauga_tranzactie(self):
        try:
            id_tranzactie = input("Dati id-ul tranzactiei: ")
            id_client_sursa = input("Dati id-ul clientului sursa: ")
            id_client_destinatie = input("Dati id-ul clientului destinatie: ")
            valoare = float(input("Dati valoarea tranzactiei: "))
            self.tranzactie_service.adauga(id_tranzactie, id_client_sursa,
                                           id_client_destinatie, valoare)
        except Exception as e:
            print(e)

    def ui_export_json(self):
        try:
            cnp = input("Introduceti CNP-ul clientului cautat: ")
            filename = input("Dati numele fisierului "
                             "in care se va face exportul: ")
            self.tranzactie_service.export_json(cnp, filename)
        except Exception as e:
            print(e)
