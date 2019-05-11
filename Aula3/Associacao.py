cidade = "londres"
listaDeCidades = ["madrid", "paris","londres","sao paulo"]

if(cidade in listaDeCidades):
    print("1 - A sua cidade foi encontrada na lista")
else:
    print("1 - A sua cidade nao foi encontrada na lista")

if(cidade not in listaDeCidades):
    print("2 - A sua cidade não foi encontrada na lista")
else:
    print("2 - A sua cidade foi encontrada na lista")

cidade = "nova iorque"

if (cidade in listaDeCidades):
    print("3 - A sua cidade foi encontrada na lista")
else:
    print("3 - A sua cidade nao foi encontrada na lista")