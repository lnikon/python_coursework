import os
import sys

from regression_collector import directory_walker
from spyglass_handler import DefaulSpyglassHandler
from arguments_parser import SpyglassCollectorArgumentParser

if __name__ == '__main__':
    print("========================================")
    print("Welcome to SpyglassCollector-3000!111!!!\n")

    arg_parser = SpyglassCollectorArgumentParser()
    args = arg_parser.parse()
    
    base_path = args.base
    print("Base path for log files is: {}".format(base_path))

    master_file = args.master
    print("Master file is: {}".format(master_file))

    search_for = args.search
    print("The searching and handling will be done for: {}".format(search_for))
    print("========================================\n")

    print("Initializing default handler for Spyglass...")
    default_handler = DefaulSpyglassHandler(master_file=master_file)
    print("Done!\n")

    print("Starting to apply default spyglass handler for {} files starting from {} base path".format(search_for, base_path))
    directory_walker(base_path, search_for, default_handler)
    print("Done!")
    print("========================================")    

    default_handler.save(master_file)
    print("\nResults were collected into {} master file".format(master_file))
    print("========================================")    