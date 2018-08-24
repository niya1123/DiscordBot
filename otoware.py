import discord, passToken, re, asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if re.match(r'.*\?+', message.content) or re.match(r'.*\？+', message.content):  
        channel = client.get_channel(passToken.channelID)
        if client.is_voice_connected(channel.server):
            voice = client.voice_client_in(channel.server)
        else:
            voice = await client.join_voice_channel(channel)
        
        player = voice.create_ffmpeg_player('potter.m4a')
        player.start()

        while not player.is_done():
            await asyncio.sleep(1)



        
client.run(passToken.otoware_token)