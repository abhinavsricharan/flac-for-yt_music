# YouTube to FLAC Downloader

![Banner](social_preview.jpg)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Powered by yt-dlp](https://img.shields.io/badge/Powered_by-yt--dlp-red)
![License](https://img.shields.io/badge/License-MIT-green)

This script allows you to easily download audio from any YouTube video or YouTube Music link and convert it into a FLAC file, complete with embedded metadata (title, artist) and cover art.

## Features

*   **Highest Quality Audio Selection:** Automatically rips the absolute best audio stream available from the source.
*   **Automatic Cover Art:** Fetches the YouTube thumbnail and natively embeds it into the FLAC file.
*   **Smart Metadata:** Tags your files with the correct Title and Artist automatically based on the video information.
*   **Playlist Support:** Feed it a playlist URL and watch it download an entire album sequentially.

## Why use this tool?

While YouTube streams audio using lossy formats (like Opus or AAC), downloading them as FLAC provides a couple of distinct benefits:
1. **No Generation Loss:** If you plan to use the audio in a video editor, DJ software, or audio workspace, saving it as FLAC ensures the audio will not undergo any further degradation or "generation loss" during intermediate edits.
2. **Library Consistency:** If you are building a local music library and prefer all your tracks to be in the lossless `.flac` format for uniformity and metadata support, this tool handles the container conversion perfectly. 

*Note: Because the original source on YouTube is lossy, converting to FLAC does not magically upscale or improve the original audio fidelity beyond what YouTube provides. It perfectly preserves the lossy stream in a lossless container.*

## Prerequisites

Before using the script, you need to make sure your terminal is correctly set up. You must have `ffmpeg` installed and accessible in your system's PATH.

1. **Open a Terminal:** Open PowerShell or Command Prompt. 
2. **Navigate to the folder:** Go to the folder where the script is located.
   ```bash
   cd <your-file-path>
   ```
3. **Activate the Virtual Environment:** Since the required Python packages (`yt-dlp` and `mutagen`) are installed in an isolated environment, you must activate it before running the script.
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   *(Note: If you see `(.venv)` appear at the start of your terminal prompt, it was successful.)*

## How to Download a Song

To download a song, simply run `main.py` followed by the YouTube URL wrapped in quotes.

### Basic Command:
```bash
python main.py "YOUR_YOUTUBE_URL_HERE"
```

### Examples:

**Single Video / Song:**
```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**YouTube Music Link:**
```bash
python main.py "https://music.youtube.com/watch?v=dQw4w9WgXcQ"
```

**Playlists:**
The script also natively supports downloading entire playlists. Just provide the playlist URL.
```bash
python main.py "https://www.youtube.com/playlist?list=PL..."
```
*(Warning: Playlists will download every video in the list one by one, which may take some time and consume a lot of disk space.)*

## Troubleshooting

- **`ffprobe and ffmpeg not found` error:** This means your terminal cannot find the `ffmpeg` installation. Close your terminal entirely and open a new one to refresh your system's PATH variables.
- **Script fails to download:** Sometimes YouTube updates their systems which breaks downloaders. If you get extraction errors, you can update the underlying downloader by running: `pip install --upgrade yt-dlp` while your virtual environment is active.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## Disclaimer

This tool is provided for personal, educational, and fair-use purposes only. Users are responsible for ensuring their use of this software complies with YouTube's Terms of Service and their local copyright laws. The developers of this tool are not responsible for any misuse.

## License

This project is licensed under the MIT License.
