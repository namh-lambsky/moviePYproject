import sys
import moviepy.editor as mpy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_time = 2
end_time = 4
ffmpeg_extract_subclip(sys.argv[1], start_time, end_time, targetname=sys.argv[2])
