import yt_dlp

def download_1080p_custom_name(link, custom_name):
    ydl_opts = {
        
        'format': 'bestvideo[height=1080]+bestaudio/best',
        
        
        'windows_filenames': True,
        'restrict_filenames': True,
        
        'outtmpl': f'{custom_name}.%(ext)s',
    }
    
    print("\nConnecting to YouTube... Splicing 1080p streams...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        
    print(f"\nSuccessfully downloaded as: {custom_name}.mp4")


video_link = input("1. Paste your video link here and press Enter: ")
name_input = input("2. Type a short, clean name to save the file as (e.g., my_video): ")

download_1080p_custom_name(video_link, name_input)
