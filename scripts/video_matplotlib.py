import sys
import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

x = np.linspace(-2, 2, 200)

fig, ax = plt.subplots()
def make_frame(t):
    ax.clear()
    ax.plot(x, np.sinc(x**2) + np.sin(x + 2*np.pi/duration * t), lw=3)
    ax.set_ylim(-1.5, 2.5)
    return mplfig_to_npimage(fig)

duration = 2
animation = VideoClip(make_frame, duration=duration)
# export as a video file
animation.write_videofile(sys.argv[2], fps=24)
# export as a GIF
# animation.write_gif("tmp.gif", fps=24) # usually slower
# Ipython
# animation.ipython_display(fps=20, loop=True, autoplay=True)
