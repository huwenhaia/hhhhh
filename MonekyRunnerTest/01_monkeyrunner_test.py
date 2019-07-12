# 让Jython环境支持中文注释
# -*- coding: utf-8 -*-

# 写脚本之前，先导入包
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice


# 使用monkeyrunner这个包去连接安卓设备
device = MonkeyRunner.waitForConnection()

# 获取要启动的app包名和启动页名字
app = "com.zhihu.android/.app.ui.activity.MainActivity"

# 启动这个app
device.startActivity(component=app)

# 去点击一下880,，800这个一点
device.touch(880, 880, MonkeyDevice.DOWN_AND_UP)


# 截图，并且保存到电脑上面
result = device.takeSnapshot()
result.writeToFile('c:\\Users\\SNake\\VSCodeProjects\\ljtest201906\\MonekyRunnerTest\\jietu.png','png')