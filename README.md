# listdates - A tools that list all dates in the given range #
-----
## Installation
```
git clone xxxxxx && cd xxxxx
python setup.py install
```
## Usage
```
listdates <begin-date> <end-date> <output-date-format>
for example:
>listdate 20160701 20160710 %y%m%d
160701
160702
160703
160704
160705
160706
160707
160708
160709
160710
>listdate 20160705 20160701 %m%d
0705
0704
0703
0702
0701
```
