numero = 100

if(numero):
    print("1 - numero, tem uma expressao verdadeira")
    print(numero)
    print()

numero2 = 0

if(numero2):
    print("2 - numero2, tem uma expressao verdadeira")
    print(numero2)
    print()

numero3 = 478

if(numero3):
    print("3 - numero3, tem uma expressao verdadeira")
    print(numero3)
else:
    print("3 - numero3, tem uma expressao falsa")
    print(numero3)

print()

numero4 = 0

if(numero4):
    print("4 - numero4, tem uma expressao verdadeira")
    print(numero4)
else:
    print("4 - numero4 tem uma expressao falsa")
    print(numero4)

print()

numero5 = 100000

if(numero5 > 2000):
    print("expressao e menor que 2000")
    if(numero5 == 2500):
        print("expressao e igual a 2500")
    elif(numero5 > 50000):
        print("expressao e maior que 5000")

else:
    print("nao encontrei nenhuma expressao verdadeira")

print("adeus")