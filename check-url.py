#!/usr/bin/python3

import requests
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


with open('urls.txt', 'r') as file:
	urls = file.readlines()

for url in urls:
	url = url.strip()
	try:
		response = requests.get(url, timeout=5)
		if response.status_code == 200:
			prGreen(f"[+] La url {url} Funciona")
		else:
			prRed(f"[-] La url {url}  No Funciona")
	except:
		prRed(f"[-] La url {url} No Funciona")

