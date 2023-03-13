# Laboratoarele 8, 9 și 10 - Săptămânile 8, 9 și 12
**Saptămâna 10 este liberă sau fără preluări de teme. Săptămâna 11 este cea cu testul 2. Ultima iterație se va preda în săptămâna 12.**


0. Teste și specificații la toate iterațiile.
1. **Iterația 1** 
   - Toate CRUD-urile, minim încă o funcționalitate diferită de CRUD. Cu validări, arhitectură stratificată cu toate elementele descrise la curs. Salvarea datelor în fișiere.  
   - Fără warning-uri PEP 8. Acestea vor fi afișate pe github când faceți commit. Nota maximă dacă există warning-uri PEP 8 este `9`.
2. **Iterația 2**
   - Toate funcționalitățile în afară de Undo+Redo. 
   - Repository generic, clase proprii de excepții. 
   - Folosirea type hinting, ABC, protocol.
   - Fără warning-uri PEP 8. Acestea vor fi afișate pe github când faceți commit. Nota maximă dacă există warning-uri PEP 8 este `8`.
3. **Iterația 3**
   - Implementat Undo+Redo eficient.
   - Refactorizat toate funcționalitățile posibile folosind `map`, `filter`, `list comprehensions`, `reduce`, `zip`.
   - Refactorizat minim o metodă folosind recursivitate.
   - Refactorizat minim două metode folosind lambda.
   - Implementat și folosit o funcție proprie de sortare care să aibă aceeași interfață cu funcția `sorted` din Python. 
   - Fără warning-uri PEP 8. Acestea vor fi afișate pe github când faceți commit. Nota maximă dacă există warning-uri PEP 8 este `7`.
4. **Bonusuri**: se acordă ca note peste 10.
   - Documentație Agile, conform https://asana.com/guide/examples/project-management/asana-agile. Se pot folosi și alte tool-uri atâta timp cât se păstrează aceleași concepte. Maxim `5p` / iterație.
   - Scrierea aplicației în Django cu baze de date, păstrând pe cât posibil organizarea de la curs. Maxim `7p` / iterație. 
   - Scrierea aplicației în Angular sau React cu Material sau Bootstrap, păstrând pe cât posibil organizarea de la curs. Maxim `10p` / iterație. 
   - Scrierea aplicației ca REST API în Django cu baze de date și în Angular sau React cu Material sau Bootstrap ca frontend. Nota `10` pe laborator și pe examenul practic. Este necesar să arătați progresul pe parcursul iterațiilor dacă alegeți acest bonus. Se pot acorda bonusuri parțiale proporționale cu cele de mai sus pentru aplicații funcționale, dar care nu respectă principiile de dezvoltare ale unor astfel de aplicații.
   

**Căutare full text** înseamnă că stringul introdus de utilizator se caută în toate câmpurile tuturor entităților menționate. Se returnează toate entitățile în ale căror câmpuri se găsește stringul. Se pot returna entități de tipuri diferite.


2. **Cinema**   
    2.1. CRUD film: id, titlu, an apariție, preț bilet, în program. Prețul să fie strict pozitiv.  
    2.2. CRUD card client: id, nume, prenume, CNP, data nașterii (`dd.mm.yyyy`), data înregistrării (`d.mm.yyyy`), puncte acumulate. CNP-ul trebuie să fie unic.  
    2.3. CRUD rezervare: id, id_film, id_card_client (poate fi nul), data și ora. Clientul acumulează pe card `10%` (parte întreagă) din prețul filmului. Se tipărește numărul total de puncte de pe card. Rezervarea se poate face doar dacă filmul este încă în program.  
    2.4. Căutare filme și clienți. Căutare full text.  
    2.5. Afișarea tuturor rezervărilor dintr-un interval de ore dat, indiferent de zi.  
    2.6. Afișarea filmelor ordonate descrescător după numărul de rezervări.  
    2.7. Afișarea cardurilor client ordonate descrescător după numărul de puncte de pe card.  
    2.8. Ștergerea tuturor rezervărilor dintr-un anumit interval de zile.  
    2.9. Incrementarea cu o valoare dată a punctelor de pe toate cardurile a căror zi de naștere se află într-un interval dat.   
