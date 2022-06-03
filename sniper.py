#Copyright 2022, Mythxcal, All rights reserved.

import configparser
from re import L
import sys
import requests
from APIUtils import Discord
from configparser import ConfigParser
from colorama import Fore
import colorama, os, requests, time, discord
from discord import Webhook
from discord.ext import commands
import webbrowser


def set_title(title):
    os.system(f"title {title}")



colorama.init(True)
set_title('Giveaway Sniper')
config = ConfigParser()
config.read('config.ini')

token = config["settings"]["token"]
webhook = config["settings"]["webhook"]

invite_links = []
total_snipes = 0


print(f"""{Fore.LIGHTMAGENTA_EX}  ▄████  ██▓ ██▒   █▓▓█████ ▄▄▄       █     █░ ▄▄▄     ▓██   ██▓        ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  
 ██▒ ▀█▒▓██▒▓██░   █▒▓█   ▀▒████▄    ▓█░ █ ░█░▒████▄    ▒██  ██▒      ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██▒ ▓██  █▒░▒███  ▒██  ▀█▄  ▒█░ █ ░█ ▒██  ▀█▄   ▒██ ██░      ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██░  ▒██ █░░▒▓█  ▄░██▄▄▄▄██ ░█░ █ ░█ ░██▄▄▄▄██  ░ ▐██▓░        ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██░   ▒▀█░  ░▒████▒▓█   ▓██▒░░██▒██▓  ▓█   ▓██▒ ░ ██▒▓░      ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░▓     ░ ▐░  ░░ ▒░ ░▒▒   ▓▒█░░ ▓░▒ ▒   ▒▒   ▓▒█░  ██▒▒▒       ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░  ▒ ░   ░ ░░   ░ ░  ░ ▒   ▒▒ ░  ▒ ░ ░    ▒   ▒▒ ░▓██ ░▒░       ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░ ░   ░  ▒ ░     ░░     ░    ░   ▒     ░   ░    ░   ▒   ▒ ▒ ░░        ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ 
      ░  ░        ░     ░  ░     ░  ░    ░          ░  ░░ ░                 ░           ░  ░              ░  ░   ░     
                 ░                                      ░ ░                                                            """)


class Channel(Discord):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        super().__init__(token=token)
    
    def get_messages(self):
        req = requests.get(self.url(f'/channels/{self.id}/messages'), headers=self.headers())
        return req.json()

class Guild(Discord):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        super().__init__(token=token)


    def channels(self):
        req = requests.get(self.base_url + f'/guilds/{self.id}/channels', headers=self.headers())
        return req.json()


class Sniper(Discord):
    def get_guilds(self):
        req = requests.get(self.base_url + "/users/@me/guilds", headers=self.headers())
        return req.json()
    
    
    def get_id(self):
        try:
            user = requests.get(self.base_url + "/users/@me", headers=self.headers()).json()
            return user["id"]
        except:
            return 400
        
        
    def check_invite(self, invite):
        code = invite.replace('https://discord.gg/', '')
        x = requests.get('https://discord.com/api/v9/invites/' + code, headers=self.headers())
        return x
    
    def run(self):
        print(f"{Fore.LIGHTWHITE_EX}>>> This sniper was made by Mythxcal <<<")
        
        id = self.get_id()
        if id != 400:
            print(f"{Fore.LIGHTCYAN_EX}[*] Sniper Started (ID: {id})")
        else:
            print(f"{Fore.LIGHTRED_EX}[*] Improper Token Has Been Passed")
            time.sleep(5)
            exit()
            
        print(f"{Fore.LIGHTBLUE_EX}[!] Sniping Giveaways")
        for g in self.get_guilds():
            count = 0
            guild_id = g["id"]
            guild_name = g["name"]
            guild = Guild(id=guild_id, name=guild_name)
            for c in guild.channels():
                channel = Channel(id=c["id"], name=c["name"])
                
                if ('giveaway' in channel.name) or ('drop' in channel.name) or ('leave' in channel.name) or (c["position"] < 3) or ('req' in channel.name) or ('special' in channel.name) or ('gw' in channel.name) or ('ad' in channel.name) or ('🎉' in channel.name) or ('🎁' in channel.name) or ('here' in channel.name) or ('set' in channel.name) or ('godly' in channel.name) or ('gem' in channel.name) or ('💎' in channel.name):
                    for message in channel.get_messages():
                        try:
                            author_id = message["author"]["id"]
                            content = message["content"]
                            message_id = message["id"]
                            if author_id == '294882584201003009':
                                if "**GIVEAWAY**" in content:
                                    x = requests.put(self.url(f'/channels/{channel.id}/messages/{message_id}/reactions/%F0%9F%8E%89/@me'), headers=self.headers())    
                                    count += 1
                                    global total_snipes
                                    total_snipes += 1             
                                    time.sleep(3)

                            for word in content.split():
                                if 'https://discord.gg/' in word:
                                    invite_links.append(word)
                                    
                        except Exception as e:            
                            pass
            if count != 0:
                print(f"{Fore.LIGHTYELLOW_EX}[!] Sniped {count} giveaway(s) in {guild_name}") 

                
                
        

sniper = Sniper(token=token)
webbrowser.open("https://www.youtube.com/channel/UCoFyPFzHDqmTnzBNvqr8hFQ?sub_confirmation=1")
sniper.run()
print(f"{Fore.LIGHTYELLOW_EX}[!] Joined {total_snipes} Giveaways")


def send_webhook(msg):
    payload = {"content": msg}
    x = requests.post(webhook, json=payload)
    
for invite in invite_links:
    if sniper.check_invite(invite).status_code == 200:
        send_webhook(invite)    
    else:
        invite_links.remove(invite)
        
        
print(f"{Fore.LIGHTBLUE_EX}[!] Sent requirement servers to webhook")
print(f"{Fore.LIGHTBLUE_EX}[!] Snipe Complete")

        
    
while True:
    pass
