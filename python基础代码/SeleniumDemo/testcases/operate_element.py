# selenium定位页面元素
from selenium import webdriver
import openBrowser
import time

def operate_element_by_id():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 往输入框里输入新闻
    driver.find_element_by_id('kw').send_keys('新闻')
    # 点击'百度一下'按钮
    driver.find_element_by_id('su').click()
    time.sleep(1000)

def operate_element_by_name():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 往输入框里输入新闻
    driver.find_element_by_name('wd').send_keys('新闻')
    # 点击'百度一下'按钮
    driver.find_element_by_id('su').click()
    time.sleep(1000)

def operate_element_by_class_name():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 往输入框里输入新闻
    driver.find_element_by_class_name('s_ipt').send_keys('新闻')
    # 点击'百度一下'按钮
    driver.find_element_by_class_name('s_btn').click()
    time.sleep(1000)

def operate_element_by_link_text():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 点击'新闻'链接
    driver.find_element_by_link_text('新闻').click()
    time.sleep(1000)

def operate_element_by_partial_link_text():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 点击'新闻'链接
    driver.find_element_by_partial_link_text('新').click()
    time.sleep(1000)

def operate_element_by_css_01():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 元素有id属性的时候，通过css来定位
    driver.find_element_by_css_selector('#kw').send_keys('新闻')
    # 点击'百度一下'按钮
    driver.find_element_by_class_name('s_btn').click()
    time.sleep(1000)

def operate_element_by_css_02():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 元素有class属性的时候，通过css来定位
    driver.find_element_by_css_selector('.s_ipt').send_keys('新闻')
    # 点击'百度一下'按钮
    driver.find_element_by_class_name('s_btn').click()
    time.sleep(1000)

def operate_element_by_css_03():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 元素有class属性的时候，通过css来定位
    driver.find_element_by_css_selector('input[name="wd"]').send_keys('新闻')
    # 点击'百度一下'按钮
    driver.find_element_by_class_name('s_btn').click()
    time.sleep(1000)

def operate_element_by_css_04():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 元素有class属性的时候，通过css来定位
    driver.find_element_by_css_selector('input[name="wd"]').send_keys('新闻')
    # 点击'百度一下'按钮
    driver.find_element_by_css_selector('input[value="百度一下"]').click()
    time.sleep(1000)

def operate_element_by_css_05():
    driver = openBrowser.open_chrome()
    driver.get('https://weibo.com/login.php')
    time.sleep(5)

    # 通过css绝对路径来定位元素
    # html>body>div.B_unlog>div.WB_miniblog>div.WB_miniblog_fb>div#weibo_top_public
    driver.find_element_by_css_selector('html>body>div.B_unlog>div.WB_miniblog>div.WB_miniblog_fb>div#weibo_top_public>div>div>div.gn_search_v2>input').send_keys('新闻')
    time.sleep(1000)

def weibo_login():
    driver = openBrowser.open_chrome()
    driver.get('https://weibo.com/')
    time.sleep(10)

    # 通过xpath绝对路径来定位元素
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[1]/div/input').send_keys('123456')
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[2]/div/input').send_keys('123456')
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]/a').click()
    time.sleep(1000)

def weibo_login_01():
    driver = openBrowser.open_chrome()
    driver.get('https://weibo.com/')
    time.sleep(10)

    # 通过xpath相对路径来定位元素
    driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span').click()
    time.sleep(1000)

def operate_element_by_tag_name():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    # 通过tag_name来定位元素
    driver.find_element_by_xpath('//*[@id="form"]/span[1]').find_element_by_tag_name('input').send_keys('新闻')
    driver.find_element_by_xpath('//*[@id="form"]/span[2]').find_element_by_tag_name('input').click()
    time.sleep(1000)

def get_text():
    driver = openBrowser.open_chrome()
    driver.get('https://www.baidu.com')

    text = driver.find_element_by_link_text('新闻').text
    print('text:', text)

def get_element_attribute():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    value = driver.find_element_by_id('su').get_attribute('value')
    print('value:', value)

def get_current_url():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    url = driver.current_url
    print('url:', url)

def get_window_handle():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    handle = driver.current_window_handle
    print('handle:', handle)

def checkbox_is_selected():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/')
    time.sleep(8)

    selected = driver.find_element_by_id('login_form_savestate').is_selected()
    print('selected01:', selected)
    driver.find_element_by_id('login_form_savestate').click()
    selected = driver.find_element_by_id('login_form_savestate').is_selected()
    print('selected02:', selected)

    time.sleep(1000)

def input_clear():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')

    driver.find_element_by_id('kw').send_keys('新闻')
    driver.find_element_by_id('su').click()
    time.sleep(2)

    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su').click()

    driver.quit()

def get_title():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')

    title = driver.title
    print('title:', title)

def get_back():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')

    driver.find_element_by_id('kw').send_keys('新闻')
    driver.find_element_by_id('su').click()
    time.sleep(2)

    driver.back()
    driver.forward()

def move_element():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')

    # 导入ActionChains类
    from selenium.webdriver.common.action_chains import ActionChains
    element = driver.find_element_by_id('s-usersetting-top')
    # 这里使用move_to_element模拟将鼠标悬停在元素'设置'处
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(3)
    driver.find_element_by_link_text('高级搜索').click()
    time.sleep(3)

    driver.quit()

def get_select():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/signup/signup.php')
    time.sleep(3)

    # 导入Select类
    from selenium.webdriver.support.select import Select
    element = driver.find_element_by_class_name('year')
    # index索引是从0开始,选择1则表示选择第二个选项
    Select(element).select_by_index(1)
    time.sleep(3)

    driver.quit()

def get_select_by_value():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/signup/signup.php')
    time.sleep(3)

    # 导入Select类
    from selenium.webdriver.support.select import Select
    element = driver.find_element_by_class_name('year')
    # 第二个选项对应的value的值是2019
    Select(element).select_by_value('2019')
    time.sleep(3)

    driver.quit()

def get_select_by_visible_text():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/signup/signup.php')
    time.sleep(3)

    # 导入Select类
    from selenium.webdriver.support.select import Select
    element = driver.find_element_by_class_name('year')
    # 第二个选项显示的文本是2019
    Select(element).select_by_visible_text('2019')
    time.sleep(3)

    driver.quit()

def get_select_options():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/signup/signup.php')
    time.sleep(3)

    # 导入Select类
    from selenium.webdriver.support.select import Select
    element = driver.find_element_by_class_name('year')
    ops = Select(element).options
    for i in ops:
        print(i.text)

    driver.quit()

def get_all_selected_options():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/signup/signup.php')
    time.sleep(3)

    # 导入Select类
    from selenium.webdriver.support.select import Select
    element = driver.find_element_by_class_name('year')
    ops = Select(element).all_selected_options
    for i in ops:
        print(i.text)

    driver.quit()

def get_first_selected_option():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/signup/signup.php')
    time.sleep(3)

    # 导入Select类
    from selenium.webdriver.support.select import Select
    element = driver.find_element_by_class_name('year')
    Select(element).select_by_index(3)

    print(option.text)

    driver.quit()

def send_keys_by_js():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    js = "document.getElementById('kw').value='新闻'"
    driver.execute_script(js)
    time.sleep(3)

    driver.quit()

def scroll_by_js():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    driver.find_element_by_id('kw').send_keys('新闻')
    driver.find_element_by_id('su').click()
    time.sleep(3)
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(10)

    driver.quit()

def operate_keyboard():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    # driver.find_element_by_id('kw').send_keys('seleniumtest')
    # time.sleep(3)
    # 导入Keys类
    from selenium.webdriver.common.keys import Keys
    # driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id('kw').send_keys('seleniumtest' + Keys.BACK_SPACE)

    time.sleep(3)

    driver.quit()

def qq_email_login():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://mail.qq.com/cgi-bin/loginpage')
    # 先切换到iframe
    driver.switch_to.frame('login_frame')

    driver.find_element_by_id('u').send_keys('1222222')
    driver.find_element_by_id('p').send_keys('111111')
    driver.find_element_by_id('login_button').click()

    time.sleep(3)

    driver.quit()

def get_cookie():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://www.cnblogs.com/')
    print('before login:')
    # 打印全部cookie
    for cookie_detail in driver.get_cookies():
        print(cookie_detail)

    print('--------------------------')

    # 登录用户
    driver.find_element_by_link_text('登录').click()
    driver.find_element_by_id('mat-input-0').send_keys('zhaokch')
    driver.find_element_by_id('mat-input-1').send_keys('qwe123456')
    driver.find_element_by_css_selector('body > app-root > div > mat-sidenav-container > mat-sidenav-content > div > div > app-sign-in > app-content-container > mat-card > div > form > div > button').click()

    time.sleep(5)

    print('after login:')
    # 打印登录后的全部cookie
    for cookie_detail in driver.get_cookies():
        print(cookie_detail)

    print('--------------------------')

    driver.quit()

def operate_slider():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://passport.ctrip.com/user/reg/home')
    # 点击同意协议按钮
    driver.find_element_by_link_text('同意并继续').click()

    # 获取滑块元素
    from selenium.webdriver.common.action_chains import ActionChains
    slider = driver.find_element_by_class_name('cpt-drop-btn')
    print(slider.size['width'])
    print(slider.size['height'])

    # 获取滑块区域元素
    element = driver.find_element_by_id('slideCode')
    print(element.size['width'])
    print(element.size['height'])

    # 鼠标左键按下不放
    ActionChains(driver).click_and_hold(slider).perform()
    # 平行移动滑块到滑块区域到最右端
    ActionChains(driver).drag_and_drop_by_offset(slider, element.size['width'], 0).perform()
    time.sleep(5)

def screenshot():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('https://passport.ctrip.com/user/reg/home')

    # 对页面进行截图
    driver.save_screenshot('../img/ctrip.png')
    driver.quit()

def screenshot_element():
    driver = openBrowser.open_chrome()
    driver.maximize_window()
    driver.get('http://user.qunar.com/passport/login.jsp')

    # 点击'密码登录'链接
    driver.find_element_by_class_name('pwd-login').click()
    # 整个页面截图
    driver.save_screenshot('../img/qunar_login.png')
    # 获取验证码元素
    vcodeImg = driver.find_element_by_id('vcodeImg')
    # 获取验证码对坐标
    left = vcodeImg.location['x']
    top = vcodeImg.location['y']
    right = left + vcodeImg.size['width']
    bottom = top + vcodeImg.size['height']
    print(right)

    from PIL import Image
    # 打开刚才保存对页面截图
    im = Image.open('../img/qunar_login.png')
    # 使用获取到的位置剪切图片
    im = im.crop((left*2, top*2, right*2, bottom*2))
    im.save('../img/im.png')

    driver.quit()



if __name__ == '__main__':
    screenshot_element()

