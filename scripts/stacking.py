import sys
from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip(sys.argv[1]).margin(10) # add 10px contour
clip2 = clip1.fx( vfx.mirror_x)
final_clip = clips_array([[clip1, clip2]])
#final_clip.resize(width=480).write_videofile("tmp_stack.mp4", write_logfile=True, codec="libx264", audio_codec="aac", preset="ultrafast", temp_audiofile='temp-audio.m4a', remove_temp=True)
final_clip.write_videofile(sys.argv[2], preset="ultrafast", threads=4)
