#!/bin/bash

bash make-vid-with-countdown.sh
ffmpeg -i 1800-countdown-timer.mp4 -i looped_audio.mp3 -shortest -af 'afade=out:st=1798:d=2' -c:v libx264 -crf 22 -preset veryfast fade_vid.mp4
