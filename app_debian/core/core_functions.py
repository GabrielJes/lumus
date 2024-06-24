import subprocess

class CoreFunctionManager:
    """
Class for managing package-related functions and direct OS commands,
intended for non-committal package reinstalls, system testing, and 
environment verification.

This class provides methods to execute direct system commands and manage 
packages without permanently altering the system state. It is specifically
designed for scenarios where testing new systems or verifying environments
is required without making lasting changes to installed packages.

Usage:
    This class should be instantiated only in non-production environments 
    or during testing phases where package reinstallations are necessary 
    for experimentation or system validation.

Example:
    >>> from package_manager import NonCommittalPackageManager
    >>> pm = NonCommittalPackageManager()
    >>> pm.install_package('example-package')
    >>> pm.execute_command('apt-get update')

Attributes:
    None

Methods:
    - install_package(package_name): Installs a package without permanent changes.
    - uninstall_package(package_name): Uninstalls a package without permanent changes.
    - execute_command(command): Executes a system command without permanent changes.

Notes:
    This class does not persist changes to the system. It is suitable for 
    temporary package management and system command execution during testing 
    and evaluation phases.

Warning:
    Do not use this class in production environments or where permanent 
    modifications to the system are required. It is intended solely for 
    non-committal operations during system and environment testing.
"""
    @staticmethod
    def CheckPackageManagersInstalled(self) -> dict:
        self.__PackagesInstall= { 
                                "apt": None,"snap": None,"aptitude": None,
                                 "synaptic": None,"flatpak": None 
                                 }
        for package, v in self.__PackagesInstall.items():
            command = f"dpkg -s {package} | grep -i '^status:\\|^version:\\|^package:'"
            try:
                output = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
                if output.returncode == 0:
                    self.__PackagesInstall[package] = True  
            except Exception:
                self.__PackagesInstall[package] = False
        return self.__PackagesInstall 

    @staticmethod
    def APTpackageManagement(packageManagement,package) -> str:
        if packageManagement == 'apt':
            command = f"sudo apt install {package}"
            try:
                output = subprocess.run(command,shell=True,capture_output=True)
                return output.returncode
            except Exception:
                return False
            

        
        

a = CoreFunctionManager()
b = a.APTpackageManagement(packageManagement='apt',package='vim')
print(b)













#     def __init__(self):
#         self.__PackagesInstall= { 
#                                "apt": None,"snap": None,
#                                 "dpkg": None,"aptitude": None,
#                                 "synaptic": None,"flatpak": None 
#                                 }
        
        
#     """ Verificando se o package management esta instalado, e qual package management esta instalado"""
    
#     def PackageManagementConfigure(self) -> dict:
#         for package, v in self.__PackagesInstall.items():
#             command = f"dpkg -s {package} | grep -i '^status:\\|^version:\\|^package:'"
            
#             try:
#                 output = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
#                 if output.returncode == 0:
#                     self.__PackagesInstall[package] = True  
#                 else:
#                     self.__PackagesInstall[package] = False  
#             except subprocess.CalledProcessError:
#                 self.__PackagesInstall[package] = False
#         return self.__PackagesInstall

    
#     """ Removendo gerenciadores de pacote que não estão instalados,
#     dando preferencia aos que ja tem na maquina ( devolve uma lista com os gerenciadores que ja estão instalados.)"""
    
#     def RemoveFalseKeys(self,dictionary:dict) -> list: 
#         true_keys = []
#         for key, value in list(dictionary.items()):
#             if not value:
#                 del dictionary[key]
#             else:
#                 true_keys.append(key)
#         return true_keys

    
#     """ Escolhendo package management que vamos usar para instalação"""
    
#     def UsingPackageManagement(self,TrueKeys:list) -> str:
#         CountPackageInstalled = len(TrueKeys)
#         if CountPackageInstalled > 0:
#             Select = input(f"Select your package management: \n {TrueKeys}:\n\n " )
#             if Select in TrueKeys:
#                 PackagePrincipal = str(Select)
#                 return PackagePrincipal.lower()
            
            
#     def InstallPackages(self,packagesInstall,PackageManagement):
#             command = f"echo '{PackageManagement} install {packagesInstall}'"
#             try:
#                 output = subprocess.run(command,shell=True,capture_output=True,text=True,check=True)
#                 if output.returncode != 0:
#                     command = f'sudo {PackageManagement} install {packagesInstall} --classic'
#                     return output.returncode
#                 else:
#                     return output.returncode
#             except :
#                 raise subprocess.CalledProcessError
            
    
