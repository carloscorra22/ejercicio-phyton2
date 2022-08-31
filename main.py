def cuestionador(numero):
    if (numero%2!=0):
        return "es primo"
    else:
        return "no es primo"

resultado= cuestionador(2)

print("el numero", resultado)