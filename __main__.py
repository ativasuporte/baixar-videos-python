#João Pedro
import os
import sys
import time
import pip
import subprocess
from subprocess import call

home = os.path.expanduser("~")
default_path = home + "\\Downloads\\youtube-dl"


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])



def main():
    #cabecinha
    os.system("cls")
    print("Verificando a instalação do youtube-dl...")

    try:
        install("youtube-dl")
    except:
        print("Houve um problema na instalação...")

    url = input("Url do vídeo: ")
    comando = "youtube-dl -o " + default_path + "\\%(title)s.%(ext)s " + url
    try:
        call(comando)
    except:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    print("Vídeo baixado em: " + default_path)

    while True:
        escolha = input("Deseja exibir a pasta de downloads? (y/n)")
        if escolha.lower() == "y":
            comando = "start explorer " + default_path
            os.system(comando)
            break
        if escolha.lower() == "n":
            break
        print("Opção inválida!")
        time.sleep(1)
        os.system("cls")

    time.sleep(2)
    os.system("cls")
    print("Valeu!")
    time.sleep(5)
    return

main()
