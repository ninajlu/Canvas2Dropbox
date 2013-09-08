#!/bin/sh
cd ~/Downloads
recent=$(ls -Art | tail -n 1)
echo "$recent"
sh ~/dropbox_uploader.sh upload ~/Downloads/"$recent"
