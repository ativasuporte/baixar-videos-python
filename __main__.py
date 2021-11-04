#João Pedro
import os
import sys

home = os.path.expanduser("~")
default_path = home + "\\Downloads\\youtube-dl"


def main():
    #cabecinha

    print("Verificando a instalação do youtube-dl...")

    os.system("pip install --upgrade youtube-dl")

    url = input("Url do vídeo: ")

    comando = "youtube-dl -o " + default_path + "\\%(title)s.%(ext)s " + url

    os.system(comando)

    print("Vídeo baixado em: " + default_path)


main()
