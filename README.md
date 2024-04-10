CSPM - Create Compliance Standard
=================================

Este repositorio contiene scripts y funciones para trabajar con Custom Compliance Standards en CSPM - Prisma Cloud.

Archivos
--------

*   **config.py**: Contiene todas las variables, credenciales y URLs utilizadas en el proyecto.
    
*   **authenticate\_cspm.py**: Script que contiene la función para obtener el token de autenticación con el módulo de Cloud Security.
    
*   **list\_compliance\_standards.py**: Script que devuelve en formato JSON los estándares existentes. El JSON cuenta con las siguientes columnas:
    
    *   `id`: Identificador único del estándar de cumplimiento.
    *   `description`: Descripción del estándar de cumplimiento.
    *   `createdBy`: Usuario que creó el estándar de cumplimiento.
    *   `createdOn`: Fecha y hora de creación del estándar de cumplimiento en milisegundos desde la época UNIX.
    *   `lastModifiedBy`: Último usuario que modificó el estándar de cumplimiento.
    *   `lastModifiedOn`: Fecha y hora de la última modificación del estándar de cumplimiento en milisegundos desde la época UNIX.
    *   `systemDefault`: Indicador de si el estándar de cumplimiento es el predeterminado del sistema.
    *   `policiesAssignedCount`: Número de políticas asignadas al estándar de cumplimiento.
    *   `name`: Nombre del estándar de cumplimiento.
    *   `cloudType`: Tipos de nubes a las que se aplica el estándar de cumplimiento (por ejemplo, OCI, Alibaba Cloud, AWS, GCP, Azure).
*   **add\_compliance\_standard.py**: Script que contiene la función para la creación del Custom Compliance Standard.
    
*   **check\_compliance\_standard.py**: Script para validar la existencia del estándar y continuar o no con la creación.
    
*   **list\_compliance\_requirements.py**: Script que contiene la función para obtener los requerimientos existentes para un compliance ID. El JSON cuenta con las siguientes columnas:
    
    *   `id`: Identificador único del requisito de cumplimiento.
    *   `description`: Descripción del requisito de cumplimiento.
    *   `createdBy`: Usuario que creó el requisito de cumplimiento.
    *   `createdOn`: Fecha y hora de creación del requisito de cumplimiento (en milisegundos desde el 1 de enero de 1970).
    *   `lastModifiedBy`: Último usuario que modificó el requisito de cumplimiento.
    *   `lastModifiedOn`: Fecha y hora de la última modificación del requisito de cumplimiento (en milisegundos desde el 1 de enero de 1970).
    *   `systemDefault`: Indicador de si el requisito de cumplimiento es el predeterminado del sistema.
    *   `policiesAssignedCount`: Número de políticas asignadas al requisito de cumplimiento.
    *   `requirementId`: Identificador único del requisito (posiblemente un valor interno).
    *   `name`: Nombre del requisito de cumplimiento.
    *   `viewOrder`: Orden de visualización del requisito de cumplimiento.

*   **list\_compliance\_requirements.py**: Script para crear los requirements ID