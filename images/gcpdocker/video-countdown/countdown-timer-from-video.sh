#This example will create a 3 second video, with 100 frames per second and it will print the elapsed and remaining times using a two second accuracy.
fps=60;
mantissaDigits=2;
upperFont=100;

thingy=`ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 ${1}`

seconds=`echo ${thingy} | awk '{print ($0-int($0)>0)?int($0)+1:int($0)}'`

ffmpeg -i ${1} -vf "drawtext=fontfile='/System/Library/Fonts/ArialHB.ttc':fontcolor=0xEE9736:fontsize=$upperFont:x=(10):y=(h-text_h-10):text='%{eif\:(($seconds-t)/60)\:d\:2}\:%{eif\:mod(($seconds-t),60)\:d\:2}'" "$seconds-countdown-timer.mp4";
