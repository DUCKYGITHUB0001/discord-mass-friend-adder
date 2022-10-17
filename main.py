import discord
from discord.ext import commands
import asyncio
import colorama
from colorama import Fore, init
import random
import string

token = input(" User Token : ")

bot = commands.Bot(command_prefix='.', self_bot=True)

init()

@bot.event
async def on_ready():
    print(f"{Fore.CYAN} Logged in to the user account: {bot.user}")



@bot.command()
async def start(ctx):
    print(" ")
    guild = ctx.guild
    print(f"{Fore.WHITE}[{Fore.CYAN}GUILD{Fore.WHITE}]{Fore.CYAN} Got target guild")
    print(" ")
    scraped = 0
    failed = 0
    friended = 0
    for mem in guild.members:
        try:
            f = open("scraped.txt", "a")
            f.write(f"{mem}\n")
            f.close()
            scraped = scraped + 1
            print(f'{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}] {Fore.WHITE}[{Fore.GREEN}{scraped}{Fore.WHITE}]{Fore.CYAN} added {mem} to the list of scraped users')
            await asyncio.sleep(1)
            idd = mem.id
            user = await bot.fetch_user(idd)
            try:
                await user.send_friend_request()
                friended = friended + 1
                print(f'{Fore.WHITE}[{Fore.CYAN}SENT{Fore.WHITE}] {Fore.WHITE}[{Fore.GREEN}{friended}{Fore.WHITE}]{Fore.CYAN} Sent a friend request to {mem} with id {mem.id}')
                timetosleep = random.randint(12,19)
                print(f'{Fore.WHITE}[{Fore.CYAN}X{Fore.WHITE}] Waiting for {Fore.CYAN}{timetosleep}{Fore.WHITE} seconds.')
                await asyncio.sleep(timetosleep)
            except:
                print(f'{Fore.WHITE}[{Fore.RED}NOT SENT{Fore.WHITE}] {Fore.CYAN} Failed to send request, or request already sent')
                timetosleep = random.randint(12,19)
                print(f'{Fore.WHITE}[{Fore.CYAN}X{Fore.WHITE}] Waiting for {Fore.CYAN}{timetosleep}{Fore.WHITE} seconds.')
                await asyncio.sleep(timetosleep)
        except:
            failed = failed + 1
            print(f'{Fore.WHITE}[{Fore.RED}FAIL{Fore.WHITE}] {Fore.WHITE}[{Fore.RED}{failed}{Fore.WHITE}] {Fore.CYAN} couldnt add {mem} to the list of scraped users')
    print(" ")
    print(f"{Fore.WHITE} Scraped Users {Fore.GREEN}{scraped} {Fore.WHITE}| {Fore.RED}{failed}")
        

        


bot.run(f'{token}')




