import discord # インストールした discord.py
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
        await client.send_message(message.channel, reply)

    # !timeで現在時刻を答える
    if message.content.startswith('!time'):
        replay = datetime.now().strftime("%Y年%m月%d日 %H時:%M分:%S秒") 
        await client.send_message(message.channel, replay)   
        
    # 発言チャンネル内全てのログの削除
    if message.content.startswith('!clean'):
        clean_flag = True
        while (clean_flag):
            msgs = [msg async for msg in client.logs_from(message.channel)]
            if len(msgs) > 1: # 1発言以下でdelete_messagesするとエラーになる
                await client.delete_messages(msgs)
            else:
                clean_flag = False
                await client.send_message(message.channel, '過去は清算されたよ')    

    # ログの削除　
    if client.user.id in message.content: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ？' # 返信文の作成
        await client.send_message(message.channel, reply) # 返信を送る

    if message.content.startswith('!bgm'):
        channel = client.get_channel(passToken.channelID)
        if client.is_voice_connected(channel.server):
            voice = client.voice_client_in(channel.server)
        else:
            voice = await client.join_voice_channel(channel)
        path = "/Users/YK/Github/DiscordBot/Music"
        files = os.listdir(path)
        files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]

        #音楽を再生してるかどうか
        playing_song = False
        print(files_file)
        while len(files_file) > 0:
            if playing_song == False:
                if(files_file[0] == ".DS_Store"):
                    del files_file[0]
                player = voice.create_ffmpeg_player('Music/' + files_file[0])
                playing_song = True
                player.start()
                del files_file[0]
                print(files_file)
            elif player.is_done():
                playing_song = False   
            else:
                await asyncio.sleep(1)
                continue

# botの接続と起動
client.run(passToken.token)