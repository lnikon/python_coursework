import argparse

class SpyglassCollectorArgumentParser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Collector for spyglass logs')
        self.parser.add_argument('-b', '--base', type=str, help='Path to regressions base folder', required=True)
        self.parser.add_argument('-m', '--master', type=str, help='Path to master file where results should be collected', required=True)
        self.parser.add_argument('-s', '--search', type=str, default='spyglass.html', help='Spyglass logfile name', required=False)
    
    def parse(self):
        return self.parser.parse_args()