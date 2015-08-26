#airbb

init:
在目标ubuntu机器上运行init_env.sh脚本:
sh init_evn.sh
任何提问都Yes
环境基本更新完成
进入工作目录
git clone https://github.com/txdywy/airbb.git
进入airbb目录
python install.py安装所有python库
全部准备工作完成



在基本搞定环境工具后,我会开始初期的airbb后台框架重构.

这次我会把每个应用的模块,工具一点点添加进来,这样大家应该也会基本都熟悉这个过程了.

最初期的基本要求环境:
1. [Ubuntu] 最基本的环境,只需一台ubuntu14.04 server环境的虚拟机或vpc(比如aws,如果对aws感兴趣,我们可以之后再单独开展.目前只要本地有ubuntu环境就足够了)
我们的airbb框架需要了解的最基本知识(我只列出知识点,我的前提是大家只要能了解每块名词的大概含义和功能就好,随着项目进展,应该会对相应的细节越来越熟悉.
有些东西甚至不知其所以然也能用的很好.stackoverflow,google,baidu,github will be your best friends!(虽然有人不推崇这种鸟枪法,但是互联网世代的程序员能做到用好的就已经很棒了))Linux的基本知识,这个会在开发中慢慢吸收.

2. [Python] 我们基本的语言是python 2.7(最新为2.7.10,小版本号主要是修bug,不必特别在意),为目前最稳定的生产环境版本
python语言的特色是入门门槛低,productive极高,能零活优雅的处理很多看似复杂的问题.社区非常活跃,很丰富的开源库环境(你能想到的很多功能都有人实现).是介于面向对象和函数式语言之间的优秀生产力.只有到比较要求性能(异步)的后期阶段学习成本变高,但其实也主要是基于系统级别的(比如linux).初期http://www.diveintopython.net/ 这本电子书中偏逻辑功能的部分就基本足够了.(jave等oo背景的人会感觉编码更轻松了)可以了解一下python中的pip,简单说pip对于python就相当于apt-get对于ubuntu.是包管理器.我需要安装任何发布好的第三方python包都会通过它.

3. [Flask] python下我们会接触最频繁的web server框架http://flask.pocoo.org/.它提供给我们的就是整体网站代码如何布局,处理http请求的接口,返回页面等一切跟web有关的功能.

4. [SQLAlchemy] 网站服务会连接数据库.为了令代码清晰易读,且隐含和数据库(数据库的运维和交互都是复杂的事情)交互的工作,现代网站开发都会倾向使用orm.Sqlalchemy就是python中最优秀的orm库.我们使用时会进一步使用flask特有的flask-sqlalchemy库,将更多的数据库连接/session处理细节隐含起来,让程序员更多关注逻辑.

5. [Sqlite3] 简易的关系内存数据库,简洁小巧.测试和少量用户下足够用.方便迁移数据等.mysql用了之后就会发现还是很复杂的,需要很多相关知识,有相应的学习成本.因为我们使用了orm,如果真正上线时可以很轻松的切换到mysql.

6. [uwsgi] u这里是希腊字母miu, https://uwsgi-docs.readthedocs.org/en/latest/ 是一个用c++写成的web server容器,专门针对支持WSGI协议的python web server.本身参数虽然很多,但是我们开发时只需要很简单的一条启动服务器的命令即可.后续线上会和nginx交互,并添加更多功能参数.

7. [screen] 简单的shell命令行下窗口工具,基本作用是在你离线后,服务器还会维持一个窗口session,保存你命令行的现场(比如你起了一个服务器).等下回登录回来还能继续工作.http://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html  我们实际需要的命令很少.更流行和复杂的类似工具是tmux,视兴趣使用


综上,我会基于这里的基本环境构建一个能返回hello world的web server.稍后各人可讨论实施


A Micro Framework Test

in root folder airbb

python

from models.model_test import *

init_db()

this will create a local database airbb.db

sqlite3 airbb.db to access db with sql

quit python

in root folder airbb

uwsgi --http :1222 --module wsgi --callable app -M --process 4

U can access http://hostname/test/haha to get a test html page

http://hostname/test/haha?u=xxx will add a user data to Table TestUser, the page will be updated 



