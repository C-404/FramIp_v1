import os
import time
try:
    import requests
    pass
except:
    print('[×]Error\n Library request not found')
    os.system('clr || clear')
    os.system('pip install requests')
import siteName
try:
    from colorama import *
except:
    print('[×]Error\n Library colorama not found')
    time.sleep(2)
    os.system('clr || clear')
    os.system('pip install colorama')
    from colorama import *
import scanp
import SearchIp

getIPaddr = siteName.getIP
getServer = siteName.getServerName
search = SearchIp.search
scan = scanp.sc

os.system('clr || clear')
#переменная с лого
logo = Fore.LIGHTBLUE_EX+r"""
           ______                        ____        
          |  ___|                       |_  _|       
          | |_   _ __   __ _  _ __ ___    | |   _ __  
          |  _| | '__| / _` || '_ ` _ \   | |  | '_ \ 
          | |   | |   | (_| || | | | | | _| |_ | |_) |
          \_|   |_|    \__,_||_| |_| |_| \___/ | .__/ 
                                               | |    
                                               |_|
                                  
"""
#модули
modulesList = Fore.GREEN+r"""
            •-----------------------------------------•
            |Modulses:                                |
            |   [1] – get IP domain                   |
            |   [2] – get name domain                 |
            |   [3] – get IP info                     |
            |   [4] – get open port domain            |       
            •-----------------------------------------•
            

            
"""
print(
logo,
'                        framework by c404'+Fore.GREEN+r"""
            •-----------------------------------------•
            |Commands:                                |
            |   [exit] – exit                         |
            |   [modules] – view all module           |
            |   []                                    |
            |                                         |
            |                                         |
            •-----------------------------------------•
""")



def setModule (): # выбор модуля
    moduleNum = input(Fore.LIGHTCYAN_EX+"[Enter module num]: ")

    if moduleNum == "1":

        try:
            domain = input ( "[Enter domain]: " )
            ipSite = getIPaddr(domain)

            print("-" * 60)
            print("[IP] == [{0}]".format(ipSite)) 
            print("-" * 60)

        except:
            print(Fore.RED+"[Error]: Domain or ip not found!" )
  

    elif moduleNum == "2":

        try:
            site = input ( "[Enter domain]: " )
            url = "http://" + site
            server = getServer(url)
          
            print("-" * 60)
            print("[Server] == [{0}]".format(server))
            print("-" * 60)

        except:
            print(Fore.RED+"[Error]: Domain or server not found!" )
    elif moduleNum == "3":
        getIP = input("[Enter IP]:")
        results = search(getIP)
        print(results)
    elif moduleNum == "4":
        host = input("[Enter domain]:")
        results = scan(host)
        print(results)
        
        
        


    comand()

def comand ():

    comand = input("[$] --> ")

    if comand == "exit": exit( "Close program... " )
    elif comand == "modules":
      
        print ( modulesList )
        print ( setModule () )

    else:

        print (Fore.RED+"[Error]: Comand not found!" )
comand()
