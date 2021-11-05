#João Pedro
import os
import sys
import time

home = os.path.expanduser("~")
default_path = home + "\\Downloads\\youtube-dl"


def main():
    #cabecinha
    os.system("cls")

    print("Verificando a instalação do youtube-dl...")

    os.system("pip install --upgrade youtube-dl")

    os.system("cls")

    url = input("Url do vídeo: ")

    comando = "youtube-dl -o " + default_path + "\\%(title)s.%(ext)s " + url

    os.system(comando)

    os.system("cls")

    print("Vídeo baixado em: " + default_path)

    while True:

        escolha = input("Deseja exibir a pasta de downloads? (y/n)")

        if escolha.lower() == "y":
            comando = "start explorer.exe " + default_path
            os.system(comando)
            break
        if escolha.lower() == "n":
            break
        print("Opção inválida!")
        time.sleep(1)
        os.system("cls")

    time.sleep(2)
    os.system("cls")
    print("Obrigado por utilizar meu script!")
    return


main()
