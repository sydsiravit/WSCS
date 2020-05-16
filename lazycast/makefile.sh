#!/bin/bash

mkdir build
cmake -S ./RPiPlay/ -B build
make -C build

sudo apt install libx11-dev libasound2-dev libavformat-dev libavcodec-dev

make
