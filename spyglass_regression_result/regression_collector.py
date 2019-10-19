import sys
import os
import spyglass_handler

def directory_walker(base_path, search_for, handler):
    '''
    @base_path  from where start walking

    @search_for  name(s) of file(s) to which @handler should be applied

    @handler     object with handle method which should be applied to the files during walk


    Walk recursively on directories starting from specified base path and
    and apply specified handler to all files equal to search_for
    '''

    for dirpath, _, files in os.walk(base_path):
        for file_name in files:
            if file_name == search_for:
                file_to_process = dirpath + '/spyglass.html'
                print("Processing of " + file_to_process, end='')
                handler.handle(file_to_process)
                print("... Done!")