from colorama import Fore, Back, Style, init
init(autoreset=True)
import requests
import time
import os
print(Fore.BLUE + r""" .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+. 
(     ______  __      __  ________  ________      )
 )   /      |/  \    /  |/        |/        |    ( 
(    $$$$$$/ $$  \  /$$/ $$$$$$$$/ $$$$$$$$/      )
 )     $$ |   $$  \/$$/  $$ |__       $$ |       ( 
(      $$ |    $$  $$/   $$    |      $$ |        )
 )     $$ |     $$$$/    $$$$$/       $$ |       ( 
(     _$$ |_     $$ |    $$ |         $$ |        )
 )   / $$   |    $$ |    $$ |         $$ |       ( 
(    $$$$$$/     $$/     $$/          $$/         )
 )                                               ( 
(                                                 )
 "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+" """)
time.sleep(5)
os.system("cls" if os.name=="nt" else "clear")
print(Fore.RED + "WELCOME TO IYFT")
iyft_answer = input(Fore.GREEN + "What is her/his nickname:")
#urls
url = f"https://youtube.com/@{iyft_answer}"
url2 = f"https://www.tiktok.com/@{iyft_answer}"
url3 = f"https://www.pornhub.com/pornstar/{iyft_answer}"
url4 = f"https://www.instagram.com/{iyft_answer}"
url5 = f"https://github.com/{iyft_answer}"
#responses
resp =requests.get(url, timeout=5)
resp2 =requests.get(url2, timeout=5)
resp3 =requests.get(url3, timeout=5)
resp4 =requests.get(url4, timeout=5)
resp5 =requests.get(url5, timeout=5)
#if
if resp.status_code == 200:
    print(f"Username found:{url}")
if resp2.status_code == 200:
    print(f"Username found:{url2}")
if resp3.status_code == 200:
    print(f"Username found:{url3}")
if resp4.status_code == 200:
    print(f"Username found:{url4}")
if resp5.status_code == 200:
    print(f"Username found:{url5}")
