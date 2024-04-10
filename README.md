# CSPM - Create Compliance Standard
Repositorio para la creación de un Custom Compliance Standard en CSPM - Prisma Cloud

config.py contine todas las variables, credenciales y URLs utilizadas en el proyecto

authentica_cspm.py es un Script que contiene la función para obtener el token de autenticación con el módulo de Cloud Security.

list_compliance_standards.py es un Script que devuelve en formato JSON los estándares existentes. El json cuenta con los siguientas columnas:

id: Identificador único del estándar de cumplimiento.
description: Descripción del estándar de cumplimiento.
createdBy: Usuario que creó el estándar de cumplimiento.
createdOn: Fecha y hora de creación del estándar de cumplimiento en milisegundos desde la época UNIX.
lastModifiedBy: Último usuario que modificó el estándar de cumplimiento.
lastModifiedOn: Fecha y hora de la última modificación del estándar de cumplimiento en milisegundos desde la época UNIX.
systemDefault: Indicador de si el estándar de cumplimiento es el predeterminado del sistema.
policiesAssignedCount: Número de políticas asignadas al estándar de cumplimiento.
name: Nombre del estándar de cumplimiento.
cloudType: Tipos de nubes a las que se aplica el estándar de cumplimiento (por ejemplo, OCI, Alibaba Cloud, AWS, GCP, Azure).