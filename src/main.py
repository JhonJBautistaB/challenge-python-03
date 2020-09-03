# Resolve the problem!!
import re
import os


def run():
    # Start coding here
    regular_exp = '[a-z]'
    ruta_actual = os.getcwd()
    print(ruta_actual)
    with open('src/encoded.txt', 'r', encoding='utf-8') as f:
        resultado = re.findall(regular_exp, f.read())
        mensaje_oculto = ''.join(resultado)
    print(mensaje_oculto)

if __name__ == '__main__':
    run()
