import os

from discord import VoiceChannel, VoiceClient
from discord.ext.commands import Bot, Context

import player
import youtube

bot: Bot = Bot(command_prefix='/')


@bot.event
async def on_ready() -> None:
    print("Ready")


@bot.command
async def play(ctx: Context, url: str = None) -> None:
    if url is not None:
        await join_channel(ctx=ctx)
        audio = youtube.get_audio(url=url)
        vc: VoiceClient = ctx.voice_client
        player.play(voice_client=vc, audio=audio, on_finish=stop(ctx=ctx))
    else:
        await ctx.send("url not received")


@bot.command()
async def stop(ctx: Context) -> None:
    vc: VoiceClient = ctx.voice_client
    player.stop(vc)
    await leave_channel(voice_client=vc)


@bot.command()
async def pause(ctx: Context) -> None:
    vc: VoiceClient = ctx.voice_client
    player.pause(voice_client=vc)


@bot.command()
async def resume(ctx: Context) -> None:
    vc: VoiceClient = ctx.voice_client
    player.resume(voice_client=vc)


async def join_channel(ctx: Context):
    author_channel: VoiceChannel = ctx.author.voice.channel
    await author_channel.connect()


async def leave_channel(voice_client: VoiceClient):
    await voice_client.disconnect()


if __name__ == '__main__':
    token = os.environ['TOKEN']
    bot.run(token)
