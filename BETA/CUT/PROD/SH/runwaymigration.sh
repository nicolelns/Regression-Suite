#! /usr/bin/sh

cd /Users/nsmith/Desktop/BETA/CUT/BACKEND/
python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2012.season=fashion-lists:seasons/fall.type=fashion-lists:collection-type/menswear
mv /Users/nsmith/Desktop/results.txt /Users/nsmith/Desktop/fall2012menswear.txt
#python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2012.season=fashion-lists:seasons/fall.type=fashion-lists:collection-type/rtw
#mv /Users/nsmith/Desktop/results.txt /Users/nsmith/Desktop/fall2012rtw.txt
#python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2013.season=fashion-lists:seasons/resort.type=fashion-lists:collection-type/resort
#python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2013.season=fashion-lists:seasons/spring.type=fashion-lists:collection-type/menswear
#python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2012.season=fashion-lists:seasons/fall.type=fashion-lists:collection-type/couture
#python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2013.season=fashion-lists:seasons/fall.type=fashion-lists:collection-type/couture
#python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2012.season=fashion-lists:seasons/spring.type=fashion-lists:collection-type/couture
#python runwaymigration.py http://author.nymetro.com/services/fashion/get.fashion.shows.json:year=years:2012.season=fashion-lists:seasons/spring.type=fashion-lists:collection-type/rtw
