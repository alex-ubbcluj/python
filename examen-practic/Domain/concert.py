from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class Concert(Entity):
    nume: str
    locatie: str
    capacitate_locatie: int
    id_artist: str
