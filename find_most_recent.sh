#!/bin/sh
cd ~/Downloads
recent=$(ls -Art | tail -n 1)
echo $recent
sh ~/Downloads/Dropbox_uploader.sh -p upload ~/Downloads/$recent
