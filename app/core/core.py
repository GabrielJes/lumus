

import subprocess
import sys
import os
import psutil

class ConfigurePackage:
    
    def __init__(self, list_apps:list,value_install) -> None:
        self.list_apps = list_apps
        self.value_install = value_install
        return None
    
    def PackageManagementConfigure(self):
        self.package = "apt"
        self.VerifyPackageManagementInstall = subprocess.run([f"dpkg -s {self.package}"],shell=True)
        return self.VerifyPackageManagementInstall.stdout

a = ConfigurePackage(list_apps="snap",value_install=None)
b = a.PackageManagementConfigure()
print(b)