import sys

def main():
    try:
        x = 5/0
    except ValueError:
        print("Apanhei um valor errado")

    except:
        print(f'Ocorreu um erro inesperado: {sys.exc_info()[1]}')
    else:
        print(x)
        print("A sua operacao foi concluida com sucesso")


if __name__ == '__main__': main()