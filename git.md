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
将一个修
