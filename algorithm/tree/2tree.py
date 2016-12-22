#coding:utf-8
'''
    构建了一颗二叉树，以及使用 先序遍历、中序遍历、后序遍历 显示
'''
class Node(object):
    def __init__(self,element=-1,lchild=None,rchild=None):
        '''
            树的节点定义
        :param element:
        :param lchild:
        :param rchild:
        '''
        self.element = element
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        '''
            初始化根节点
        '''
        self.root = Node()
    def add(self,e):
        '''添加节点'''
        node = Node(e)
        if self.root.element == -1:
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if treeNode.lchild == None:
                    # 先判断根节点的左节点是否为空，如果为空，则设置左节点为node
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == None:
                    # 判断根节点的右节点是否为空，如果为空，则设置右节点为node
                    treeNode.rchild = node
                    return
                else:
                    # 如果根节点已经满了，则将其左右节点加入队列，先左后右，节点的添加是按照层次遍历的规则来的
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)
    def preorder(self,root):
        '''
            先序遍历
        :param root: 节点
        :return:
        '''
        if root == None:
            return
        # 递归，先遍历根节点，再找左子树，再找右子树
        print(root.element,end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def centerorder(self,root):
        '''
            中序遍历
        :param root: 节点
        :return:
        '''
        if root == None:
            return
        self.centerorder(root.lchild)
        print(root.element,end=' ')
        self.centerorder(root.rchild)

    def postorder(self,root):
        '''
            后序遍历
        :param root: 节点
        :return:
        '''
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.element,end=' ')

    def preorder_stack(self,root):
        '''
            通过栈实现的递归，先序遍历
        :param root:
        :return:
        '''
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.element,end=' ')
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild


if __name__ == '__main__':
    elems = range(10)
    tree = Tree()
    print('\n'+'-'*10+'层次遍历'+'-'*10)
    for elem in elems:
        print(elem,end=' ')
        tree.add(elem)

    print('\n'+'-'*10+'先序遍历'+'-'*10)
    tree.preorder(tree.root)
    print('\n' + '-' * 10 + '中序遍历' + '-' * 10)
    tree.centerorder(tree.root)
    print('\n' + '-' * 10 + '后序遍历' + '-' * 10)
    tree.postorder(tree.root)

    print('\n'+'-'*10+'先序遍历（栈）'+'-'*10)
    tree.preorder_stack(tree.root)