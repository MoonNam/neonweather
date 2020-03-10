import discord
import datetime
import os

client = discord.Client()
now = datetime.datetime.now()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("야근")
    await client.change_presence(status=discord.Status.online, activity=game)


import discord
import datetime

client = discord.Client()
now = datetime.datetime.now()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("야근")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/clear"):
        a = message.author.top_role
        if str(message.author.top_role) == "🍔인게임관리자🍔":
            await message.channel.purge(limit=1000)
        elif str(message.author.top_role) == "🍔인게임관리자🍔":
            await message.channel.purge(limit=1000)
        elif str(message.author.top_role) == "🍔인게임관리자🍔":
            await message.channel.purge(limit=1000)
        else:
            await message.channel.send("권한이 없습니다.")

    if message.content.startswith("/퇴근"):
        await message.channel.send(message.author.display_name +"님이 퇴근하셨습니다." + '\n\n' + (str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + "시" + str(now.minute) + "분"))

    if message.content.startswith("/출근"):
        now_time =(str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + "시" + str(now.minute) + "분")
    embed = discord.Embed(color=0xff0000)
    embed.add_field(name="네온 출석부", value=message.author.display_name + " 님이 출근하셨습니다.　　" + '\n\n' + now_time, inline=True)
    embed.set_thumbnail(url=message.author.avatar_url)
    await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
