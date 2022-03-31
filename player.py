import asyncio
from typing import Awaitable

from discord import VoiceClient, FFmpegPCMAudio

from audio import Audio


def play(voice_client: VoiceClient, audio: Audio, on_finish: Awaitable) -> None:
    audio_source = FFmpegPCMAudio(
        executable='./bin/ffmpeg.exe',
        source=audio.mp3_url,
        before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
    )

    voice_client.play(
        source=audio_source,
        after=lambda _: asyncio.run_coroutine_threadsafe(
            coro=on_finish,
            loop=voice_client.loop
        ).result()
    )


def stop(voice_client: VoiceClient) -> None:
    voice_client.stop()


def pause(voice_client: VoiceClient) -> None:
    voice_client.pause()


def resume(voice_client: VoiceClient) -> None:
    voice_client.resume()
