from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

device_1 = connect_device('android:///172.16.79.141?cap_method=javacap&touch_method=adb')

poco = AndroidUiautomationPoco(device_1, use_airtest_input=True, screenshot_each_action=False)


window = poco('com.songheng.eastnews:id/x1')
if window.exists():
    window.click()