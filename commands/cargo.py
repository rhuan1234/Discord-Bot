from discord.ext import commands
import discord


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.msg_id = None
        self.msg_user = None

    @commands.command(name='todos_cargos')
    async def roles(self, ctx):
        guild = ctx.guild

        all_roles = guild.roles

        member_for_roles = {}
        for role in all_roles:
            member_for_roles[role.name] = 0

        for member in guild.members:
            for role in member.roles:
                member_for_roles[role.name] += 1

        texto = ''
        for role, member in member_for_roles.items():
            texto += f'{role:<30} {member} Membros \n'
        await ctx.send(f'```{texto}```')

    @commands.command(name='cargo')
    async def new_role(self, ctx):
        embed = discord.Embed(
            title='Escolha um cargo',
            color=0x690FC3,
            description='-Bronze - 🧱\n'
                        '-Prata - 📻\n'
                        '-Ouro - 🪙\n'
                        '-Diamante - 💎\n'
        )
        bot_msg = await ctx.send(embed=embed)
        await bot_msg.add_reaction('🧱')
        await bot_msg.add_reaction('📻')
        await bot_msg.add_reaction('🪙')
        await bot_msg.add_reaction('💎')
        self.msg_id = bot_msg.id
        self.msg_user = ctx.author


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if self.msg_id is not None:
            role = None
            guild = reaction.message.guild
            member = guild.get_member(user.id)
            if member is None:
                try:
                    member = await guild.fetch_member(user.id)
                except discord.errors.NotFound:
                    print("Membro não encontrado no servidor")
                    return

            if reaction.message.id == self.msg_id and str(reaction.emoji) == '🧱':
                role = guild.get_role(1242838530313687172)
            elif reaction.message.id == self.msg_id and str(reaction.emoji) == '📻':
                role = guild.get_role(1242838653471031448)
            elif reaction.message.id == self.msg_id and str(reaction.emoji) == '🪙':
                role = guild.get_role(1242838728070795324)
            elif reaction.message.id == self.msg_id and str(reaction.emoji) == '💎':
                role = guild.get_role(1242838765920059453)
            channel = reaction.message.channel
            if role not in member.roles:
                await member.add_roles(role)
                await channel.send(f'{user.name} foi adicionado ao cargo {role}')
            else:
                await channel.send(f'{user.name} já tem cargo {role}')

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if self.msg_id is not None:
            role = None
            guild = reaction.message.guild
            member = guild.get_member(user.id)
            if member is None:
                try:
                    member = await guild.fetch_member(user.id)
                except discord.errors.NotFound:
                    print("Membro não encontrado no servidor")
                    return

            if reaction.message.id == self.msg_id and str(reaction.emoji) == '🧱':
                role = guild.get_role(1242838530313687172)
            if reaction.message.id == self.msg_id and str(reaction.emoji) == '📻':
                role = guild.get_role(1242838653471031448)
            if reaction.message.id == self.msg_id and str(reaction.emoji) == '🪙':
                role = guild.get_role(1242838728070795324)
            if reaction.message.id == self.msg_id and str(reaction.emoji) == '💎':
                role = guild.get_role(1242838765920059453)

            if role in member.roles:
                await member.remove_roles(role)
                channel = reaction.message.channel
                await channel.send(f'{user.name} foi removido do cargo {role}')

async def setup(bot):
    await bot.add_cog(Roles(bot))
