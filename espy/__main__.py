import sys
import os
from .transpiler import transpilar

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'run':
        print('Uso: espy run archivo.espy')
        sys.exit(1)
    archivo = sys.argv[2]
    if not os.path.exists(archivo):
        print(f'Archivo no encontrado: {archivo}')
        sys.exit(1)
    with open(archivo, 'r', encoding='utf-8') as f:
        codigo_espanol = f.read()
    codigo_python = transpilar(codigo_espanol)
    # Definir __name__ como '__main__' para compatibilidad
    globals()['__name__'] = '__main__'
    # Ejecutar el código Python resultante
    exec(codigo_python, globals())

if __name__ == '__main__':
    main()
