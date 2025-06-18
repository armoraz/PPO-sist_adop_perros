# Sistema de Adopción de Perros

Trabajo práctico para la materia *Programación Orientada a Objetos – Python*.  
El objetivo es implementar una plataforma básica de adopción de perros, respetando los principios de POO y buenas prácticas de desarrollo.

## Estructura del proyecto

El proyecto cuenta con dos implementaciones:

1. **Versión de consola (POO puro)** — permite gestionar el sistema por línea de comandos.  
2. **Versión web (Django)** — permite exponer la misma funcionalidad mediante una aplicación web.

### Estructura de carpetas

PPO-perros/
├── sistema_adopcion/ # Módulo con la lógica de negocio (modelo de dominio)
│ ├── init.py
│ ├── perro.py # Clase Perro
│ ├── usuario_adoptante.py # Clase UsuarioAdoptante
│ ├── sistema_adopcion.py # Clase SistemaAdopcion (controla la lógica general)
│ └── persistencia.py # Manejo de persistencia (guardado en archivos)
│
├── menu.py # Menú interactivo (interfaz de usuario para consola)
├── main.py # Punto de entrada principal de la versión de consola
├── registros.py # Funciones auxiliares de registro de perros y usuarios
├── testing/ # Scripts para generar datos de prueba
│
├── sistema_adopcion_web/ # Proyecto Django (versión web)
│ ├── adopciones/ # App Django con vistas, modelos y templates
│ └── sistema_adopcion_web/ # Configuración del proyecto Django
│
├──
└── README.md # Descripción general del proyecto
