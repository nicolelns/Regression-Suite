#! /usr/bin/bash

cd ../../BACKEND
python runwayshows.py
cd ../PROD/PY
python runway.py
python runwayshowopener.py
cd ../SEL
python runwayshowopener.sel.py
python runwayshow.sel.py

