#!/bin/bash

#youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -o announcements ${1}
# comment the above out and just go straight from the mp4 if we need to get it somewhere besides youtube

rm list.txt

for i in {1..24}
do
    echo "file 'announcements.mp4'" >> list.txt
done

ffmpeg -f concat -i list.txt -c copy loop.mp4

ffmpeg -sseof -1800 -i loop.mp4 -c copy loop30min.mp4

bash countdown-timer-from-video.sh loop30min.mp4

rm announcements.mp4 list.txt loop.mp4 loop30min.mp4
