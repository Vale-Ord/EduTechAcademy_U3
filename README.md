# EduTechAcademy – Diseño Arquitectural del Sistema

**Materia:** Componentes de Lógica del Negocio  
**Unidad:** 3 – Diseño Arquitectural del Sistema  
**Profesor:** Miguel Ángel Gómez Marroquín  
**Módulo Netacad:** 3  
**Fecha:** 13/10/2026

---

## 👥 Integrantes del equipo

| Nombre | Matrícula |
| :--- | :--- |
| Valeria Ordaz Garcia | 2169894 |
| Luis José Mendoza Serrano | 2223173 |
| Omar Alejandro Salazar Castro | 2226576 |

---

## Descripción del proyecto

Prototipo de arquitectura de software para **EduTechAcademy**, una organización dedicada a ofrecer cursos de capacitación y educación continua en modalidades presencial y en línea.

Este proyecto convierte el análisis de negocio de la Unidad 2 (BRD, User Stories, BPMN, glosario) en una arquitectura de software basada en **Domain-Driven Design (DDD)**.

El sistema cubre el proceso completo:
- Inscripción de estudiantes
- Control de cupos
- Registro de pagos
- Impartición de cursos
- Registro de asistencia y evaluaciones
- Validación de criterios de certificación
- Emisión de certificados

---

## Arquitectura implementada

### Patrón de lógica de negocio
- **Domain Model** (ADR-001) con **Service Layer** como capa de coordinación.

### Elementos del dominio
- **7 Aggregates**: Curso, Grupo, Instructor, Estudiante, Inscripción, SolicitudCapacitación, ClienteEmpresarial.
- **Value Objects**: Calificación, PorcentajeAsistencia, Cupo, Precio, Modalidad, EstadoGrupo, EstadoInscripción, EstadoPago, EstadoCertificación, entre otros.
- **Entidades internas**: Pago, Asistencia, Evaluación, CambioDeGrupo, Certificación, AsignaciónInstructor.
- **Domain Service**: `PoliticalInscripcion` (verificación de requisitos de inscripción).
- **Domain Events**: InscripciónRegistrada, PagoRecibido, AsistenciaRegistrada, EvaluaciónRegistrada, EstudianteElegible, EstudianteNoElegible, CertificadoEmitido, GrupoCambiado, InstructorSustituido, GrupoCancelado.

### Reglas de negocio clave
- **RB-02**: Control de cupo (los ocupados nunca superan la capacidad).
- **RB-03**: La inscripción se confirma solo con el pago.
- **RB-06**: Asistencia mínima del 80% para certificar.
- **RB-07**: Calificación mínima de 70/100 para aprobar.
- **RB-08**: Certificación requiere ambos criterios (70/100 y 80%).
- **RB-09**: Cambio de grupo con autorización y trazabilidad.
- **RB-11**: Sustitución de instructor conservando historial.
- **RB-14**: Permisos por rol verificados en el Service Layer.

### Aplicación de CQRS
- **Commands**: Operaciones que modifican estado (`inscribir`, `cambiarGrupo`, `registrarPago`).
- **Queries**: Consultas de solo lectura directas a repositorios (`consultarCursosDisponibles`, `obtenerReporte`).
- Ver ADR-008 para más detalle.

### Persistencia
- **Repository por Aggregate** (7 interfaces).
- **Unit of Work** con límites transaccionales documentados.
- Implementación en memoria (prototipo).

---

## Estructura del proyecto
EduTechAcademy_U3/
├── src/
│ ├── domain/ # Reglas de negocio (Aggregates, Value Objects, entidades)
│ │ ├── curso.py
│ │ ├── grupo.py
│ │ ├── estudiante.py
│ │ ├── inscripcion.py
│ │ └── value_objects.py
│ ├── application/ # Service Layer (Application Services)
│ │ ├── inscripcion_service.py
│ │ ├── certificacion_service.py
│ │ └── asistencia_service.py
│ └── infrastructure/ # Repositorios en memoria y Unit of Work
│ ├── repositorios_memoria.py
│ └── unit_of_work.py
├── tests/ # Pruebas automatizadas (unittest)
│ ├── test_inscripcion.py
│ ├── test_certificacion.py
│ ├── test_cupo.py
│ └── evidencias/ # Capturas y logs de ejecución
│ ├── ejecucion-pruebas.png
│ └── ejecucion-pruebas.txt
└── README.md

text

---

## Cómo ejecutar las pruebas

Desde la raíz del proyecto, abre una terminal y ejecuta:

```bash
python -m unittest discover -s tests -v
Resultado esperado:
text
Ran 15 tests in 0.003s

OK
Las pruebas cubren:

Value Objects: Cupo, Calificación, PorcentajeAsistencia.

Inscripción: Éxito, sin cupo, confirmación por pago, monto incorrecto.

Certificación: Estudiante elegible, no elegible por calificación, no elegible por asistencia, grupo no finalizado.

Evidencias de ejecución
Las evidencias se encuentran en la carpeta tests/evidencias/:

ejecucion-pruebas.png: Captura de pantalla de las 15 pruebas aprobadas.

ejecucion-pruebas.txt: Log completo de la ejecución.

Documentación adicional
El proyecto incluye los siguientes documentos de arquitectura:

Informe de arquitectura: Análisis completo del diseño (BRD, patrones, mapa de dominio, Service Layer, Repository, Unit of Work, CQRS, SOLID, ADR).

ADRs (Architecture Decision Records): 11 decisiones documentadas con contexto, alternativas, decisión y consecuencias.

Matriz de trazabilidad: Relación entre BN, US, CU, RB, componentes y ADRs.

Bitácora de IA: Registro del uso de inteligencia artificial como copiloto.

Diagramas UML: Mapa de dominio, diagrama de clases y diagramas de secuencia 

Tecnologías utilizadas
Python 3.13

unittest (biblioteca estándar de Python)

Visual Studio Code (editor)

Git y GitHub (control de versiones)

Referencias bibliográficas

Evans, E. (2003). Domain-driven design: Tackling complexity in the heart of software. Addison-Wesley.

Fowler, M. (2002). Patterns of enterprise application architecture. Addison-Wesley.

Nygard, M. (2011). Documenting architecture decisions. Cognitect.

Vernon, V. (2013). Implementing domain-driven design. Addison-Wesley.

Repositorio
