from core.core_functions import CoreFunctionManager

ObjeticConfigureAPP = CoreFunctionManager

with open('Localdata/data','r') as datafile:
    for element in datafile:
        output = ObjeticConfigureAPP.APTpackageManagement(packageManagement='apt',package=element)
        print(element)
        

