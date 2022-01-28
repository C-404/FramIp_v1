
def search(getIP):
        import json
        import urllib.request
        url = "https://ipinfo.io/" + getIP + "/json"

        try:
            getInfo = urllib.request.urlopen( url )

        except:
            print( "\n[!] - IP not found! - [!]\n" )
            exit()

            infoList = json.load(getInfo)

            def whoisIPinfo(ip):

              try:

                myComand = "whois " + getIP
                whoisInfo = os.popen( myComand ).read()
                return whoisInfo

              except:

                return "\n [!] -- Error -- [!] \n"

     
        print( "-" * 60 )
        infoList = json.load(getInfo)

        print( "IP: ", infoList["ip"] )
        print( "City: ", infoList["city"] )
        print( "Region: ", infoList["region"] )
        print( "Country: ", infoList["country"] )
        print( "Hostname: ", infoList["hostname"] )

        print( "-" * 60 )