关于Pycharm同步git
查看git config配置，在终端中输入以下命令：
git config --list
然后把自己的git账户添加上
git config --global user.name 你的git账户名
git config --global user.email 你注册git的邮箱
添加完成可以 git config –list 查看信息是否匹配
然后打开pycharm进行配置，依次点击
file--setting--version control—git  这里是检测到本地安装的git应用程序
file--setting--version control—github 这里需要在此对话框中输入用户名和密码
PS：右下角都有个test，点击test可以看到是否测试成功
 创建github仓库，假设在本地已经有项目代码
点击Vcs——Import into Version Control——Share Project on Github
next会弹出对话框让你输入名字简介啥的
next点击share
next又一个对话框让你选择哪些文件需要被同步，选好后，在下面的commit Message可以输入自己的信息
next点OK，你的代码就提交到github上了
next你可以看一下
 关于修改后的文件提交
对修改后的文件或目录点击右键： Git—Commit File...
填好commit的信息后，点击下面的commit and Push，可以直接提交到github
关于git同步到本地Python
这个叫做clone
目录：Vcs——Checkout from Version Control——Github
嗯对，就是这个，我还没研究，自行百度吧
