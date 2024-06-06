import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import os
from commands.PlayMusic.generics import random_generics


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join')
    async def join(self, ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("Você precisa estar em um canal de voz para usar este comando.")

    @commands.command(name='leave')
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("O bot não está em um canal de voz.")

    @commands.command(name='play_generics')
    async def play_generics(self, ctx):
        url = random_generics()
        await self.play(ctx, url)

    @commands.command(name='play')
    async def play(self, ctx, url: str):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'song.mp3')
        if os.path.exists(file_path):
            os.remove(file_path)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'song',
            'noplaylist': True
        }

        if ctx.voice_client is None:
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                await channel.connect()
            else:
                await ctx.send("Você precisa estar em um canal de voz para usar este comando.")
                return

        await ctx.send('Carregando...')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_music = ydl.extract_info(url, download=False)
            if int(info_music.get('duration')) < 600:
                ydl.download([url])
            else:
                await ctx.send('Músicas com mais de 10min não são aceitas')
                return

        voice_client = ctx.voice_client
        if not voice_client.is_playing():
            voice_client.play(discord.FFmpegPCMAudio('song.mp3'))
            voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
            voice_client.source.volume = 0.5
            embed = discord.Embed(
                title='MUSIC',
                color=0xffcbdb
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
            embed.add_field(name='TITLE', value=info_music.get('title'), inline=False)
            embed.add_field(name='VIEWS', value='{:,}'.format(info_music.get('view_count')))
            date = info_music.get('upload_date')
            embed.add_field(name='PUBLICATION', value=f'{date[:4]}/{date[4:6]}/{date[6:]}')
            embed.add_field(name='DURATION', value=f'{info_music.get("duration")}s')
            embed.set_image(url=info_music.get('thumbnail'))

            await ctx.send(embed=embed)
        else:
            await ctx.send("Já estou tocando uma música. Use o comando '!stop' para parar a música atual.")

    @commands.command(name='pause')
    async def pause(self, ctx):
        voice_client = ctx.voice_client
        if voice_client.is_playing():
            voice_client.pause()
            await ctx.send("Música pausada.")
        else:
            await ctx.send("Não estou tocando nenhuma música no momento.")

    @commands.command(name='resume')
    async def resume(self, ctx):
        voice_client = ctx.voice_client
        if voice_client.is_paused():
            voice_client.resume()
            await ctx.send("Música retomada.")
        else:
            await ctx.send("A música não está pausada no momento.")

    @commands.command(name='stop')
    async def stop(self, ctx):
        voice_client = ctx.voice_client
        if voice_client.is_playing():
            voice_client.stop()
            await ctx.send('Música encerrada')
        else:
            await ctx.send("Não estou tocando nenhuma música no momento.")


async def setup(bot):
    await bot.add_cog(Music(bot))
