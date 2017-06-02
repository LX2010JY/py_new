#MarkDown 部分语法
### 标题
* 以井号表示标题 一级标题一个井号`# 一级标题`
- 二级标题两个井号`## 二级标题` 并以此类推
### 列表
1. 有序列表 直接使用数字并在后面加一个点和空格 即为有序列表 如`1. `
2. 无序列表 使用 减号加空格`- `或者信号加空格 `* `
### 引用（blockquote）
> 使用`> 引用内容` 即可引用
### 图片与链接
1. `![]()` 图片和链接很相似 只是图片前面多了一个感叹号 ![](http://ww2.sinaimg.cn/large/6aee7dbbgw1efffa67voyj20ix0ctq3n.jpg)
2. `[]()` 链接 中括号为显示内容，括号为链接地址 [你好呀](http://www.baidu.com)
### 字体
1. **粗体** 两个星号（一边两个）中间为粗体 `**粗体**`
2. *斜体italic* 一个星号包裹中间 为斜体 (怎么只有英文有用) `*italic*`
### 代码块 代码段
1. 使用 两个` ``` `包裹 中间内容即可写代码 例如：
```php
<?php
    class aimplementsb implements b {
        protected $abc;
        function __construct() {
            $this->abc = 111;
        }
        function bfunc() {
            pass
        }
    }
```
2. 使用 两个 ` ` `包裹，中间内容即可写代码段，特殊字符等等
