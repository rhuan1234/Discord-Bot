from discord.ext import commands
import discord
import time
from datetime import datetime


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def user(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=0xffcbdb
        )
        embed.add_field(name='No Discord:', value=f'Há {datetime.now().year - ctx.author.created_at.year} anos')
        embed.add_field(name='No Servidor:',
                        value=f'Há {(datetime.now().date() - ctx.author.joined_at.date()).days} dias')
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f'{ctx.author}', icon_url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def server(self, ctx):
        guild = ctx.guild
        owner = await guild.fetch_member(guild.owner_id)
        embed = discord.Embed(
            color=0xffcbdb
        )
        embed.set_author(name=f'{guild.name}', icon_url=guild.icon.url)
        embed.add_field(name='🆔 ID do servidor:', value=guild.id)
        embed.add_field(name='🗓 Criado Em:', value=f'{str(guild.created_at.date()).replace("-", "/")}')
        embed.add_field(name='📂 Gerenciado Por:', value=f'@{owner}')
        embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name=f'👨‍👦‍👦 Integrantes:', value=f'({guild.member_count}) Membros')
        # Filtrando canais de voz
        voice = sum(1 for channel in guild.channels if isinstance(channel, discord.VoiceChannel))
        # Filtrando canais de texto
        text = sum(1 for channel in guild.channels if isinstance(channel, discord.TextChannel))
        embed.add_field(name=f'📢 Canais ({text + voice})', value=f'{text} Texto | {voice} Voz')
        embed.add_field(name=f'Cargos: {len(guild.roles)}', value='Digite !todos_cargos para ver')
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        start_time = time.time()
        message = await ctx.send("Pong!🏓")
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convertendo para milissegundos
        embed = discord.Embed(
            title='Pong!🏓',
            color=0xffcbdb,
            description=f'⌛ Latência: {latency:.0f}ms'
        )

        await message.edit(content='', embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))
