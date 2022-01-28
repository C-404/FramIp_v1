import socket # импортируем библиотеки
import requests

def getIP ( domainName ): # данная функция использует библиотеку сокет для получения IP

    try:
        ip = socket.gethostbyname(domainName)
        return ip

    except:
        return "[Error]: ip not found!"

def getServerName ( siteName ): # данная функция, берет из HTTP заголовков имя сервера по средством requests

    try:
        content = requests.get( siteName )
        server = content.headers['Server']
        return server

    except:
        return "[Error]: Server not found!"