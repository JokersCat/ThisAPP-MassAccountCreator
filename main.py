import os
import threading, random, requests
from colorama import Fore
import httpx
import datetime
now = datetime.datetime.now()


claimed = 0
errors = 0
def check():
    _username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz123456789', k=3))
    try:
        _check = requests.post(
            "https://api.ws.thisapp.so/graphql",
            json={
                "operationName": "CheckUsername",
                "variables": {
                    "input": {
                        "username": _username
                    }
                },
                "query": "query CheckUsername($input: CheckUsernameInput!) {\n  checkUsername(input: $input) {\n    isAvailable\n    __typename\n  }\n}\n"
            },
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                "origin": "https://thisapp.com"
            }
        )

        if '"isAvailable":true' in _check.text:
            print(f'{Fore.RESET}[{Fore.LIGHTYELLOW_EX}~{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Ready to claim: {_username}')
            date = now.strftime(f'%d-%m-%Y-%M-%S')
            firstname = 'your-mum'
            email = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)) + '@gmail.com'
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                # "content-type": "application/json",
                "origin": "https://thisapp.com",
                "referer": "https://thisapp.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36"
            }
            payload = {"email": f"{email}", "firstName": f"{firstname}", "lastName": "edited",
                       "username": f"{_username}"}
            with httpx.Client() as client:
                req = client.post("https://api.ws.thisapp.so/v1/auth/presignup", json=payload, headers=headers)
                # print("[%s] %s" % (req.status_code, username))
                if req.status_code == 200:
                    print(
                        f'{Fore.RESET}[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}Successfully claimed: {_username}')
                    with open('claimed.txt', 'a+') as file:
                        file.write(
                            f'username: {_username} | firstname: {firstname} | email: {email} | sniped at: {date}\n')
                if req.status_code == 500:
                    print(
                        f'{Fore.RESET}[{Fore.LIGHTRED_EX}-{Fore.RESET}] {Fore.LIGHTRED_EX}Failed already claimed: {_username}')

    except:
        pass


        


import os
os.system('cls')
while True:
    if threading.active_count() < 100:
        threading.Thread(target=check).start()
