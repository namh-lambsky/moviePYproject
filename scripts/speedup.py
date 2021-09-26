import sys
import moviepy.editor as mpy
clip = (mpy.VideoFileClip(sys.argv[1], audio=True).fx(mpy.vfx.speedx,2.0))
clip.write_videofile(sys.argv[2], audio=True)
