import os
import sys
import argparse

def sgdc_to_tcl_converter(in_file_name, out_file_name):
    '''
    Algorithm overview

    1. If there is lines, then read line
    3. If starts with #, then skip
    2. Replace " with \"
    3. Replace substring between first \" and . with '${design_name}'
    4. Go to 1
    '''

    sgdc_file = open(in_file_name, 'r')
    tcl_file = open(out_file_name, 'w+')

    for line in sgdc_file:
        if not line:
            tcl_file.write('\n')
            continue

        if line.startswith("#"):
            continue

        line = line.strip('\n')

        design_name_begin = line.find('"') + 1
        design_name_end = line.find('.')
        design_name = line[design_name_begin:design_name_end]

        line = line.replace(design_name, r'${design_name}', 1)

        line = line.replace(r'"', r'\"')
        result = '{}{}{}{}{}'.format('append rv "', line.strip('\n'), r'\n', '"', '\n')

        tcl_file.write(result)

    pass

if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument('--input', type=str)
    aparser.add_argument('--output', type=str)

    args = aparser.parse_args()

    input_name = args.input
    output_name = args.output

    sgdc_to_tcl_converter(input_name, output_name)

    pass
