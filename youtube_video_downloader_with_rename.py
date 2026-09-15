import yt_dlp

def download_1080p_custom_name(link, custom_name):
    ydl_opts = {
        # 1. Strictly forces 1080p video combined with the best audio track
        'format': 'bestvideo[height=1080]+bestaudio/best',
        
        # 2. Cleans up formatting quirks for Windows safety
        'windows_filenames': True,
        'restrict_filenames': True,
        
        # 3. Saves the file using the custom name you typed + its file extension (.mp4)
        'outtmpl': f'{custom_name}.%(ext)s',
    }
    
    print("\nConnecting to YouTube... Splicing 1080p streams...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        
    print(f"\nSuccessfully downloaded as: {custom_name}.mp4")

# --- Interactive Terminal Layout ---
video_link = input("1. Paste your video link here and press Enter: ")
name_input = input("2. Type a short, clean name to save the file as (e.g., my_video): ")

# Fires the automated code loop
download_1080p_custom_name(video_link, name_input)
