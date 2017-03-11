# -*- encoding:utf-8 -*-
import unicodecsv as csv
import os.path


class SVSource:
    def __init__(self, filename, name, cols, head=True, sep='\t'):
        if not os.path.isfile(filename):
            print 'file ' + filename + 'doesn not exist.'
            return None
        self.f = open(filename)
        self.sep = sep
        self.name = name
        self.cols = cols
        if head:
            self.f.readline()

    def get(self):
        s = self.f.readline().strip()
        if s == '':
            return s
        return s.split('\t')[self.cols]

    def __iter__(self):
        s = self.get()
        while s != '':
            yield s
            s = self.get()

    def reset(self):
        self.f.seek(0)

    def close(self):
        self.f.close()