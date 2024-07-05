#!/usr/bin/env python3

import subprocess
from time import sleep

def teste():
    with open('data', 'r') as datafile:
        for element in datafile:
            package = element.strip()  

            command = f"sudo apt install {package} -y" 

            try:
                print(f"Instalando aplicativo {package}")
                sleep(2)
                result = subprocess.run(command, capture_output=True, shell=True, text=True)
                if result.returncode == 0:
                    print(f"{package} instalado com sucesso!")
                else:
                    print(f"Erro ao instalar {package}:")
                    print(result.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar comando para {package}: {e}")
            except KeyboardInterrupt:
                print("Interrupção detectada. Saindo...")
                break
            except Exception as e:
                print(f"Erro inesperado ao executar comando para {package}: {e}")

teste()
