# cmdb
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

项目本来是叫webssh，去年那时只从CMDB中提取webssh功能，这次加了些功能后就干脆叫cmdb算了。

* 特色:

        基于django、python2.7开发，部署简单。
        1. 本项目功能实用/通用。为方便阅读理解，代码备注详细，适合将代码/功能集成到各自系统中二次开发，也很适合新手学习/入门。
        2. webssh终端，该有功能基本都有，websocker基于django的channels模块，和http在同一监听端口，减少模块依赖安装
        3. websftp文件操作，基于elfinder，上传下载，在线图片预览、文本编辑，文本语法高亮着色（基于ace编辑器）
        4. 软件终端（SSH透明堡垒机），支持从网页跳转到Xshell，比webssh/sftp更方便，需文件操作时可以从Xshell启动Xftp进行
        如果客戶端是Linux系統，跳转到SecureCRT和FX。
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

# License
<a href="http://www.gnu.org/licenses/lgpl-2.1.html" target="_blank">LGPL2.1</a> 
<a href="https://github.com/996icu/996.ICU/blob/master/LICENSE" target="_blank">996</a>
