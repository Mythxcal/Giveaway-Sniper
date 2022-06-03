import requests
import time
import discord
from discord.ext import commands
import random


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
