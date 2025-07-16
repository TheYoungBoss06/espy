# espy-lang

> **¡Programa en Python usando sintaxis y palabras clave en español!**

espy-lang es un transpilador que te permite escribir código Python completamente en español y ejecutarlo en cualquier sistema, facilitando el aprendizaje, la enseñanza y la programación para hispanohablantes.

---

## 🚀 Instalación

### Desde PyPI (recomendado)

```sh
pip install espy-lang
```

### Desde GitHub (última versión)

```sh
pip install git+https://github.com/TheYoungBoss06/espy-lang.git
```

### Desde el código fuente (desarrolladores)

```sh
git clone https://github.com/TheYoungBoss06/espy-lang.git
cd espy-lang
pip install -e .
```

---

## 📝 Uso rápido

1. Escribe tu código en español en un archivo `.espy`:

```python
clase Calculadora:
    funcion sumar(yo, x, y):
        retornar x + y

c = Calculadora()
imprimir(c.sumar(2, 3))
```

2. Ejecuta tu archivo:

```sh
espy-lang run archivo.espy
```

---

## 🧩 Características principales

- Palabras clave, operadores, tipos, excepciones y métodos mágicos en español
- Compatibilidad con la mayoría de la sintaxis de Python
- Soporte para módulos estándar y anotaciones de tipo
- Decoradores y async/await en español
- Fácil de instalar y usar

---

## 📚 Tabla de palabras clave soportadas

| Español      | Python      |
|--------------|-------------|
| funcion      | def         |
| clase        | class       |
| retornar     | return      |
| si           | if          |
| sino_si      | elif        |
| sino         | else        |
| para         | for         |
| mientras     | while       |
| romper       | break       |
| continuar    | continue    |
| pasar        | pass        |
| importar     | import      |
| desde        | from        |
| como         | as          |
| intentar     | try         |
| excepto      | except      |
| finalmente   | finally     |
| lanzar       | raise       |
| con          | with        |
| lambda       | lambda      |
| producir     | yield       |
| global       | global      |
| no_local     | nonlocal    |
| afirmar      | assert      |
| eliminar     | del         |
| no           | not         |
| y            | and         |
| o            | or          |
| en           | in          |
| es           | is          |
| Verdadero    | True        |
| Falso        | False       |
| Nulo         | None        |
| imprimir     | print       |
| entrada      | input       |
| lista        | list        |
| diccionario  | dict        |
| conjunto     | set         |
| tupla        | tuple       |
| rango        | range       |
| longitud     | len         |
| ...          | ...         |

---

## 💡 Ejemplo avanzado

```python
clase Persona:
    funcion __inicializar__(yo, nombre):
        yo.nombre = nombre

    funcion __texto__(yo):
        retornar f"Persona: {yo.nombre}"

p = Persona("Ana")
imprimir(p)
```

---

## 🤝 Contribuir

¿Tienes ideas, sugerencias o quieres ayudar a mejorar espy-lang?

- Haz un fork y envía un pull request
- Abre un issue para reportar bugs o proponer mejoras
- ¡Toda contribución es bienvenida!

---

## 📬 Contacto

- Autor: Tu Nombre
- Email: tu.email@ejemplo.com
- GitHub: [https://github.com/TheYoungBoss06/espy-lang](https://github.com/TheYoungBoss06/espy-lang)

---

## ⚖️ Licencia

MIT License. Consulta el archivo LICENSE para más detalles.