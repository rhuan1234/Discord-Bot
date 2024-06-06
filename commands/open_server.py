from discord.ext import commands


class Open(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1245358209070268539)
        msg = f'Bem vindo {member.mention}'
        await channel.send(msg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        msg = f'Adeus sangue bom! Vá em paz {member.mention}'
        channel = self.bot.get_channel(1236684618455978056)
        await channel.send(msg)


async def setup(bot):
    await bot.add_cog(Open(bot))
