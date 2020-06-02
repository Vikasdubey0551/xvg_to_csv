## prerequisites

This scripts converts a single or multiple **XVG** (gromacs output file) or text files to a joint **CSV** file without distrupting the formating and labels. 

Prerequistes are `numpy`,`regex` and `argparse` libraries. 

## Usage 

`usage: python multi_xvg_to_csv.py [-h] [-f XVG1 XVG2 ..] [-o CSV]`

optional arguments:

    -h, --help  show this help message and exit  
    -f XVG    INPUT1.xvg INPUT2.xvg ...
    -o CSV    OUTPUT.csv 
