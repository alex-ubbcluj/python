from Domain.client import Client


class ClientValidator:
    def validate(self, client: Client):
        erori = []
        if client.nume == "":
            erori.append("Numele clientului nu poate fi gol!")
        if len(client.cnp) != 13:
            erori.append("CNP-ul trebuie sa aiba 13 caractere!")
        if client.sold_initial < 0:
            erori.append("Soldul initial trebuie sa fie pozitiv!")
        if erori:
            raise ValueError(erori)
