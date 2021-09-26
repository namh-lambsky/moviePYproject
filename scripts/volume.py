import sys
import moviepy.editor as mpy
clip = mpy.VideoFileClip(sys.argv[1], audio=True, verbose=True).volumex(3.0)
clip.write_videofile(sys.argv[2], write_logfile=False, fps=60)
