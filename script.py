import whisper
import os
import sys
import yt_dlp
import subprocess
import time
from moviepy.editor import *

VIDEO_FILE_PATH = "./aa.mp4"
AUDIO_FILE_PATH = "./aa.mp3"
output_file_path = "./transcription.txt"
input_link_file = "./link.txt"
transcription_file = "./transcription.doc"
transcription_file2 = "./transcription.txt"

# 0. Clean files:
if (os.path.isfile(output_file_path)):
    os.remove(output_file_path)
if (os.path.isfile(VIDEO_FILE_PATH)):
    os.remove(VIDEO_FILE_PATH)
if (os.path.isfile(AUDIO_FILE_PATH)):
    os.remove(AUDIO_FILE_PATH)
if (os.path.isfile(transcription_file)):
    os.remove(transcription_file)
if (os.path.isfile(transcription_file2)):
    os.remove(transcription_file2)



# 1. Read the URL:
with open(input_link_file, "r") as f:
    for line in f:
        link = line
        break

print(link)

# 2. Download the video:
print()
print("Step 1: Downloading the video..")
subprocess.run(["yt-dlp","--no-playlist","--no-check-certificate", "-i", "-f", "18", "--output", VIDEO_FILE_PATH, str(link)]) 

# 3. Convert to mp3:
print()
print("Step 2: Convert to mp3..")
def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)

if (os.path.isfile(VIDEO_FILE_PATH)):
    os.remove(VIDEO_FILE_PATH)

# 4. Do transcription:
print()
print("Step 3: Video transcription in progress..")
# Solve error: FileNotFoundError: [WinError 2] The system cannot find the file specified
# Put ffmpeg.exe in the same directory.
# https://github.com/openai/whisper/discussions/109

AUDIO_FILE_PATH = "./aa.mp3"

#print(os.path.isfile(AUDIO_FILE_PATH))

start = time.time()
model = whisper.load_model("medium")
results = model.transcribe(AUDIO_FILE_PATH)
end = time.time()
time_taken = (end - start)/1000
print("<< Time taken to transcribe: ",time_taken, "seconds (", time_taken/60, "minutes)")

with open(output_file_path, "w") as txt_file:
    txt_file.write(results["text"])
    txt_file.write("\n")

print(results["text"])

if (os.path.isfile(AUDIO_FILE_PATH)):
    os.remove(AUDIO_FILE_PATH)

print()
print("<<<<< Transcription finished and saved to file [transcription.txt].")
print("You can now close this window..")



"""
yt-dlp --no-playlist --no-check-certificate -i -f 18 --output aa.mp4 https://www.youtube.com/watch?v=Owf5Uq4oFps


# This gives times as well (runs in realtime):
whisper --model medium --language English aa.mp4

"""
