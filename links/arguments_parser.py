import argparse
from helper import LinksGenerator

class ArgumentsParser(object):
    def __init__(self):
        self.links = []
        self.links_file = []

        self.parser = argparse.ArgumentParser(description='Links or file with links')
        group = self.parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-l', '--links', type=str, nargs='+', help='List of links')
        group.add_argument('-f', '--file', type=str, help='File with one link on each line')
        group.add_argument('-g', '--generate', type=str, help='Generate file with random links')
    
    def parse(self):
        return self.parser.parse_args()
