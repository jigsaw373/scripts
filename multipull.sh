#!/bin/bash
# multiple pull repos at once

find . -mindepth 1 -maxdepth 1 -type d -print -exec git -C {} pull \;
