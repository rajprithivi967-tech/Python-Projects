import yt_dlp

def get_available_resolutions(link):
    print("\nScanning video streams... Please wait...")
    ydl_opts = {
        'windows_filenames': True,
        'restrict_filenames': True,
    }
    
    # Extract metadata without downloading the video files yet
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(link, download=False)
            formats = info.get('formats', [])
        except Exception as e:
            print(f"Error reading link: {e}")
            return None

    # Filter out and collect unique video resolutions available for this clip
    resolutions = set()
    for f in formats:
        # Check for streams that have video tracks and defined heights
        if f.get('vcodec') != 'none' and f.get('height'):
            resolutions.add(f['height'])
            
    # Return a cleanly sorted list from lowest resolution to highest
    return sorted(list(resolutions))

def download_chosen_video(link, custom_name, chosen_height):
    ydl_opts = {
        # Strictly forces your custom chosen resolution combined with the best audio track
        'format': f'bestvideo[height={chosen_height}]+bestaudio/best',
        'windows_filenames': True,
        'restrict_filenames': True,
        'outtmpl': f'{custom_name}.%(ext)s',
    }
    
    print(f"\nDownloading in {chosen_height}p resolution... Stitching tracks...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print(f"\nSuccessfully downloaded as: {custom_name}.mp4")

# --- Dynamic App User Interface ---
video_link = input("1. Paste your video link here and press Enter: ")

# Step 1: Scan and display resolutions dynamically
available_res = get_available_resolutions(video_link)

if available_res:
    print("\n--- Available Resolutions Detected ---")
    for res in available_res:
        print(f"-> {res}p")
    print("--------------------------------------")
    
    # Step 2: Ask the user to make their selection
    while True:
        try:
            choice = int(input("\n2. Type your preferred resolution height number (e.g., 1080): "))
            if choice in available_res:
                break
            else:
                print(f"That resolution isn't available. Please pick from the list: {available_res}")
        except ValueError:
            print("Please enter a valid numeric value.")
            
    # Step 3: Name and process download
    name_input = input("\n3. Type a short, clean name to save the file as: ")
    download_chosen_video(video_link, name_input, choice)
else:
    print("Could not retrieve resolutions for this video clip.")
    input("\nPress Enter to exit...")
