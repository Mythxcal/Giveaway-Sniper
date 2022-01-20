import requests
import time
import discord
from discord.ext import commands
import random




class Generator:
    def user_agent(headers=None):
        if headers == None:
            f = open(r"C:\Users\aisha\AppData\Local\Programs\Python\Python38\Lib\site-packages\APIUtils\Data\user_agents.md", 'r').readlines()
            return random.choice(f).replace('\n', '')
        
            
        f = open(r"C:\Users\aisha\AppData\Local\Programs\Python\Python38\Lib\site-packages\APIUtils\Data\user_agents.md", 'r').readlines()
        headers["user_agent"] = random.choice(f).replace('\n', '')
        return headers

        
        return random.choice(f).replace('\n', '')
    
    def proxy(formatted=True):
        if formatted:
            f = open(r"C:\Users\aisha\AppData\Local\Programs\Python\Python38\Lib\site-packages\APIUtils\Data\proxies.md", 'r').readlines()
            return {"proxies": random.choice(f).replace('\n', '')}
        if formatted == False:
            f = open(r"C:\Users\aisha\AppData\Local\Programs\Python\Python38\Lib\site-packages\APIUtils\Data\proxies.md", 'r').readlines()
            return random.choice(f).replace('\n', '')
        
class ROBLOX:
    def __init__(self, cookie):
        self.cookie = cookie
    
    def get_token(self):
        noTokenHeaders = {
            "Cookie":".ROBLOSECURITY={}".format(self.cookie),
        }
        url = "https://auth.roblox.com/"
        abc = requests.post(url, headers=noTokenHeaders)
        return abc.headers['x-csrf-token']

    def headers(self):
        headers = {
            "Cookie": f".ROBLOSECURITY={self.cookie}",
            'x-csrf-token': ROBLOX.get_token(self)
        }
        return headers
    
    


class Discord:
    def __init__(self, token):
        self.token = token
        
    base_url = 'https://discord.com/api/v9'
    
    def url(self, t):
        return Discord.base_url + t
    
    def headers(self):
        header = {
            "authorization": self.token
        }
        return header
    
        
        


