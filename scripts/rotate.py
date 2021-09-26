import sys
import moviepy.editor as mpy

clip = mpy.VideoFileClip(sys.argv[1], audio=True).rotate(180)
clip.write_videofile(sys.argv[2], audio=True)
#clip.write_videofile("tmp_rotated.mp4", codec="libx264", audio_codec="aac", preset="ultrafast", temp_audiofile='temp-audio.m4a', remove_temp=True)
# Search the write_videofile docs and change the preset to ultrafast, compare execution time and quality
