import sys
sys.path.append("services")
from services.menuPrincipal import menuPrincipalController 

def executaApp():
    menuPrincipalController()
    print("oi")

executaApp()
