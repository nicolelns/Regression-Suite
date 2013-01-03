#! /usr/bin/bash

curl --head http://www.vulture.com/ >header.txt
python header_test.py