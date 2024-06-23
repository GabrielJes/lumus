
import subprocess
from test.test import *
ConfigureEnvironment = subprocess.run(["bash","config"],shell=True)
print(ConfigureEnvironment.returncode)