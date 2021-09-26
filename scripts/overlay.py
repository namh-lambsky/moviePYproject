import sys
import moviepy.editor as mpy

clip = mpy.VideoFileClip(sys.argv[1])

# Make the text. Many more options are available.
#w,h = moviesize = clip.size
#my_text = mpy.TextClip("EXAMPLE 2", fontsize=70, color='white')
#text_col = my_text.on_color(size=(clip.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)

# https://www.python-engineer.com/posts/video-editing-with-python/
txt = mpy.TextClip('Please Study!', font='Courier',
                   fontsize=120, color='white', bg_color='gray35')
txt = txt.set_position(('center', 0.6), relative=True)
txt = txt.set_start((0, 2)) # (min, s)
txt = txt.set_duration(6)
txt = txt.set_opacity(0.5)
txt = txt.crossfadein(1.0)
txt = txt.crossfadeout(1.0)
# composite video
final_clip = mpy.CompositeVideoClip([clip, txt])
# save file
final_clip.write_videofile(sys.argv[2])#, fps=24,
#codec=vcodec,
#preset=compression,
#ffmpeg_params=["-crf",videoquality])
