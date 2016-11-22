import json
import os
import requests as rq
import pandas as pd


class resof_lagou:

    '''
        获取拉勾网招聘信息
    '''
    def __init__(self,dir,kw):
        self.url = 'http://www.lagou.com/jobs/positionAjax.json?first=false&pn={0}&kd={1}'
        self.dir = dir
        self.kw = kw
        self.lagou_data = []

    def check_save_dir(self,path=''):
        '''
        检查指定的保存路径是否存在，如果不存在，创建一个
        :return:
        '''
        diretor = self.dir
        if path!='':
            diretor += path

        if not os.path.exists(diretor):
            os.makedirs(diretor)

    def getinfo(self):
        for i in range(1,31):
            print('抓取第{0}页'.format(i))
            lagou_url = self.url.format(i,self.kw)
            if lagou_url:
                # json_dumps 将python对象转为json格式 ， json_loads 将json格式转为python对象
                lagou_data = json.loads(rq.get(lagou_url).text)
                self.lagou_data.extend(lagou_data['content']['positionResult']['result'])
        # pandas 不懂
        position_data = pd.DataFrame(self.lagou_data)
        self.check_save_dir()
        print(type(position_data))
        position_data.to_csv("{0}招聘{1}职位.csv".format(self.dir,self.kw))
        print('数据已保存到本地')

kw = input('请输入抓取职位的关键字：')
lagou = resof_lagou('../file/lagou/',kw)
lagou.getinfo()
