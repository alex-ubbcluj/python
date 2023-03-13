# Laborator 11 - Săptămâna 11

Scrieți un program cu meniu de tip consolă. Programul va reține datele într-un fișier. Vor fi suportate
următoarele funcționalități:
1. [1p] Adăugare client: id, nume (string nenul), CNP (13 caractere), sold initial (pozitiv).
Important:
După fiecare adăugare se vor afișa toate obiectele pentru entitatea Client.
2. [2p] Adăugare tranzacție: id, id_client_sursa, id_client_destinatie (trebuie să existe și să fie
distincte), valoare. La adaugarea unei tranzacții trebuie verificat dacă soldul clientului sursa are
destule fonduri, iar soldurile clienților trebuie actualizate în cazul in care tranzacția este
permisă.
Important:
După fiecare adăugare se vor afișa toate obiectele pentru entitatea Tranzactie.
3. [2p] Afișarea clienților ordonați descrescător după numărul de vocale (a, e, i, o, u) din nume. Se
va afișa și acest număr.
4. [2p] Afișarea tuturor tranzacțiilor care sunt considerate periculoase. O tranzactie este considerată periculoasă dacă are o valoare mai mare de 15000. Se vor afișa și numele și CNP-
urile clienților implicați in astfel de tranzacții.

5. [3p] Export istoric tranzactii in format JSON: se citește un CNP de la tastatura si se construiește
istoricul clientului căutat astfel: se creează un fișier JSON cu un obiect în care cheile sunt id-urile
tranzacțiilor, iar valoarea unei chei este un obiect de tip tuplu care contine următoarele
informații: “trimitere” dacă clientul căutat este sursa / “primire” dacă clientul căutat este
destinatar, numele celuilalt client implicat, valoare.
Exemplu de export valid:

{

“1” : (“trimitere”, “Mihai”, 25.0),

“7”: (“primire”, “Florin”, 45.0),

“25” : (“trimitere”, “Andreea”, 25.0)

}
