import discord # インストールした discord.py==1.0.0a
import passToken, os, time, sys, re, asyncio
from datetime import datetime
# from .opus_loader import load_opus_lib
client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
      
    #!nekoでにゃーんと答える.
    if message.content.startswith('!neko'):
        reply = 'にゃーん'
        await message.channel.send(reply)

    

# botの接続と起動
client.run(passToken.token)