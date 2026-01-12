## 🚁 Drone Maestría

Drone Maestría es un proyecto desarrollado en Python para la maestría que implementa algoritmos clave relacionados con el procesamiento de datos y/o planificación de rutas para drones. El repositorio contiene una aplicación principal (main.py) y módulos auxiliares para algoritmos específicos como interpolación y cálculo de opacidad.

## 🧠 Descripción

Este proyecto forma parte de un trabajo de investigación en maestría orientado al desarrollo de soluciones computacionales aplicadas al comportamiento y procesamiento de datos de drones. Entre las funcionalidades destacadas se encuentran:
## 📝 Funcionalidades principales
## 🧮 Algoritmo de interpolación

El módulo está pensado para:
📌Redimensionar las imágenes del dataset correspondiente para que el modelo de inteligencia artificial pueda hacer el entrenamiento de mejor manera.

## 🎯 Algoritmo de opacidad
Este módulo puede:
📍Agregar opacidad a las imágenes para hacer parecer que en las imágenes es de noche o este nublado. Pero lo ideal es tomar las imágenes en varias partes del día cuando haya sol, este nublado, de noche, etc para que así el modelo tenga un mejor entrenamiento y por consiguiente una mejor predicción.

## 🛠️ Script principal (main.py)
Integra los módulos de reconocimiento y rutas autónomas, sirve como punto de entrada para ejecutar el conjunto de algoritmos y/o pruebas.

## 📁 Estructura del repositorio

```text
drone_maestria/
├── Algoritmo_de_interpolacion.py   # Implementación de interpolación
├── Algoritmo_de_opacidad.py         # Cálculo de opacidad / ponderaciones
├── main.py                          # Script principal de ejecución
├── .gitignore
└── README.md                        # Este archivo
```

## 🧩 Requisitos

Este proyecto está escrito en Python 3. Asegúrate de tenerlo instalado (preferentemente >= 3.7).

## 🚀 Uso
Ejecutar el proyecto

Dentro del directorio del proyecto:

python main.py

## 🧪 Pruebas
Las pruebas fueron realizadas dentro de la universidad y con imágenes del objeto ya que el dron no cuenta con las suficientes especificaciones fisicas para realizar un vuelo tan alto y no cuenta con una cámara en la parte baja del dron para hacer el reconocimiento ideal.

## 🧑‍💻 Contribuciones
Este repositorio es parte de un proyecto académico.
