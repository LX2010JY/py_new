# -*-coding:utf-8-*-
class FileInfo(object):
    '''
        一堆感觉没啥用的装饰器
    '''

    def __init__(self):
        self._subject = '' #教程名称
        self._filename=''  # 课程名称
        self._mid = ''     # 课程ID号
        self._url = {}      #下载链接
    @property
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self,value):
        self._subject = value
    @property
    def filename(self):
        return self._filename
    @filename.setter
    def filename(self,value):
        self._filename = value
    @property
    def mid(self):
        return self._mid
    @mid.setter
    def mid(self,value):
        self._mid = value
    @property
    def url(self):
        return self._url
    @url.setter
    def url(self,value):
        self._url = value
