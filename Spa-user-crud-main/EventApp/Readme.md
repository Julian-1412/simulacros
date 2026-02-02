# 📅 EventMaster SPA - Sistema de Gestión de Eventos

Este proyecto es una Single Page Application (SPA) diseñada para la gestión integral de eventos empresariales. Permite la administración de usuarios, la creación de eventos con control de aforo y el seguimiento de inscripciones en tiempo real.

---

## 🚀 Características Principales

### 🔐 Autenticación y Roles
- **Login y Registro:** Sistema de acceso con persistencia en `Local Storage`.
- **Roles Definidos:** - **Admin:** Control total sobre usuarios y eventos.
  - **User:** Acceso a catálogo e inscripciones personales.

### 🛠️ Funcionalidades de Administrador
- **Dashboard Analítico:** Visualización de métricas (Total de ventas, cupos globales, % de ocupación).
- **Gestión de Usuarios:** CRUD completo para administrar cuentas.
- **Gestión de Eventos:** Creación, edición y eliminación de eventos con asignación de capacidad máxima.

### 🎟️ Funcionalidades de Usuario
- **Catálogo de Eventos:** Visualización de eventos disponibles con validación de cupos.
- **Inscripciones Inteligentes:** Registro con un solo clic (deshabilitado si el evento está lleno).
- **Mis Eventos:** Panel personal para gestionar y cancelar asistencias.

---

## 🛠️ Tecnologías Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (ES6+).
- **Arquitectura:** Single Page Application (SPA) modular.
- **Persistencia:** JSON Server (Base de Datos simulada) y Local Storage.
- **Comunicación:** API Fetch con manejo de errores asíncronos (`try...catch`).

---

## 📦 Estructura del Proyecto



```text
src/
├── assets/         # Recursos estáticos
├── helpers/        # Validadores de rutas y autenticación
├── services/       # Lógica de comunicación con la API (Fetch)
├── styles/         # Estilos modulares (CSS)
├── utils/          # Orquestadores de lógica de cada vista
├── views/          # Plantillas HTML (Templates)
└── main.js         # Punto de entrada y Router


🔧 Instalación y EjecuciónClonar el repositorio:Bashgit clone [https://github.com/tu-usuario/nombre-del-proyecto.git](https://github.com/tu-usuario/nombre-del-proyecto.git)
Instalar dependencias:Bashnpm install
Ejecutar la Base de Datos (JSON Server):(Asegúrate de tener json-server instalado globalmente o vía npx)Bashnpx json-server --watch db.json --port 3000
Ejecutar el Proyecto:Bashnpm run dev
📸 Capturas de PantallaDashboard AdminCatálogo de Usuario👨‍💻 Datos del CoderNombre: [Tu Nombre Completo]Cohorte: [Nombre de tu curso/cohorte]Proyecto: Prueba Técnica - Caso de Uso Empresarial: Gestión de Eventos.Nota: Este proyecto ha sido desarrollado siguiendo principios de código limpio, modularización y manejo de errores para garantizar una experiencia de usuario fluida y segura.
---

### Consejos para la Sustentación Individual:
1.  **Enfatiza la Modularización:** Explica por qué separaste los `services` de la `logic`. Di que es para que el código sea testeable y fácil de mantener.
2.  **Explica el Flujo de Datos:** Menciona cómo `Maps()` valida si el usuario tiene permiso (Admin/User) antes de mostrar una vista.
3.  **Manejo de Cupos:** Cuando te pregunten por la capacidad, resalta que haces un `filter` en los registros para comparar contra el `capacity` del evento antes de permitir el botón de "Inscribirme".

**¿Hay algo más que necesites pulir antes de tu entrega? ¡Mucho éxito en la sustentació