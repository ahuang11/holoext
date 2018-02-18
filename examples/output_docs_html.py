import glob
import os

files = glob.glob('*.ipynb')
for file in files:
    os.system('jupyter nbconvert {0}'.format(file))
    os.system('mv *.html ../docs/examples/html_output')
