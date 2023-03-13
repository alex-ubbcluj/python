from datetime import datetime
from Domain.film_error import FilmError
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.rezervare_service import RezervareService
from Service.undo_redo_service import UndoRedoService


class Console:
    def __init__(self,
                 film_service: FilmService,
                 card_client_service: CardClientService,
                 rezervare_service: RezervareService,
                 undo_redo_service: UndoRedoService):
        self.__film_service = film_service
        self.__card_client_service = card_client_service
        self.__rezervare_service = rezervare_service
        self.__undo_redo_service = undo_redo_service

    def run_meniu(self):
        while True:
            print("1. CRUD film")
            print("2. CRUD card client")
            print("3. CRUD rezervare")
            print("4. Cautare full text filme si carduri")
            print("5. Afișarea tuturor rezervărilor "
                  "dintr-un interval de ore dat, indiferent de zi")
            print("6. Afișarea filmelor ordonate descrescător "
                  "după numărul de rezervări")
            print("7. Afișarea cardurilor client ordonate descrescător "
                  "după numărul de puncte de pe card")
            print("8. Ștergerea tuturor rezervărilor "
                  "dintr-un anumit interval de zile")
            print("9. Incrementarea cu o valoare dată a punctelor "
                  "de pe toate cardurile a căror zi de naștere "
                  "se află într-un interval dat")
            print("u. Undo")
            print("r. Redo")
            print("x. Exit")
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                self.run_crud_film_meniu()
            elif optiune == "2":
                self.run_crud_card_client_meniu()
            elif optiune == "3":
                self.run_crud_rezervare()
            elif optiune == "4":
                self.ui_cautare_full_text()
            elif optiune == "5":
                self.af_rezervari_interval_orar()
            elif optiune == "6":
                self.af_filme_dupa_nr_rez()
            elif optiune == "7":
                self.af_carduri_dupa_puncte()
            elif optiune == "8":
                self.ui_sterge_rez_interval_zile()
            elif optiune == "9":
                self.ui_incrementare_puncte_interval_zile()
            elif optiune == "u":
                self.__undo_redo_service.undo()
            elif optiune == "r":
                self.__undo_redo_service.redo()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def run_crud_film_meniu(self):
        while True:
            print("1. Adauga film")
            print("2. Sterge film")
            print("3. Modifica film")
            print("r. Genereaza n filme random")
            print("d. Stergere in cascada")
            print("a. Afiseaza toate filmele")
            print("b. Back")
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                self.ui_adauga_film()
            elif optiune == "2":
                self.ui_sterge_film()
            elif optiune == "3":
                self.ui_modifica_film()
            elif optiune == "r":
                self.ui_genereaza_filme_random()
            elif optiune == "d":
                self.ui_sterge_in_cascada()
            elif optiune == "a":
                self.afiseaza_toate_filmele()
            elif optiune == "b":
                break
            else:
                print("Optiune invalida!")

    def run_crud_card_client_meniu(self):
        while True:
            print("1. Adauga card client")
            print("2. Sterge card client")
            print("3. Modifica card client")
            print("r. Genereaza n carduri random")
            print("a. Afiseaza toate cardurile")
            print("b. Back")
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                self.ui_adauga_card_client()
            elif optiune == "2":
                self.ui_sterge_card_client()
            elif optiune == "3":
                self.ui_modifica_card_client()
            elif optiune == "r":
                self.ui_genereaza_carduri_random()
            elif optiune == "a":
                self.afiseaza_toate_cardurile()
            elif optiune == "b":
                break
            else:
                print("Optiune invalida!")

    def run_crud_rezervare(self):
        while True:
            print("1. Adauga rezervare")
            print("2. Sterge rezervare")
            print("3. Modifica rezervare")
            print("a. Afiseaza toate rezervarile")
            print("b. Back")
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                self.ui_adauga_rezervare()
            elif optiune == "2":
                self.ui_sterge_rezervare()
            elif optiune == "3":
                self.ui_modifica_rezervare()
            elif optiune == "a":
                self.afiseaza_toate_rezervarile()
            elif optiune == "b":
                break
            else:
                print("Optiune invalida!")

    def ui_adauga_film(self):
        try:
            id_film = input("Introduceti id-ul filmului: ")
            titlu = input("Introduceti titlul filmului: ")
            an_aparitie = input("Introduceti anul aparitiei: ")
            pret_bilet = float(input("Introduceti pretul biletului: "))
            in_program = input("Mentionati daca filmul "
                               "este in program sau nu('da'/'nu'): ")
            self.__film_service.add(id_film, titlu, an_aparitie,
                                    pret_bilet, in_program)
        except FilmError as fe:
            print(fe)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_film(self):
        try:
            id_film = input("Introduceti id-ul filmului de sters: ")
            self.__film_service.delete(id_film)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_film(self):
        try:
            id_film = input("Introduceti id-ul filmului de modificat: ")
            titlu = input("Introduceti noul titlu: ")
            an_aparitie = input("Introduceti noul an al aparitiei: ")
            pret_bilet = float(input("Introduceti noul pret al biletului: "))
            in_program = input("Mentionati daca noul film "
                               "este in program sau nu: ")
            self.__film_service.update(id_film, titlu, an_aparitie,
                                       pret_bilet, in_program)
        except FilmError as fe:
            print(fe)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def afiseaza_toate_filmele(self):
        for film in self.__film_service.get_all():
            print(film)

    def ui_adauga_card_client(self):
        try:
            id_card_client = input("Introduceti id-ul cardului client: ")
            nume = input("Introduceti numele clientului: ")
            prenume = input("Introduceti prenumele clientului: ")
            cnp = input("Introduceti CNP-ul clientului: ")
            data_nasterii_str = input("Introduceti data nasterii clientului "
                                      "<dd.mm.yyyy>: ")
            data_inregistrarii_str = input("Introduceti data "
                                           "inregistrarii cardului "
                                           "<dd.mm.yyyy>: ")
            data_nasterii_lst = data_nasterii_str.split(".")
            data_inregistrarii_lst = data_inregistrarii_str.split(".")
            data_nasterii = datetime(int(data_nasterii_lst[2]),
                                     int(data_nasterii_lst[1]),
                                     int(data_nasterii_lst[0]))
            data_inregistrarii = datetime(int(data_inregistrarii_lst[2]),
                                          int(data_inregistrarii_lst[1]),
                                          int(data_inregistrarii_lst[0]))
            self.__card_client_service.add(id_card_client, nume, prenume,
                                           cnp, data_nasterii,
                                           data_inregistrarii,
                                           0)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_card_client(self):
        try:
            id_card_client = input("Introduceti id-ul cardului de sters: ")
            self.__card_client_service.delete(id_card_client)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_card_client(self):
        try:
            id_card_client = input("Introduceti id-ul cardului de modificat: ")
            nume = input("Introduceti noul nume: ")
            prenume = input("Introduceti noul prenume: ")
            cnp = input("Introduceti noul CNP: ")
            data_nasterii_str = input("Introduceti noua data a nasterii "
                                      "<dd.mm.yyyy>: ")
            data_inregistrarii_str = input("Introduceti noua data "
                                           "a inregistrarii cardului "
                                           "<dd.mm.yyyy>: ")
            puncte_acumulate = int(input("Introduceti noile "
                                         "puncte acumulate: "))
            data_nasterii_lst = data_nasterii_str.split(".")
            data_inregistrarii_lst = data_inregistrarii_str.split(".")
            data_nasterii = datetime(int(data_nasterii_lst[2]),
                                     int(data_nasterii_lst[1]),
                                     int(data_nasterii_lst[0]))
            data_inregistrarii = datetime(int(data_inregistrarii_lst[2]),
                                          int(data_inregistrarii_lst[1]),
                                          int(data_inregistrarii_lst[0]))
            self.__card_client_service.update(id_card_client,
                                              nume, prenume,
                                              cnp, data_nasterii,
                                              data_inregistrarii,
                                              puncte_acumulate)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def afiseaza_toate_cardurile(self):
        for card_client in self.__card_client_service.get_all():
            print(card_client)

    def ui_adauga_rezervare(self):
        try:
            id_rezervare = input("Introduceti id-ul rezervarii: ")
            id_film = input("Introduceti id-ul filmului: ")
            id_card_client = input("Introduceti id-ul cardului client: ")
            if id_card_client == "":
                id_card_client = None
            data_str = input("Introduceti data rezervarii <dd.mm.yyyy>: ")
            ora = float(input("Introduceti ora rezervarii: "))
            data_lst = data_str.split(".")
            data = datetime(int(data_lst[2]),
                            int(data_lst[1]),
                            int(data_lst[0]))
            self.__rezervare_service.add(id_rezervare, id_film,
                                         id_card_client, data, ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_rezervare(self):
        try:
            id_rezervare = input("Introduceti id-ul rezervarii de sters: ")
            self.__rezervare_service.delete(id_rezervare)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_rezervare(self):
        try:
            id_rezervare = input("Introduceti id-ul rezervarii de modificat: ")
            id_film = input("Introduceti noul id al filmului: ")
            id_card_client = input("Introduceti noul id al cardului client: ")
            if id_card_client == "":
                id_card_client = None
            data_str = input("Introduceti noua data "
                             "a rezervarii <dd.mm.yyyy>: ")
            ora = float(input("Introduceti noua ora a rezervarii: "))
            data_lst = data_str.split(".")
            data = datetime(int(data_lst[2]),
                            int(data_lst[1]),
                            int(data_lst[0]))
            self.__rezervare_service.update(id_rezervare, id_film,
                                            id_card_client, data, ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def afiseaza_toate_rezervarile(self):
        for rezervare in self.__rezervare_service.get_all():
            print(rezervare)

    def ui_cautare_full_text(self):
        try:
            search_str = input("Introduceti stringul "
                               "dupa care doriti sa faceti cautarea: ")
            for film in self.__film_service.cautare_film(search_str):
                print(film)
            for card_client in \
                    self.__card_client_service.cautare_card_client(search_str):
                print(card_client)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def af_rezervari_interval_orar(self):
        try:
            ora_inceput = float(input("Introduceti ora de inceput: "))
            ora_sfarsit = float(input("Introduceti ora de sfarsit: "))
            for rezervare in self.__rezervare_service.rezervari_interval_orar(
                                                     ora_inceput, ora_sfarsit):
                print(rezervare)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_genereaza_filme_random(self):
        try:
            n = int(input("Introduceti n: "))
            self.__film_service.genereaza_filme_random(n)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_genereaza_carduri_random(self):
        try:
            n = int(input("Introduceti n: "))
            self.__card_client_service.genereaza_carduri_random(n)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def af_filme_dupa_nr_rez(self):
        for film_nr_rez in self.__rezervare_service.ord_filme_dupa_nr_rez():
            print(f"{film_nr_rez[0]}, are {film_nr_rez[1]} "
                  f"{'rezervari' if film_nr_rez[1] != 1 else 'rezervare'}")

    def af_carduri_dupa_puncte(self):
        for card_client in self.__card_client_service.ord_carduri_dupa_pct():
            print(card_client)

    def ui_sterge_in_cascada(self):
        try:
            id_film = input("Introduceti id-ul filmului "
                            "pentru care se va efectua stergerea in cascada: ")
            self.__film_service.sterge_in_cascada(id_film)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_sterge_rez_interval_zile(self):
        try:
            zi_start = int(input("Introduceti ziua de inceput: "))
            zi_stop = int(input("Introduceti ziua de sfarsit: "))
            self.__rezervare_service.sterge_rez_interval_zile(zi_start,
                                                              zi_stop)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_incrementare_puncte_interval_zile(self):
        try:
            zi_start = int(input("Introduceti ziua de inceput: "))
            zi_stop = int(input("Introduceti ziua de sfarsit: "))
            puncte = int(input("Introduceti valoarea "
                               "cu care se va efectua incrementarea: "))
            self.__card_client_service.incrementare_puncte_interval_zile(
                zi_start, zi_stop, puncte)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
