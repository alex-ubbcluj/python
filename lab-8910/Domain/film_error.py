from dataclasses import dataclass


@dataclass
class FilmError(Exception):
    mesaje: list[str]

    def __str__(self):
        return f"FilmError: {self.mesaje}"
