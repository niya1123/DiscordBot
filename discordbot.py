import discord # インストールした discord.py
import passToken, sys
from datetime import datetime

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

    # !exitでBotの終了
    # if message.content.startswith('!exit'):
    #     replay = "じゃあね〜！"
    #     await client.send_message(message.channel, replay)
    #     # sys.exit()
    #     # client._closed.is_set(True)
        
    #発言チャンネル内全てのログの削除
    # if message.content.startswith('!clean'):
    #     clean_flag = True
    #     while (clean_flag):
    #         msgs = [msg async for msg in client.logs_from(message.channel)]
    #         if len(msgs) > 1: # 1発言以下でdelete_messagesするとエラーになる
    #             await client.delete_messages(msgs)
    #         else:
    #             clean_flag = False
    #             await client.send_message(message.channel, 'ログの全削除が完了しました')    

    if client.user.id in message.content: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ？' # 返信文の作成
        await client.send_message(message.channel, reply) # 返信を送る

# botの接続と起動
client.run(passToken.token)