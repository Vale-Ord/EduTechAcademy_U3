from dataclasses import dataclass
from typing import List

@dataclass
class Curso:
    id: str
    nombre: str
    modalidad: str
    precio: float
    requisitos: List[str]
    
    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if self.modalidad not in ["Presencial", "En línea"]:
            raise ValueError("Modalidad debe ser Presencial o En línea")