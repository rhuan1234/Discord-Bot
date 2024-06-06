from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True  
intents.message_content = True  
intents.reactions = True  
intents.guild_messages = True
intents.voice_states = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot online - Olá Mundo!')
    await load_cogs()

async def load_cogs():
    try:
        await client.load_extension('commands.interactions')
        await client.load_extension('commands.cargo')
        await client.load_extension('commands.open_server')
        await client.load_extension('commands.PlayMusic.play')
        await client.load_extension('commands.moderation')
        await client.load_extension('commands.info')
        print('Cog carregado com sucesso!')
    except Exception as e:
        print(f'Erro ao carregar Cog: {e}')


TOKEN = 'seu token'
client.run(TOKEN)
