import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
import json
from colorama import Fore

colorama.init()

print("""
██████╗░██╗░░░██╗░██████╗████████╗██╗░░░██╗
██╔══██╗██║░░░██║██╔════╝╚══██╔══╝╚██╗░██╔╝
██████╔╝██║░░░██║╚█████╗░░░░██║░░░░╚████╔╝░
██╔══██╗██║░░░██║░╚═══██╗░░░██║░░░░░╚██╔╝░░
██║░░██║╚██████╔╝██████╔╝░░░██║░░░░░░██║░░░
╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░

A Discord Webhook Spammer. Made by Alliege
""")

def webhkspammer():
    webhook = input(Fore.YELLOW + "[Rusty] > Enter The Webhook Link: ")
    message = input(Fore.GREEN + "[Rusty] > Enter The Message: ")
    delay = float(input(Fore.RED + "[Rusty] > Enter The Delay (Example : 0.5)"))

    while True:
        print(Fore.CYAN + "Sending --> " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Sent --> " + message)
        except:
            print("[Rusty ERROR] Something Happend! / Probably Broken Webhook -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    webhkspammer()