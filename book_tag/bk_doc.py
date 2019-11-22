import os
import re


class Book(object):
    def __init__(self, SUMMARY_PATH):
        self.SUMMARY_PATH = SUMMARY_PATH

    @property
    def chapter(self):
        with open(self.SUMMARY_PATH, encoding='utf-8') as f:
            content = f.read()
            patten_path = r'\((.*?)\)'
            patten_name = r'\[(.*?)\]'
            names = re.compile(patten_name).findall(content)
            paths = re.compile(patten_path).findall(content)
        try:
            chapter = dict(map(lambda x, y: [x, y], names, paths))
        except BaseException as e:
            raise e
        return chapter


if __name__ == '__main__':
    book = Book('./5.1/PaaS平台/SUMMARY.md')
    print(book.chapter)