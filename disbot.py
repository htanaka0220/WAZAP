import discord
import random
#import numpy as np
#import pandas as pd
import os

TOKEN ="NjMyNDY4MzE3NDk1NjIzNjkw.XaF2-A.rd-WusaN0UcBM-gEewxY2kkPuJ8"#トークンキー


client = discord.Client()

#bot起動時
@client.event
async def on_ready():
    print("success login")

#文字が打ち込まれたときの処理
@client.event
async def on_message(message):#discordにて発せられた文をmessageに格納
    if message.content.startswith("電気"):
            os.system("./jtalk.sh \"電気を消しました\"")
            
    elif message.content.startswith("exited"):
            os.system("./jtalk.sh \"おくうが高専の外へ出ていきました\"")
            
    elif message.content.startswith("entered"):
            os.system("./jtalk.sh \"おくうが高専の中へ入ってきました\"")

# Bot起動
client.run(TOKEN)
