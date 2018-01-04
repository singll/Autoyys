### 阴阳师-护肝小工具
## 简介
这个项目是因为我没时间肝阴阳师，所以写出来的一个小脚本，目前只支持自动刷御魂
如果发现运行不正常，可以在issues里面提出来，我觉得分辨率可能是个问题，毕竟本人很穷，只有一个手机
PS:此项目是受到微信跳一跳的项目启发，然后做的，附上跳一跳地址
> https://github.com/wangshub/wechat_jump_game

##需要工具
* 电脑(可以任意系统，不过本人只有win10，其他系统可能会有小问题)
* 手机
* Python [点击下载](https://www.python.org/downloads/release/python-364/)
* ADB [点击下载](https://adb.clockworkmod.com/)
## 详细步骤
# 1.安装Python
[安装教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)
# 2.安装ADB
* 1.点击next
![](https://singll.github.io/Image/adb_step/adb_step1.png)
* 2.这一步需要记住你的安装位置，如果不好记可以自己放在容易找到的地方
![](https://singll.github.io/Image/adb_step/adb_step2.png)
* 3.点击next进行安装
![](https://singll.github.io/Image/adb_step/adb_step3.png)
* 4.安装完成，点击close
![](https://singll.github.io/Image/adb_step/adb_step4.png)
* 5.然后我们进行环境变量配置（我这里是win10的步骤，其他系统可以百度“win7”（系统名）+“环境变量配置”），在我的电脑，右键，进入<b>属性</b>
![](https://singll.github.io/Image/adb_step/adb_step5.png)
* 6.点击<b>高级系统设置</b>
![](https://singll.github.io/Image/adb_step/adb_step6.png)
* 7.点击<b>环境变量</b>
![](https://singll.github.io/Image/adb_step/adb_step7.png)
* 8.点击<b>新建</b>
![](https://singll.github.io/Image/adb_step/adb_step8.png)
* 9.变量名：ADB_HOME 变量值：刚才记住的安装路径，我这里是默认的安装位置
![](https://singll.github.io/Image/adb_step/adb_step9.png)
* 10.在下面找到path，然后点击<b>编辑</b>
![](https://singll.github.io/Image/adb_step/adb_step10.png)
* 11.点击<b>新建</b>，然后输入%ADB_HOME%，之后要注意，要把能点的<b>确定都点了</b>，这样配置才能生效
![](https://singll.github.io/Image/adb_step/adb_step11.png)
* 12.我们来验证一下配置是否生效，在左下角搜索"cmd"（也可以用快捷键win+r），进入命令提示符
![](https://singll.github.io/Image/adb_step/adb_step12.png)
* 13.在cmd里面输入：adb version ，输出同图片说明配置正确
![](https://singll.github.io/Image/adb_step/adb_step13.png)
# 3.下载项目
* 1.在本页面，点击下载，然后解压到任意位置
![](https://singll.github.io/Image/example/example_downproj.png)
* 2.在解压之后的文件夹里，按住<b>Shift</b>键，然后按<b>右键</b>进入<b>在此处打开 Powershell 窗口</b>(或者<b>cmd</b>窗口)
![](https://singll.github.io/Image/example/example_rightmenu.png)
* 3.界面如下图，其他系统或者cmd不再详细列出。类似这种界面就都可以。 ![](https://singll.github.io/Image/example/example_powershell.png)
* 4.输入代码之前要保证python已经安装成功，然后输入<b>pip install -r requirements.txt</b>，输出如下图即可
![](https://singll.github.io/Image/example/example_installpil.png)
# 4.调试ADB
* 1.将手机用<b>USB</b>连上<b>电脑</b>
* 2.输入<b>adb devices</b>,如果输出如下图，则可以跳过下步
![](https://singll.github.io/Image/example/example_adbdevices.png)
* 3.如果上面输出不对，请将安卓手机的 USB 调试模式打开，设置》更多设置》开发者选项》USB 调试
# 5.开始肝
* 在手机上打开阴阳师，然后到下图界面，这里要注意，一定要把<b>阵容锁定</b>（老司机都懂得）
![](https://singll.github.io/Image/example/example_start.png)
* 在<b>powershell</b>输入<b>python autoyys.py</b>
![](https://singll.github.io/Image/example/example_run.png)
然后就可以愉快的 看电视剧/电影 了~~，当然，这里还支持定制话的运行。
* 比如<b>python autoyys.py 35 10</b> 这里<b>35</b>是你刷魂十的最快速度，<b>10</b>是刷的次数，比如你可以输入100，这样程序就会在刷完100次之后自动停止0.0
## TODO LIST
PS:我先去忙别的了，这个等以后有时间再来完善
- [ ] 支持组队刷御魂、觉醒等
- [ ] 支持自动刷探索
