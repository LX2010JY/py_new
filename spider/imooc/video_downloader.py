#-*-coding:utf-8-*-
import os
import threading
import urllib
import sys
import conf
from urllib.request import urlretrieve

class File_Downloader(threading.Thread):
    '''
        继承 线程类，下载视频主要功能
    '''
    def __init__(self,fileInfo,id):
        '''
        :param fileInfo: 视频数据对象
        :param id:  线程编号
        '''
        threading.Thread.__init__(self)
        self._fileinfo = fileInfo
        self._id = id
        self.createdir()
    def run(self):
        fileurl = self._fileinfo.url[conf.STATE]
        filepath = self.filedir+os.sep+self._fileinfo.filename+'.mp4'
        urlretrieve(fileurl,filepath,self.Schedule)
    def createdir(self):
        '''
            下载视频之前，先创建视频文件夹
        :return:
        '''
        self.filedir = conf.PATH+self._fileinfo.subject+"("+conf.INFOR[conf.STATE]+")"
        if not os.path.exists(self.filedir):
            os.makedirs(self.filedir)

    def Schedule(self,blocknum,blocksize,totalsize):
        '''
        视频文件怎么可能一次性全部给你，分为多个数据块发送过来
        :param blocknum: 已下载的数据库
        :param blocksize:  数据库大小
        :param totalsize:  远程文件大小
        :return:
        '''
        per = 100.0 *blocknum*blocksize / totalsize
        if per>100:
            per = 100
        # 线程锁
        conf.LOCK.acquire()
        try:
            conf.PERLIST[self._id] = per #记录每个线程下载的进度
            nowsum = 0
            for item in conf.PERLIST:
                nowsum+=item
            str = u"当前下载进度:---------------->>>>{0:.2f}%".format(100*nowsum/conf.PERSUM)
            sys.stdout.write(str+"\r")
            sys.stdout.flush()
        except:
            print('下载失败！')
        finally:
            conf.LOCK.release()
