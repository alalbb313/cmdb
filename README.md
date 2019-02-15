# cmdb
项目本来是叫webssh，去年那时只从CMDB中提取webssh功能，这次加了些功能后就干脆叫cmdb算了。

* 特色:

        基于django、python2.7开发，部署简单。
        1. 本项目功能实用/通用。为方便阅读理解，代码备注详细，适合将代码/功能集成到各自系统中二次开发，也很适合新手学习/入门。
        2. webssh终端，该有功能基本都有，websocker基于django的channels模块，和http在同一监听端口，减少模块依赖安装
        3. websftp文件操作，基于elfinder，上传下载，在线图片预览、文本编辑，文本语法高亮着色（基于ace编辑器）
        4. 软件终端（SSH透明堡垒机），支持从网页跳转到Xshell，比webssh/sftp更方便，需文件操作时可以从Xshell启动Xftp进行
        5. docker管理，支持跨多宿主机管理容器，支持创建二层容器网络（二层桥接和macvlan，
        相当于使容器网卡和所属宿主机网卡接在同一交换机上，而不跨路由/NAT），
        容器创建好后无需映射端口到宿主机而可供其它主机/跨宿主机容器访问，详情帮助见 根目录\c\help\docker\docker二层网络.txt
        6. Elasticsearch索引管理
        7. 支持otp二维码验证登陆

* 环境：

        centos6/7
        python2.7

* 搭建：

        一. 容器部署方式（推荐，如果是生产方式，建议在外部部署使用mysql、redis）
        # 拉取镜像(基于centos7创建，pull下载169.2M)
        docker pull py2010/cmdb
        # 启动容器，部署完成
        docker run -it -p 8088:8088 -p 2222:2222 py2010/cmdb
        (如果为便于git更新，项目代码放在宿主机上的/xxx/xxx，加 -v /xxx/xxx:/kf/dj 参数挂载目录)
        二、如果不使用容器，手工部署也很简单，requirements.txt中写得比较详细，
        准备centos6或7（估计unbuntu也行，没实际布署测试过），
        python2.7安装requirements.txt中的模块，安装redis。
        下载项目代码，在项目根目录执行c/d start启动django网站。
        
        容器或centos系统布署并启动好了后， 访问网页，http://ip:8088，用户名/密码：admin/admin@2019


# 顺便建了个群，欢迎加入
* QQ群号 972746120 <a target="_blank" href="https://jq.qq.com/?_wv=1027&k=5aa2ERr"><img border="0" src="c/group.png"  alt="django开发交流" title="django开发交流"></a>
* <a target="_blank" href="https://jq.qq.com/?_wv=1027&k=5aa2ERr"><img border="0" src="c/qq.png"  alt="django开发交流" title="django开发交流"></a>



# 截图：
* 软件终端
![xshell](c/xshell.gif  "xshell")
* 主机列表
![](https://github.com/py2010/webssh/raw/master/host.png)

* 网页SFTP (在线文本编辑)
![websftp](c/websftp.png  "websftp")
* 网页SFTP (图片预览)
![websftp](c/websftp2.png  "websftp")
* 网页终端
![](https://github.com/py2010/webssh/raw/master/webssh.png)
![](https://github.com/py2010/webssh/raw/master/webssh2.png)
![](https://github.com/py2010/webssh/raw/master/ssh.png)
![](https://github.com/py2010/webssh/raw/master/top.png  "top")
![vi](https://github.com/py2010/webssh/raw/master/vi.png  "vi")

* 容器添加
![](c/dk_1.png)
* 容器管理列表
![](c/dk_2.png)
* 容器终端(webssh)
![](c/dk_3.png)
* 镜像管理列表
![](c/dk_img.png)
* 容器网络列表
![](c/dk_net.png)
* 容器网络添加(支持二层网络)
![](c/dk_net2.png)



# 感谢：
webssh、websftp项目，借签 <a href="https://github.com/jimmy201602/webterminal" target="_blank">jimmy201602/webterminal</a>
# 说明
原感谢中，写有三个借签项目，包含“jumpserver/coco”和“hequan2017/cmdb”，感谢二位作者提供的开源项目
为防引起不必要的误解和恶意嘲讽，现已删除，fork项目也取消。

(
“jumpserver/coco”，有三个文件从coco改来的，cmdb/ssh/目录下sshd.py sftpinterface.py sshinterface.py
“hequan2017/cmdb”，主要说这个，用的是html模板，前年开发CMDB时当时网上有二三个基于Inspinia的模板，
那时看的何全的cmdb的后台用的是site1.0，我因想快速开发，不开发前端页面，
有些添加管理页面只有后台admin，所以当时是想统一admin后台和Inspinia模板，配色/风格保持一致。
说实话，当前模板历史上真正开发量最大的有二人，一个是首个将Inspinia模板应用到CMDB中的人，感谢。
另一个就是我，并且我觉得Inspinia模板是现成的，但是要将admin后台模板风格/配色和前端Inspinia模板一致，我的工作量是最大的！

真他妈的见了鬼了，第三方群某些人总是阴阳怪气，只要讲到我的项目，就是集成、整合、CV工程师……
这些人叫得欢，其实压根都没实际用过，老是大嘴，讲个几次也就算了，很正常，有人的地方就有江湖。
逢我必说，真他妈的烦，人家作者本人都不坑声。之前我github开发项目，只要有借签、参考，都会fork。
你借签、参考别人的项目时，会不会在readme中说明？会不会fork尊重一下？
大家都是python系统开发的，你要是不懂开发，看说明也跟着起哄挖苦也就算了，真变态！
自己开发个普通系统，平平常常，网上一堆类似的系统，经常在群中发链接宣传，真是服了。
我这项目都没在群里发链接宣传，只顺便发过一次自我解嘲一下，
项目是从我在公司开发的CMDB中提取的，半年/一年从公司CMDB中提取改动一次，压根就没想怎么样，
码云认可我的项目，首页推荐，你也可以开发个去首页推荐啊，妒忌个毛？
)



<!-- github不允许超级链接在新窗口中打开？ -->
<!-- * 本项目堡垒机，借签的 [jumpserver/coco](https://github.com/jumpserver/coco?_blank)
* webssh、websftp，借签 [jimmy201602/webterminal](https://github.com/jimmy201602/webterminal?_blank)
* HTML模板结构，借签 [hequan2017/cmdb](https://github.com/hequan2017/cmdb?_blank) -->
