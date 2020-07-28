import os
import json
from shutil import copyfile

root_dir = os.path.dirname(os.path.realpath(__file__))

with open('config.json') as json_file:
    data = json.load(json_file)
    for element in data:
        for svg in element['symbols']:
            try:
                infile = os.path.join(root_dir, element['inpath'], svg)
                fbase = os.path.basename(os.path.splitext(svg)[0])
                fext = os.path.splitext(svg)[1]
                outname = element['prefix'] + fbase + element['suffix'] + fext
                outfile = os.path.join(root_dir, element['outdir'], outname)
                copyfile(infile, outfile)
                print('Copied: ' + outfile)
            except Exception as err:
                print(err)

