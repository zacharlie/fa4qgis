import os

root_dir = os.path.dirname(os.path.realpath(__file__))
svg_dir = os.path.join(root_dir, 'svgs')

def check_file(svg_dir, dirname, filename):
    try:
        element = os.path.join(svg_dir, dirname, filename)
        if os.path.isfile(element):
            print (dirname + ':' + filename)
    except Exception as err:
        print(err)

with open('elements', 'r') as file:
    lines = file.readlines()
    for line in lines:
        check_file(svg_dir, 'brands', str(line.rstrip()+'.svg'))
    for line in lines:
        check_file(svg_dir, 'regular', str(line.rstrip()+'.svg'))
    for line in lines:
        check_file(svg_dir, 'solid', str(line.rstrip()+'.svg'))

