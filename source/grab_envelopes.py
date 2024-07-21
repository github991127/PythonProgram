from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    "platformName": "Android", # 系统
    "platformVersion": "8.0.0", # 系统版本号
    "deviceName": "m5s", # 设备名
    "appPackage": "com.tencent.mm", # 包名
    "appActivity": ".ui.LauncherUI", # app 启动时主 Activity
    'unicodeKeyboard': True, # 使用自带输入法
    'noReset': True # 保留 session 信息，可以避免重新登录
}

# 判断元素是否存在
def is_element_exist(driver, by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:
        return False
    else:
        return True

# 删除领取后的红包记录
def del_red_envelope(wait, driver):
    # 长按领取过的红包
    r8 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/r8")))
    TouchAction(driver).long_press(r8).perform()
    # 点击长按后显示的删除
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/gam"))).click()
    # 点击弹出框的删除选项
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/doz"))).click()

if __name__ == '__main__':
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    # 设置等待
    wait = WebDriverWait(driver, 500)
    g73 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/g73")))
    g73.click()
    print("进入了红包群")
    while True:
        # 有红包则点击
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/r8"))).click()
        print("点击了红包")
        # 判断红包是否被领取
        is_open = is_element_exist(driver, "id", "com.tencent.mm:id/den");
        print("红包是否被领取：", is_open)
        if is_open == True:
            # 红包未被领取，打开红包
            wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/den"))).click()
            # 返回群聊
            wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/dm"))).click()
            # 删除领取过的红包记录
            del_red_envelope(wait, driver)
        else:
            # 返回群聊
            driver.keyevent(4)
            # 删除领取过的红包记录
            del_red_envelope(wait, driver)

