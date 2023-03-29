#!/bin/bash
# create image for all repos in an specific dir

for D in ./*; do
    if [ -d "$D" ]; then
        cd "$D"
        dir_name=$(basename "$D")
        suo docker image build . --tag "$dir_name":latest
        cd ..
    fi
