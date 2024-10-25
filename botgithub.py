import discord

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("Sei vecchio")
    elif message.content.startswith('$come stai?'):
        await message.channel.send("MALE PERCHÉ CI SEI TE")
    elif message.content.startswith('$buongiorno'):
        await message.channel.send("Buongiorno, come stai?")    
    elif message.content.startswith('$bene'):
        await message.channel.send("DAVVERO PENSAVI CHE ME NE FREGASSE QUALCOSA?")
    else:
        await message.channel.send(message.content)

client.run("YOUR TOKEN HERE")