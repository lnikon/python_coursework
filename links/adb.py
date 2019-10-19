import re
import argparse

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--file', required=True)

    file_name = args_parser.parse_args().file
    if not file_name:
        exit(-1)
    
    text = ''
    try:
        with open(file_name, 'r') as file:
            text = file.read()
    except IOError:
        print("IOError occured during opening of {}".format(file_name))
        exit(-1)

    regex = r'(\.(\w*)\((\w*\.java)\:(\d*)\))'
    matcher = re.compile(regex)

    err_str = matcher.findall(text)

    print(err_str)