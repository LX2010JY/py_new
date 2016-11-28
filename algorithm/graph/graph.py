from vertex import vertex
from queue2 import Queue
class graph(object):
    def __init__(self):
        self._vertexes = {}

    def add_vertex(self,key):
        '''
            将节点添加到图中，只有节点信息，没有边信息
        :param key:
        :return:
        '''
        if key in self._vertexes:
            return False
        else:
            self._vertexes[key] = vertex(key)
    def add_edge(self,from_key,to_key):
        '''
            添加边信息
        :param from_key: 出发节点
        :param to_key: 被指向节点
        :return:
        '''
        # 首先添加两个节点到 图节点字典中，如果已被添加，自动跳过，不会重复添加
        self.add_vertex(from_key)
        self.add_vertex(to_key)

        # 给出发节点 添加一个邻接的节点，出度加1
        self._vertexes[from_key].add_adjust(self._vertexes[to_key])

        # 给指向节点 入度加1
        self._vertexes[to_key].in_degree += 1
        self._vertexes[to_key].backup_in_degree +=1

    def BFS(self,key,func):
        next_vertex_queue = Queue()
        print('times')
        for k in self._vertexes:
            vertex = self._vertexes[k]
            # 标记当前节点被访问过的次数，第一次
            vertex.dist = -1
        result = []
        # 传入的key被访问了，状态变为0，加入下次访问队列
        self._vertexes[key].dist=0
        next_vertex_queue.enter(self._vertexes[key])
        while not next_vertex_queue.empty():
            # 如果节点访问队列不为空，则出队第一个节点
            vertex = next_vertex_queue.exit()
            result.append(func(vertex.key,vertex.dist))
            for adjust_vertex in vertex.adjust_list:
                if adjust_vertex.dist is -1:
                    adjust_vertex.dist = vertex.dist + 1
                    next_vertex_queue.enter(adjust_vertex)

        for k in self._vertexes:
            vertex = self._vertexes[k]
            if vertex.dist is -1:
                result.extend(self.BFS(vertex.key,func))
        return result


if __name__ == '__main__':
    graph = graph()
    graph.add_edge('v1','v2')
    graph.add_edge('v1','v3')
    graph.add_edge('v1','v4')
    graph.add_edge('v2','v4')
    graph.add_edge('v4','v3')
    graph.add_edge('v4','v7')
    graph.add_edge('v4', 'v6')
    graph.add_edge('v3', 'v6')
    graph.add_edge('v2', 'v5')
    graph.add_edge('v5', 'v4')
    graph.add_edge('v5', 'v7')
    graph.add_edge('v7', 'v6')

    print(graph.BFS('v7',lambda key,dist : (key,dist)))

