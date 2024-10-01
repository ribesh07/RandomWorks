import os
import yt_dlp

#Video logic
def download_video(video_url, output_path):
    print('\n............Dowloading.........\n\n')
    ydl_opts = {
        # format : 'best',
        'format' : 'bestvideo[height=1080]+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    

#Audio logic
def download_audio(video_url, output_path):
    print('\nStarting....\n')
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best available audio quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Customize output path and file name
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert audio to MP3
            'preferredquality': '192',  # Set MP3 quality (128, 192, 320 kbps)
        }],
        'ffmpeg_location': 'C:\\ffmpeg-7.1-full_build\\bin\\ffmpeg.exe'
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:                  #For Linux
        os.system('clear')


# video_url = "https://www.youtube.com/watch?v=eio1J_IK8ow"
output_path = "Download-Yt"  # Specify the directory where you want to save the video

print('\n\n--------------------------YT-Download---------------------')
while True:
    print('\nChoose what to download : \n\t[1]Video\n\t[2]Audio\n\t[0]Exit \n')
    Choose = input("Select :")
    if Choose == '1':
        video_url = input("\nEnter URL: ")
        download_video(video_url, output_path)
        x = input('\nCompleted ')
        clear_console()
        
    elif Choose == '2':
        video_url = input("\nEnter URL: ")
        download_audio(video_url, output_path)
        x = input('\nCompleted ')
        clear_console()
        
    elif Choose == '0':
        print('\nSee Ya !!!')
        break
    else :
        print("\nInvalid Input!\n")
        x = input('Enter again ')
        clear_console()

        