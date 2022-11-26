import requests, json
from colorama import just_fix_windows_console, Fore
just_fix_windows_console()

tokens = open("tokens.txt").read().splitlines()
promoIds = []

print(Fore.MAGENTA + """

░██████╗░██╗███████╗████████╗  ░██████╗░███████╗████████╗████████╗███████╗██████╗░
██╔════╝░██║██╔════╝╚══██╔══╝  ██╔════╝░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
██║░░██╗░██║█████╗░░░░░██║░░░  ██║░░██╗░█████╗░░░░░██║░░░░░░██║░░░█████╗░░██████╔╝
██║░░╚██╗██║██╔══╝░░░░░██║░░░  ██║░░╚██╗██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗
╚██████╔╝██║██║░░░░░░░░██║░░░  ╚██████╔╝███████╗░░░██║░░░░░░██║░░░███████╗██║░░██║
░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░  ░╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
                            By Sysy's V 0.0.1


""")
print(Fore.GREEN + "[+] Loaded " + str(len(tokens)) + " Token(s)")
print(Fore.CYAN + "[*] Getting Promo(s) Id(s)")

promoIdReq = requests.get("https://discord.com/api/v9/outbound-promotions?locale=en-US").json()
for promoCode in promoIdReq:
    promoIds.append(promoCode['id'])

print(Fore.GREEN + "[+] Found " + str(len(promoIds)) + " Promo(s) Id(s)")

def getCode(token, promoId):
        cookies = {
            '__dcfduid': '80aa09f0441611edac0eeb43410501b9',
            '__sdcfduid': '80aa09f1441611edac0eeb43410501b955b69ab4a51d8771b4873949b7f8934650c4c099b565720419be0f3244a910c5',
            '__stripe_mid': '54bf2f9b-3d0b-49a7-b216-d2401628bff307957c',
            'locale': 'en-US',
            '__cfruid': 'efc7eaa9001d1f222168f88fca0c099d5419ba48-1669453933',
            '__cf_bm': 'XYzJFgDVv_mL45rS6gEnoFV_pma_QfKbR4zJ7Zpe7LI-1669454227-0-AUcuuViFMMY0aJhY9pS7aEf97WxgLyXTUyxflNizrsdDAn51X4qIYElXN5QvkUV/vpGI3RhY6T+fSpgcGKNKJn/KS3yl0iEqMAjLUKGxgbC+rglFeMyKCynrz2FS6VO3rhYacclKFf2cmdJdsWaD4J8=',
            '__stripe_sid': '5f53904e-482e-4fdd-9e5b-734b0ceaffcc4de6f4',
        }

        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': token,
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/1039458505188462622/1039516720248934431',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE2MDY0NSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }

        response = requests.post('https://discord.com/api/v9/outbound-promotions/' + promoId + '/claim', cookies=cookies, headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + "[+] Code: " + response.json()['code'] + "    |   Product: " + response.json()['promotion']['outbound_title'] + "    |   Id: " + promoId)
            f = open("code.txt", "a")
            f.write("[+] Code: " + response.json()['code'] + "    |   Product: " + response.json()['promotion']['outbound_title'] + "    |   Id: " + promoId + "\n")
            f.close()
        else:
            print(Fore.RED + "[!] Error    |   Token: " + token[:20] + "    |   StatusCode: " + str(response.status_code))

for token in tokens:
    for promoId in promoIds:
        try:
            getCode(token, promoId)
        except:
            getCode(token, promoId)