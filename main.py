import yt_dlp

def download_youtube_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': './downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'noplaylist': False,
    }

    print("🚀 Initializing download sequence...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
    print("✅ Playlist download complete!")

if __name__ == "__main__":
    url = input("Paste your YouTube Playlist URL: ")
    download_youtube_playlist(url)