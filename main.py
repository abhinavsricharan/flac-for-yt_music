import sys
import yt_dlp

def download_youtube_to_flac(url, output_path="%(title)s.%(ext)s"):
    """
    Downloads audio from a YouTube URL, converts it to FLAC, and embeds metadata.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'writethumbnail': True, # Download thumbnail for embedding
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
            },
            {
                'key': 'EmbedThumbnail', # Embed the thumbnail into the audio file
            },
            {
                'key': 'FFmpegMetadata', # Embed standard metadata (title, artist, etc.)
                'add_metadata': True,
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download for: {url}")
            ydl.download([url])
            print("Download, conversion, and metadata embedding completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <YouTube-URL>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    download_youtube_to_flac(video_url)
