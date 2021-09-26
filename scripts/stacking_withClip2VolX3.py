import sys
from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip(sys.argv[1]).margin(10) # add 10px contour
clip2 = VideoFileClip("output/Clip2VolX3.mp4")
final_clip = clips_array([[clip1, clip2]])
final_clip.write_videofile(sys.argv[2], preset="ultrafast", threads=4)
