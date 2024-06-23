import subprocess
import sys
import os
import argparse
import json


class ConfigurePackage:
    def __init__(self):
        self.__PackagesInstall= { 
                               "apt": None,"snap": None,
                                "dpkg": None,"aptitude": None,
                                "synaptic": None,"flatpak": None 
                                }
        
    """ Verificando se o package management esta instalado, e qual package management esta instalado"""
    def PackageManagementConfigure(self) -> dict:
        for package, v in self.__PackagesInstall.items():
            command = f"dpkg -s {package} | grep -i '^status:\\|^version:\\|^package:'"
            
            try:
                output = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
                if output.returncode == 0:
                    self.__PackagesInstall[package] = True  
                else:
                    self.__PackagesInstall[package] = False  
            except subprocess.CalledProcessError:
                self.__PackagesInstall[package] = False
        return self.__PackagesInstall
    
    """ Removendo gerenciadores de pacote que não estão instalados,
    dando preferencia aos que ja tem na maquina ( devolve uma lista com os gerenciadores que ja estão instalados.)"""
    
    def RemoveFalseKeys(self,dictionary:dict) -> list: 
        true_keys = []
        for key, value in list(dictionary.items()):
            if not value:
                del dictionary[key]
            else:
                true_keys.append(key)
        return true_keys
    
    def UsingPackageManagement(self,TrueKeys):
        CountPackageInstalled = len(TrueKeys)
        for keys, values in enumerate(TrueKeys):
            setattr(self,keys,values)
            print(keys,values)
        
    
    

        



a = ConfigurePackage()
b = a.UsingPackageManagement(TrueKeys=["snap","apt"])
print(b)
