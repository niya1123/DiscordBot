import discord # インストールした discord.py==1.0.0a
import passToken, os, time, sys, re, asyncio, random,subprocess
from datetime import datetime
# from .opus_loader import load_opus_lib
client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):

    path = "./Music/"
    files = os.listdir(path)
    files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
    channel = client.get_channel(passToken.voice_channel_id)
      
    #!nekoでにゃーんと答える.
    if message.content.startswith('!neko'):
        reply = 'にゃーん'
        await message.channel.send(reply)

    if message.content.startswith('!bye'):
        await client.close()

    if message.content.startswith('!bgm'):
        if message.guild.voice_client is None:
            vc = await channel.connect()
        else:
            vc = message.guild.voice_client    
        playing_song = False #音楽流しているかどうか
        random.shuffle(files_file)
        while len(files_file) > 0:
            if playing_song == False:
                if(files_file[0] == ".DS_Store"):
                    del files_file[0]
                vc.play(discord.FFmpegPCMAudio(path+files_file[0]), after=lambda e: print('done', e))
                vc.source = discord.PCMVolumeTransformer(vc.source)
                vc.source.volume = 0.1
                playing_song = True
                del files_file[0]

            elif vc.is_playing() == False:
                playing_song = False
                
            else:
                await asyncio.sleep(1)
                continue
    if message.content.startswith('!volume'):
        vc = message.guild.voice_client
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = int(message.content[8:])

    if message.content.startswith('!next'):
        vc = message.guild.voice_client
        vc.stop()
    if message.content.startswith('!disconnect'):
       for voice_client in client.voice_clients:
           await voice_client.disconnect()

    if message.content.startswith('!dl'):
        url = message.content[4:]
        cmd = 'python ./dl.py ' + url
        subprocess.call(cmd, shell=True)

    if re.match(r'.*\?+',message.content):
        if re.search('http',message.content):
            pass
        else:
            for voice_client in client.voice_clients:
                await voice_client.disconnect()
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('./potter/potter.m4a'), after=lambda e: print('done', e))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 0.3

            while not vc.is_playing():
                await asyncio.sleep(1)      
        pass
    # if message.content.startswith('!ff'):
    #     for voice_client in client.voice_clients:
    #        await voice_client.disconnect()
    #     vc = await channel.connect()
    #     playing_song = False #音楽流しているかどうか
    #     if playing_song == False:
    #         vc.play(discord.FFmpegPCMAudio(path+ff_name), after=lambda e: print('done', e))
    #         vc.source = discord.PCMVolumeTransformer(vc.source)
    #         vc.source.volume = 0.3
    #         playing_song = True
    #     elif vc.is_playing() == False:
    #         playing_song = False 
    #     else:
    #         await asyncio.sleep(1)
       #permissionで死ぬ

# botの接続と起動
client.run(passToken.token)