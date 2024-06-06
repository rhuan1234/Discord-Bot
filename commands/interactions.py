from discord.ext import commands


class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def oi(self, message):
        await message.send(f'Olá {message.author.name}, eu sou boto. Digite !commands para ver meus comandos')

    @commands.command(name='commands')
    async def help(self, message):
        texto = '''COMANDOS:
            !oi --> Bot responde uma mensagem de olá
            !todos_cargos --> Lista os cargos do server e quantos membros tem em cada
            !cargo --> cria um embed, e você ganha um cargo dependendo da forma como você reage 
            !join --> Coloca o bot no seu canal de voz
            !leave --> Tira o bot do seu canal de voz
            !play url_da_musica --> Toca uma musica no canal de voz que você está
            !play_generics --> Toca uma musica genérica de uma lista de 20 musicas
                !pause --> Pausa a musica
                !resume --> Retoma a música
                !stop --> Encerra a música
            !kick @membro --> Kicka o membro especificado do server
            !ban @membro --> Bane o membro especificado so server
            !mute @membro --> Impede o membro de escrever mensagem de texto
            !unmute @membro --> Tira o mute do membro
            !server --> Informações do servidor
            !user @membro --> Informações do membro especificado
            !ping --> Testa latência do servidor
                    
        EVENTOS:
        
            on_member_join() --> Manda mensagem de Boas-vindas ao recém integrante
            on_member_remove() --> Manda mensagem de adeus pelo membro que saiu
            on_message() --> Identifica spam e xingamentos e toma as medidas cabíveis'''
        await message.send(f'```{texto}```')


async def setup(bot):
    await bot.add_cog(Talks(bot))
