import os
from moviepy.editor import *

# Replace with the path to your input directory
input_directory = 'downloads/'

# Replace with the path to your output directory
output_directory = "converted"

# Target bitrate (320 kbps)
bitrate = "320k"

def convert_to_mp3(input_path, output_path, bitrate):
    try:
        audio = AudioFileClip(input_path)
        audio.write_audiofile(output_path, codec='mp3', bitrate=bitrate)
        print(f"Converted: {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")

def batch_convert_to_mp3(input_directory, output_directory, bitrate):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.mp4'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_directory, file.replace(".mp4", "_320kbps.mp3"))
                convert_to_mp3(input_path, output_path, bitrate)

if __name__ == "__main__":
    batch_convert_to_mp3(input_directory, output_directory, bitrate)