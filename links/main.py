from arguments_parser import ArgumentsParser
from helper import LinksGenerator
from links_parser import LinkInfo, LinksParser

if __name__ == '__main__':
    print("Dude, listen here... YOU DON'T NEED TO WRITE URL REGEX BY YOURSELF!1!!1!!!... thanks :)")
    arg_parser = ArgumentsParser()
    args = arg_parser.parse()

    links = args.links
    links_file = args.file
    generate = args.generate

    if generate:
        link_gen = LinksGenerator()
        link_gen.generate_links_file(generate)
        exit(0)
    elif not links:
        try:
            with open(links_file, 'r') as file:
                links = []
                for _, line in enumerate(file):
                    links.append(file.readline())
        except IOError:
            print("Unable to open links file {}".format(links_file))
            exit(-1)

    parser = LinksParser(links)
    parser.parse()
    links_info = parser.get()
    for info in links_info:
        print(info)
