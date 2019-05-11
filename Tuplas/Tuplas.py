import timeit

tuplaTeste = timeit.timeit(stmt="(1,2,3,4,5)",number=100000)
listaTeste = timeit.timeit(stmt="[1,2,3,4,5]",number=100000)

print("Tempo total para criar a tupla: ", tuplaTeste)
print("Tempo total para criar a lista: ", listaTeste)

tupla1 = 1,2,3,4
tupla2 = 2,
print(type(tupla1))
print(type(tupla2))

