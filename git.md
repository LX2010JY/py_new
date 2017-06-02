#git 相关操作

#### 创建版本库
```
mkdir gitdir
cd gitdir
git init 
```
#### 基本操作
1. 查看状态 （有哪些文件修改了，添加了，等等）
```
git status
```
2. 查看文件具体修改了什么内容
```
git diff filename
```
3. 提交
```
git add filename/dirname
git commit -m 'desc'
```
4. 提交到远程仓库(如github)
```
git push
```
##### 查看提交历史
```
git log
```
以下是log部分内容，每一次提交都会有一个commit id可以靠其恢复之前的版本
>commit 02138eec7123180b5579085e7212edcc7feef0cc
>Author: lx2010jy <lx2010jy@163.com>
>Date:   Fri Jun 2 09:48:32 2017 +0800
>    '62'
但是很多时候不需要这么多内容，只需要id和每次提交的描述即可，可以加一个参数
```
git log --pretty=oneline
```
返回历史版本，通过commit id
```
git reset --hard 02138eec7123180b5579085e7212edcc7feef0cc #不用全写完，git会自动匹配，但是要保证能找到唯一的一个
```

```
# 版本库删除文件
git rm filename
```
### 错误的内容 错误的提交 后悔了，怎么办？
1. 将一个修改之后的还没有 add 的文件退回上一次提交的内容(即使文件被删除，也可以恢复)
```
# -- 必须加，因为checkout除了能够后退修改以外，还能切换分支
git checkout -- filename 

```
2. 如果已经 `git add `了，那么可以把暂存区的内容撤销掉
```
git reset HEAD filename
```

### Github 远程仓库使用基本步骤
#### 本地git与github之间的传输是需要加密的，需要给github你本地的ssh公钥
 1. 生成ssh秘钥
```
 $ ssh-keygen -t rsa -C "youremail@163.com"
```
 2. 执行上述命令后，会生成一个.ssh文件夹，将里面的id_rsa.pub 文件内容复制到[https://github.com/settings/keys](https://github.com/settings/keys)
 3. 在github添加一个git仓库![图片消失了](http://www.liaoxuefeng.com/files/attachments/0013849084639042e9b7d8d927140dba47c13e76fe5f0d6000/0)
 4. 在github添加一个仓库之后，此时 仓库没有内容，可以将其克隆到本地，也可以将其与本地仓库关联
    * 克隆
     ```bash
     git clone git@github.com:LX2010JY/py_new.git
     cd py_new
     XXXXXX操作
     git add .
     git commit -m ''
     git push
     ```
    * 关联(在本地新建一个py_new文件夹，并git init 初始化，进入py_new)
    ```bash
    mkdir py_new
    cd py_new
    git init 
    git remote add origin git@github.com:LX2010JY/py_new.git
    #将内容推送到远程仓库(第一次提交需要将本地分支和远程库的master对应起来，所以加 -u ，之后提交不需要)
    git push -u origin master
    ```

# 最难的点 分支
![oh my god,pic is run away](http://www.liaoxuefeng.com/files/attachments/0013849087937492135fbf4bbd24dfcbc18349a8a59d36d000/0)
1. git用master指向最新的提交，再用HEAD指向master(目前所在的分支)
2. 当新建一个分支dev时，git新建一个指针，指向master相同的提交，而HEAD此刻指向dev，表示此刻在dev分支上
```
git branch dev #新建分支
git checkout dev #切换到dev分支上
git checkout -b dev #新建分支，并且切换到dev分支上，相当于上面两条命令
git branch #查看所有分支当前所在的分支前面有一个小星号
```

![gone](http://www.liaoxuefeng.com/files/attachments/001384908811773187a597e2d844eefb11f5cf5d56135ca000/0)
3. 此刻修改dev分支的内容，进行提交之后，dev指针往前移动一步，但是master依旧不变
![gone](http://www.liaoxuefeng.com/files/attachments/0013849088235627813efe7649b4f008900e5365bb72323000/0)
4. #### 最简单的**合并**
    此刻dev指向了最新的提交，但是master未变，所以合并master和dev，只需要吧master指针指向最新提交即可 此称为快速合并
```
git merge dev #合并dev到当前分支
#合并之后删除dev分支
git branch -d dev
```
![gone](http://www.liaoxuefeng.com/files/attachments/00138490883510324231a837e5d4aee844d3e4692ba50f5000/0)
5. #### 合并冲突
    当master和dev都进行了新的提交但是修改内容不同时，合并不能直接 快速合并，而且会发生冲突，此刻需要手动解决冲突

![](http://www.liaoxuefeng.com/files/attachments/001384909115478645b93e2b5ae4dc78da049a0d1704a41000/0)
下列符号表示冲突部分
```
<<<<<<< HEAD #此表示当前分支的内容
Creating a new branch is quick & simple.
=======      # 此为分割线
Creating a new branch is quick AND simple.
>>>>>>> feature1 #此表示被合并的分支内容
```
修改了冲突文件之后，在此提交，即可完成合并
```
git add .
git commit -m ''
```
最后删除分支
```
git branch -d feature1

```
![](http://www.liaoxuefeng.com/files/attachments/00138490913052149c4b2cd9702422aa387ac024943921b000/0)


如果新建了分支不想合并 而且直接删除的话
```
git branch -d feature #这样是会报错的，提示你合并之后才能删除
git branch -D feature #所以强制删除
```