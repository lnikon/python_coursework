import os
import sys
from bs4 import BeautifulSoup, Tag

class DefaulSpyglassHandler(object):
    def __init__(self, master_file=""):
        self.master_file = master_file

        master = open(self.master_file, 'r+')
        self.master_content = master.read()
        self.master_soup = BeautifulSoup(self.master_content, features='html.parser')

    def handle(self, current_file):
        '''
        Find header in file with 'regression_dir' id and replace its value by its path

        Return nothing
        '''

        current_content = ''
        current_soup = BeautifulSoup(current_content, features='html.parser')

        try:
            with open(current_file, 'r') as current:
                current_content = current.read()
                current_soup = BeautifulSoup(current_content, features='html.parser')
            
        except IOError:
            print("Can't open(r/w) file {} for handling".format(current_file))
            return

        regression_log_path = current_soup.find("h1", {"id": "regression_dir"})
        
        new_regression_log_path = regression_log_path
        new_regression_log_path.string = os.path.relpath(current_file)

        regression_log_path.replaceWith(new_regression_log_path)
        
        self.master_soup.body.append(current_soup.body)

    def save(self, path):
        '''
        @path file for log collection

        Open file specified by @path and writes all results collected into it

        Return nothing
        '''
        
        try:
            with open(path, 'w') as file:
                file.write(self.master_soup.prettify())
        except IOError:
            print("Can't open(w) file {} for results collection".format(self.master_file))