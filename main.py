import tls_client, requests
from pystyle import *
import threading
from itertools import cycle
import random
import easygui
import os
from datetime import datetime
import ctypes

class xyzWeebhookSpammer:
    def __init__(self):
        self.webhooks = open("webhooks.txt", "r", encoding="utf-8").read().splitlines()
        self.time = datetime.today().strftime('%H:%M:%S')
        os.system("mode 80, 18")
        self.clear()
        self.setTitle("xyzWebhook Spammer → discord.gg/xyzshop → dev: bhop3")
        self.banner()
        self.xyz_session()

        message = Write.Input(Center.XCenter(f'{self.time} Message: '), Colors.cyan_to_green, interval=0.03).lower()

        while True:
            threading.Thread(target=self.webhook_spammer, args=(message,)).start()
    
    def xyz_session(self):
        useproxy = Write.Input(f'{self.time} Use Proxies? (y/n): ', Colors.cyan_to_green, interval=0.03).lower()

        if useproxy == "y":
            Write.Print("~ Using Proxy", Colors.cyan_to_green, interval=0.03)
            proxy = self.get_proxy_list()
            self.clear()
            self.banner()

            self.session = tls_client.Session(client_identifier = "chrome_120", random_tls_extension_order=True)

            self.session.proxies = {
                "http": proxy,
                "https": proxy
            }
        else:
            Write.Print("~ Using Proxyless", Colors.cyan_to_green, interval=0.03)
            self.clear()
            self.banner()
            self.session = tls_client.Session(client_identifier = "chrome_120", random_tls_extension_order=True)

    def banner(self):
        banner = '''
    ▐▄• ▄  ▄· ▄▌·▄▄▄▄•▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·  ▄ .▄            ▄ •▄ 
     █▌█▌▪▐█▪██▌▪▀·.█▌██· █▌▐█▀▄.▀·▐█ ▀█▪██▪▐█▪     ▪     █▌▄▌▪
     ·██· ▐█▌▐█▪▄█▀▀▀•██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄██▀▐█ ▄█▀▄  ▄█▀▄ ▐▀▀▄·
    ▪▐█·█▌ ▐█▀·.█▌▪▄█▀▐█▌██▐█▌▐█▄▄▌██▄▪▐███▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌
    •▀▀ ▀▀  ▀ • ·▀▀▀ • ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀
 
            discord.gg/xyzshop - dev: bhop3                         
        '''
        print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(banner)))
    
    def clear(self):
        os.system("cls")
    
    def setTitle(self, _str):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")
    
    def get_proxy_list(self):
        useproxy = Write.Input(f'\n{self.time} (y) Own Proxies or (n) Generate some ', Colors.cyan_to_green, interval=0.03).lower()

        if useproxy == "y":
            proxylist = easygui.fileopenbox(msg="Choose your Proxy List", title="Proxy List Opener", filetypes=".txt")
            proxies = open(proxylist, "r", encoding="utf-8").read().splitlines()
            return "http://" + random.choice(proxies) or "https://" + random.choice(proxies)

        else:
            try:
                api = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=ipport&format=text"
                proxies = requests.get(api).text.splitlines()
                return "http://" + cycle(proxies) or "https://" + cycle(proxies)
            except:
                pass
    
    @staticmethod
    def check_status(status_code: int):
        status_messages = {
            200: "Success",
            201: "Success",
            204: "Success",
            400: "Detected Captcha",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method not allowed",
            429: "Too many Requests"
        }
        return status_messages.get(status_code, "Unknown Status")

    def webhook_spammer(self, message):
        random_names=["og albaner", "xyzShop", ".gg/xyzShop"]

        avatars = cycle(["https://cdn.discordapp.com/attachments/1215050560554934363/1215050589495365672/Bugs_Bunny-removebg-preview.png?ex=65fb570b&is=65e8e20b&hm=e91ce83766dfab58599850f7846402b151e50d739c317204f9e0717bcae903b2&", "https://cdn.discordapp.com/attachments/1215050560554934363/1215050595397009529/IMG_2691.jpg?ex=65fb570c&is=65e8e20c&hm=1c5e22619802955b10148c4bbe77cc3459826cb7e99ca4749331e0da0fabba31&"])
        payload = {
            'username': random.choice(random_names),
            'content': message,
            "avatar_url": next(avatars)
        }

        req = self.session.post(random.choice(self.webhooks), json=payload)

        if req == 200 or 204:
            print(Colorate.Vertical(Colors.green_to_cyan, f'{self.time} ({xyzWeebhookSpammer.check_status(req.status_code)}) → {req.status_code}'))
        else:
            pass
        
xyzWeebhookSpammer()