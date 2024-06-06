from discord.ext import commands
from collections import defaultdict, deque
import time
import discord


class Moderate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.MESSAGE_LIMIT = 5
        self.TIME_WINDOW = 8
        self.black_list = [['teste', 0]]
        self.user_messages = defaultdict(lambda: deque(maxlen=self.MESSAGE_LIMIT))
        self.tolerancia = defaultdict(int)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.name == 'Boto':
            return
            # Bloco 1 - Spam
        user_id = message.author.id
        current_time = time.time()

        
        self.user_messages[user_id].append((message.content, current_time))
        if len(self.user_messages[user_id]) >= self.MESSAGE_LIMIT and current_time - self.user_messages[user_id][0][1] < self.TIME_WINDOW:
            await message.channel.send(
                f'{message.author.mention} está enviando mensagens muito rapidamente. Por favor, desacelere.')
            self.tolerancia[user_id] += 1
            if self.tolerancia[user_id] > 8:
                await message.author.ban()
                await message.channel.send(f'{message.author.name} foi banido por: Spam')
                return

        # Bloco 2 - Palavrôes

        palavrao = ['palavrão1', 'palavrão2', 'palavrão3']
        xigamento = False
        for palavra in message.content.split(' '):
            if palavra in palavrao:
                await message.channel.send(f'{message.author.name} não xingue os demais usuários! Passível de ban')
                await message.delete()
                xigamento = True
                break
        if xigamento:
            exist = False
            for i in self.black_list:
                if message.author.name == i[0]:
                    exist = True
                    if i[1] + 1 == 3:
                        await message.author.ban()
                        await message.channel.send(f'{message.author.name} foi banido por: Comportamento tóxico')
                        return
                    else:
                        i[1] = i[1] + 1
            if not exist:
                self.black_list.append([message.author.name, 0])

    @commands.command()
    async def kick(self, ctx, member: discord.Member):
        if ctx.guild.owner_id == ctx.author.id:
            await member.kick()
            await ctx.send(f'{member.mention} foi Kickado')
        else:
            await ctx.send(f'Você não possui permissão para usar este comando!')

    @commands.command()
    async def ban(self, ctx, member: discord.Member):
        if ctx.guild.owner_id == ctx.author.id:
            await member.ban()
            await ctx.send(f'{member.mention} foi Banido')
        else:
            await ctx.send(f'Você não possui permissão para usar este comando!')

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        if ctx.author.id == ctx.guild.owner_id:
            mute_role = discord.utils.get(ctx.guild.roles, name="Mute_role")
            if not mute_role:
                mute_role = await ctx.guild.create_role(name="Mute_role", reason="Para mutar usuários")

            await member.add_roles(mute_role, reason="Usuário mutado por um moderador")

            await ctx.send(f"{member.mention} foi mutado com sucesso.")
        else:
            await ctx.send("Você não tem permissão para mutar membros.")

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        if ctx.author.guild_permissions.manage_roles:
            mute_role = discord.utils.get(ctx.guild.roles, name='Mute_role')

            if mute_role and mute_role in member.roles:
                await member.remove_roles(mute_role)
                await ctx.send(f'{member.mention} foi desmutado.')
            else:
                await ctx.send(f'{member.mention} não está mutado.')
        else:
            await ctx.send('Você não tem permissão para desmutar membros.')

async def setup(bot):
    await bot.add_cog(Moderate(bot))
