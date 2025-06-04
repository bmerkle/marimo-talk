#!/bin/bash

for gif in *.gif; do
    # Remove .gif extension
    base="${gif%.gif}"
    # Convert to webm
    ffmpeg -i "$gif" -c:v libvpx-vp9 -b:v 0 -crf 30 "${base}.webm"
done

