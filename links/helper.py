import random

class LinksGenerator(object):
    def __init__(self):
        self.link_cnt = random.randint(50, 401)
        self.scheme = ['http://', 'https://', 'ftp://', 'market://']
        self.host = ['pythoncentral.io', 'github.com', 'python.org', 'yandex.ru']
        self.port = ['80', '90']
        
        self.res_paths = []
        for res_cnt in range(101):
            path = '/page' + str(res_cnt)
            for res_len in range(11):
                path += "/res" + str(res_len)
            self.res_paths.append(path)

    def generate_links_file(self, path):
        try:
            with open(path, 'w') as file:
                file.truncate(0)

                link_cnt = self.link_cnt
                while link_cnt > 0:
                    link_cnt -= 1                
                    
                    scheme = random.choice(self.scheme)
                    host = random.choice(self.host)

                    port = ''
                    if random.randint(0, 2):
                        port = ':' + random.choice(self.port)

                    res_path = random.choice(self.res_paths)

                    file.write(scheme + host + port + res_path + '\n')    
        except IOError:
            print("IOError occured during generation of links")
