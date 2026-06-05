import yt_dlp

url = input("playlist url here: ").strip()

opts = {
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    "outtmpl": './downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    'noplaylist': False, 
}

print("Initializing Download...")

with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download([url])

print("Completed")
