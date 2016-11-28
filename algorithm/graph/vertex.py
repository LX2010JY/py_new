class vertex(object):
    def __init__(self,key,weight=None):
        '''

        :param key:
        :param weight:
        '''
        self.key = key
        self.in_degree = 0
        self.out_degree = 0
        self.weight_list = []
        self.adjust_list = [] #邻接节点列表
        self.backup_in_degree = self.in_degree
        self.backup_out_degree = self.out_degree
        self.dist = 0

    def add_adjust(self,to_vertex):
        '''
            给节点添加邻接节点
        :param to_vertex: 本节点邻接的另一个节点
        :return:
        '''
        self.adjust_list.append(to_vertex)
        self.out_degree +=1
        self.backup_out_degree += 1
        