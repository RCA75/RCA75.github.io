# Autor: Reinaldo Carocca

#Defino función que abre el archivo index.html en modo escritura(w)
def export(var):
    with open('index.html', 'w') as f:
        f.write(var)

#Probando sentencia export
if __name__ == '__main__':
    prueba = "hola mundo"
    export(prueba)
    