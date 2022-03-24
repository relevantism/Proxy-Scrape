import os
import pyfade
import requests

class Proxy:

    def __init__(self):
        self.clear = lambda: os.system('cls')
        self.file = open(f'proxies.txt','wb')

    def Scrape(self):
        self.clear()
        os.system('title Proxy Scrape [Version 1]')
        print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_blue,'''
  __                  __                  
|__)  _  _          (_   _  _  _   _   _ 
|    |  (_) )( \/   __) (_ |  (_| |_) (- 
               /                  |      
_________________________________________

                Proxy Type              
• HTTP

• Socks4

• Socks5
 '''))
        Type_Choice = input(pyfade.Fade.Horizontal(pyfade.Colors.red_to_blue,'[$] Input Proxy Type : '))
        if Type_Choice == "HTTP":
            self.clear()
            print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_blue,'[HTTP] Proxies Saved To proxies.txt.'))
        elif Type_Choice == "Socks4":
            self.clear()
            print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_blue,'[Socks4] Proxies Saved To proxies.txt.'))
        elif Type_Choice == "Socks5":
            self.clear()
            print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_blue,'[Socks5] Proxies Saved To proxies.txt.'))
        else:
            print('False Input.')
            self.clear()
            Proxy().Scrape()
        proxy = requests.get(f'https://api.proxyscrape.com/?request=getproxies&proxytype={Type_Choice}&timeout=1000&country=all&ssl=all&anonymity=all')
        self.file.write(bytes(proxy.content))

if __name__ == "__main__":
    Proxy().Scrape()
