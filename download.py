import os
import youtube_dl


def exit():
    
    time.sleep(7)

    os.system('cls' if os.name == 'nt' else 'clear')


# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to set the console title
def set_console_title(title):
    os.system(f'title {title}' if os.name == 'nt' else f'echo -n -e "\033]0;{title}\007"')

# Define the output path
output_path = 'downloaded/'

def get_format_choice():
    while True:
        choice = input("Enter the format you want to download (mp3/mp4) or type quit to exit: ").lower()
        if choice in ['mp3', 'mp4', 'quit']:
            return choice
        else:
            print("Invalid choice. Please enter 'mp3', 'mp4', or 'quit'.")

# Define the common options for youtube_dl
def get_ytdl_options(format_choice):
    if format_choice == 'mp3':
        return {
            'format': 'bestaudio[ext=m4a]/bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': os.path.join(output_path, '%(id)s.%(ext)s'),
            'progress_hooks': [hook_function]
        }
    elif format_choice == 'mp4':
        return {
            'format': 'bestvideo[height=1080]+bestaudio/best[height=1080]/best',
            'noplaylist': True,
            'quiet': True,
            'outtmpl': os.path.join(output_path, '%(id)s.%(ext)s'),
            'progress_hooks': [hook_function]
        }
    else:
        # Default options if an unexpected format choice is made
        return {}

# Progress hook function to display loading messages
def hook_function(d):
    if d['status'] == 'finished':
        print('\nDone')
    elif d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} [{d['_speed_str']}]",
              end='', flush=True)

def download_video(url, ytdl_opts):
    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        ydl.download([url])

def main():
    # Clear console and set the title at the beginning
    clear_console()
    set_console_title("Downloader")

    # Choose the format at the beginning
    format_choice = get_format_choice()
    if format_choice == 'quit':
        return

    while True:
        url = input("Enter the YouTube URL or type quit to exit: ")
        if url == 'quit':
            break
        else:
            ytdl_opts = get_ytdl_options(format_choice)
            download_video(url, ytdl_opts)

if __name__ == "__main__":
    main()
