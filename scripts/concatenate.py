import sys
import moviepy.editor as mpy

clip1 = mpy.VideoFileClip("input/example.mp4")
clip2 = mpy.VideoFileClip("input/example2.mp4")
clip3 = mpy.VideoFileClip("input/example.mp4").subclip(5,9).crossfadein(2.0)
clip = mpy.concatenate_videoclips([clip1,clip2,clip3])
clip.write_videofile(sys.argv[2])
