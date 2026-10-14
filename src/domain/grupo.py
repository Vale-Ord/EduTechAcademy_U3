from dataclasses import dataclass, field
from typing import List
from .value_objects import Cupo

@dataclass
class AsignacionInstructor:
    instructor_id: str
    fecha_inicio: str
    fecha_fin: str = None

@dataclass
class Grupo:
    id: str
    curso_id: str
    instructor_id: str
    capacidad_maxima: int
    estado: str = "Programado"
    cupo: Cupo = field(init=False)
    asignaciones_instructor: List[AsignacionInstructor] = field(default_factory=list)
    
    def __post_init__(self):
        self.cupo = Cupo(self.capacidad_maxima, 0)
        self.asignaciones_instructor.append(
            AsignacionInstructor(self.instructor_id, "2026-01-01")
        )
    
    def admite_inscripciones(self) -> bool:
        return self.estado in ["Programado", "En curso"]
    
    def ocupar_lugar(self) -> None:
        if not self.admite_inscripciones():
            raise ValueError(f"El grupo está {self.estado} y no admite inscripciones")
        self.cupo = self.cupo.ocupar()
    
    def liberar_lugar(self) -> None:
        self.cupo = self.cupo.liberar()
    
    def es_instructor(self, instructor_id: str) -> bool:
        return self.instructor_id == instructor_id
    
    def sustituir_instructor(self, nuevo_instructor_id: str, fecha: str) -> None:
        for asignacion in self.asignaciones_instructor:
            if asignacion.fecha_fin is None:
                asignacion.fecha_fin = fecha
        self.asignaciones_instructor.append(
            AsignacionInstructor(nuevo_instructor_id, fecha)
        )
        self.instructor_id = nuevo_instructor_id
    
    def cancelar(self) -> None:
        if self.estado == "Finalizado":
            raise ValueError("No se puede cancelar un grupo finalizado")
        self.estado = "Cancelado"
    
    def finalizar(self) -> None:
        if self.estado == "Cancelado":
            raise ValueError("No se puede finalizar un grupo cancelado")
        self.estado = "Finalizado"