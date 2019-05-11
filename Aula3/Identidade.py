y = 20
x = 20

if (y is x):
    print("1 - x e y tem a mesma identidade")

if(id(y) == id(x)):
    print("2 - x e y tem a mesma identidade")

x = 25

if (y is x):
    print("3 - x e y tem a mesma identidade")
else:
    print("3 - x e y nao tem a mesma identidade")

if ( y is not x):
    print("4 - y nao tem a mesma identidade que x")