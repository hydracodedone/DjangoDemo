import logging


class MyAbstractLogger(object):
    def __init__(self, file_name):
        self.logger = logging.getLogger(name=file_name)

