import  discord
import os

#id do Server =814283608528781313

token = os.getenv("TOKEN")
'''
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
'''

#token = read_token()

client = discord.Client()

comando = ["!help","!hi","!hello","!users","!pin"]


@client.event
async def on_member_update(antes, depois):
    n = depois.nick
    if n:
        if n.lower() =="dee":
            last = antes.nick
            if last:
                await depois.edit(nick=antes)
            else:
                await depois.edit(nick=" OI PXT ")




@client.event
async def on_member_join(member):
    await client.send(f"Opa, bem vindo ao server {member.mention}")





@client.event

async  def on_message(message):
    id_server = client.get_guild(814283608528781313)
    message.content.lower()




    if message.author == client.user:
        return
    elif message.content.find("!hello")!= -1 or message.content.find("!hi")!= -1:
        await message.channel.send("Hey!")
    elif message.content == "!help":
        embed = discord.Embed(title="Comando do Bot: ")
        for i in comando:
            embed.add_field(name=i,value="-")
        await message.channel.send(content=None,embed=embed)
    elif message.content == "!users":
        await  message.channel.send(f"-- {id_server.member_count} Users nesse servidor. --")
    #Missing permission to !pin
    elif message.content.find("!pin")!= -1:
        await message.pin()
        await message.channel.send("Mensagem fixada")

    elif message.content != comando and message.content.startswith("!"):
        await message.channel.send("Comando inválido")





client.run(token)
