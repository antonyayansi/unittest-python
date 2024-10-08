
## 📐 Calculador del Máximo Común Divisor (MCD)
Este repositorio contiene un script en Python que implementa una función para calcular el Máximo Común Divisor (MCD) entre cuatro números. Utiliza la técnica del algoritmo de Euclides para dos números, extendiéndolo a cuatro, y cuenta con un conjunto de pruebas automatizadas para validar su funcionamiento.

#### 🧑‍💻 Funciones
```python
mcd(a, b)
```
Calcula el MCD entre dos números utilizando el algoritmo de Euclides.
```python
mcd_4(a, b, c, d)
```

Calcula el MCD de cuatro números aprovechando la función mcd(a, b) y combinándola en tres pasos.

#### 🧪 Pruebas Unitarias
Este proyecto utiliza unittest para validar el comportamiento de la función mcd_4.

#### Prueba:
- Comprobación de que el MCD de 3, 12, 24 y 36 es igual a 3.
#### 🚀 ¿Cómo usar este proyecto?
Clona el repositorio:
```bash
git clone https://github.com/antonyayansi/unittest-python
```
Navega hasta la carpeta del proyecto:
```bash
cd unittest-python
```
Ejecuta las pruebas:
```bash
python3 test_operaciones.py
```
##### 📂 Estructura del proyecto
```plaintext
Copiar código
📦 unittest-python
 ┣ 📜 test-mcd.py  # Pruebas unitarias
 ┗ 📜 README.md    # Este archivo
```
#### 🛠️ Tecnologías utilizadas
-  Python 🐍
- Unittest 🧪
