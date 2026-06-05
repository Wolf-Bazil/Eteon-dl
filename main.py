import yt_dlp

url = input("playlist url here: ").strip()

opts = {
    'format': 'bestaudio/best',
    "outtmpl": './downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    'noplaylist': False, 
}

print("Initializing Download...")

with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download([url])

print("Completed")
