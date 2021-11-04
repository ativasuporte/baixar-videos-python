#João Pedro
import os
import sys

home = os.path.expanduser("~")
default_path = home + "\\Downloads\\youtube-dl"


def main():

    print("Verificando a instalação do youtube-dl...")

    os.system("pip install --upgrade youtube-dl")

    url = input("Url do vídeo: ")

    os.system("youtube-dl " + url)

    print("Vídeo baixado em: " + default_path)


main()
