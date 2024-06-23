import pytest
import subprocess
from unittest.mock import patch
from core.core_functions import ConfigurePackage

""" Teste 1: Verifica se todos os pacotes estão instalados corretamente """
def test_all_packages_installed():
    configurer = ConfigurePackage()
    with patch('subprocess.run') as mocked_run:
        mocked_run.return_value.returncode = 0  # Simula que o comando dpkg -s retorna com sucesso
        result = configurer.PackageManagementConfigure()
        assert all(value == True for value in result.values())

""" Teste 2: Verifica se nenhum dos pacotes está instalado """
def test_no_packages_installed():
    configurer = ConfigurePackage()
    with patch('subprocess.run') as mocked_run:
        mocked_run.return_value.returncode = 1  # Simula que o comando dpkg -s falha
        result = configurer.PackageManagementConfigure()
        assert all(value == False for value in result.values())

""" Teste 3: Verifica se alguns pacotes estão instalados e outros não """
def test_some_packages_installed():
    configurer = ConfigurePackage()
    with patch('subprocess.run') as mocked_run:
        mocked_run.side_effect = lambda cmd, **kwargs: subprocess.CompletedProcess(cmd, 0) if "apt" in cmd else subprocess.CompletedProcess(cmd, 1)
        result = configurer.PackageManagementConfigure()
        assert result["apt"] == True
        assert result["snap"] == False

"""  Teste 4: Verifica se um pacote está parcialmente instalado (simulado) """  
def test_partially_installed_package():
    configurer = ConfigurePackage()
    with patch('subprocess.run') as mocked_run:
        mocked_run.return_value.returncode = 0  # Simula que o comando dpkg -s retorna com sucesso
        configurer.PackagesInstall["apt"] = True  # Simula que o pacote 'apt' está instalado
        result = configurer.PackageManagementConfigure()
        assert result["apt"] == True
        assert all(value in [True, False] for key, value in result.items() if key != "apt")

"""  Teste 5: Verifica se todos os pacotes são desconhecidos """  
def test_all_unknown_packages():
    configurer = ConfigurePackage()
    with patch('subprocess.run') as mocked_run:
        mocked_run.return_value.returncode = 1  # Simula que o comando dpkg -s falha
        result = configurer.PackageManagementConfigure()
        assert all(value == False for value in result.values())

""" Teste 6: Verifica se o método lida corretamente com exceções """
def test_handling_exceptions():
    configurer = ConfigurePackage()
    with patch('subprocess.run') as mocked_run:
        mocked_run.side_effect = subprocess.CalledProcessError(1, "dpkg -s apt")
        result = configurer.PackageManagementConfigure()
        assert all(value == False for value in result.values())

""" Teste 7: Verifica se todos os pacotes retornam False quando o subprocess.run lança uma exceção """ 
def test_all_packages_exception():
    configurer = ConfigurePackage()
    with patch('subprocess.run') as mocked_run:
        mocked_run.side_effect = subprocess.CalledProcessError(1, "dpkg -s")
        result = configurer.PackageManagementConfigure()
        assert all(value == False for value in result.values())

if __name__ == "__main__":
    pytest.main([__file__])
