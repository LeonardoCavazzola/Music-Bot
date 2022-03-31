from youtube_dl import YoutubeDL

from audio import Audio

ydl = YoutubeDL()


def get_audio(url: str) -> Audio:
    video = ydl.extract_info(url=url, download=False)
    title = video['title']
    mp3 = video['formats'][0]['url']
    return Audio(title=title, mp3_url=mp3)
