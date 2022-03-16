#!/bin/sh

cp main.py ./exec/slug.py && \
cp ./exec/slug.py ./exec/slug && \
sudo mv ./exec/slug /usr/bin/
