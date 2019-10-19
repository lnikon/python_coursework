from urllib.parse import urlparse
import argparse

class LinkInfo(object):
    def __init__(self, scheme='', host='', port='', res_path=''):
        self.scheme = scheme
        self.host = host
        self.port = port
        self.res_path = res_path

    def __str__(self):
        return '<{}, {}, {}, {}>'.format(self.scheme, self.host, self.port, self.res_path)

class LinksParser(object):
    def __init__(self, links=[]):
        self.links = links
        self.links_info=[LinkInfo]        

    def parse(self, lines=[]):
        for link in self.links:
            link_info = LinkInfo()

            match = urlparse(link)

            link_info.scheme = match.scheme
            link_info.host = match.hostname
            link_info.port = match.port
            link_info.res_path = match.path

            self.links_info.append(link_info)

    def get(self):
        return self.links_info