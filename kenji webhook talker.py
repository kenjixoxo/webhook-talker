#if module not installed then install
try:
    import webbrowser
    import fade
    import requests
    import os
    import colorama
    from colorama import Fore
    import time
except ModuleNotFoundError:
    os.system("pip install fade")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("python talk_as_webhook.py")

colorama.init(autoreset=True)
webbrowser.open("therealdisaster")


title = fade.purplepink(f"""
 /$$   /$$ /$$      /$$ /$$$$$$$$
| $$  /$$/| $$  /$ | $$|__  $$__/
| $$ /$$/ | $$ /$$$| $$   | $$   
| $$$$$/  | $$/$$ $$ $$   | $$   
| $$  $$  | $$$$_  $$$$   | $$   
| $$\  $$ | $$$/ \  $$$   | $$   
| $$ \  $$| $$/   \  $$   | $$   
|__/  \__/|__/     \__/   |__/   
                                 
                                 
                                                       
                                        
  kenji     webhook     talker  | @kenjixoxo                  
""")
print(title)
webhook = input(Fore.MAGENTA+"Enter Webhook: ")
set_webhook = "IF YOU WANT UR WEBHOOK SET AUTOMATICALLY SET IT HERE"

while True:
    message = input(Fore.MAGENTA+"Enter webhook message (Message to send): ")
    requests.post(webhook, json={"content": message})
    print(Fore.BLUE+f"Sent {message}")
    os.system("cls")
    print(title)
