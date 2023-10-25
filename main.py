# from pytube import Playlist
#
# playlist = Playlist('https://www.youtube.com/playlist?list=PLJFtWsAQvrNWCIWTStVTzDc9W83_uXYGw')
# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# for video in playlist.videos:
#     video.streams.first().download()
from pytube import Playlist

# Create a Playlist object
# playlist = Playlist('https://www.youtube.com/playlist?list=PLJFtWsAQvrNWCIWTStVTzDc9W83_uXYGw')
playlist = Playlist('https://www.youtube.com/watch?v=k1i0VdOImw4&list=PL6IpcFnW0Eq2h0AwQK3FV_67_gPnRQMdB')

# Iterate through the videos in the playlist
for video in playlist.videos:
    # Get the stream with audio only
    audio_stream = video.streams.filter(only_audio=True).first()

    # Download the audio stream
    audio_stream.download(output_path='downloads/')

    # Rename the downloaded file to have a .mp3 extension
    mp4_file_path = f'downloads/{audio_stream.title}.{audio_stream.subtype}'
    mp3_file_path = f'downloads/{audio_stream.title}.mp3'

    # Rename the file from .webm (or .m4a) to .mp3
    import os
    # os.rename(mp4_file_path, mp3_file_path)

print("Download and conversion to MP3 completed.")