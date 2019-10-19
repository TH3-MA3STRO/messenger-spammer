def login(browser, wait, ec, byo, username, password):
    browser.get("https://www.facebook.com/login")
    wait.until(ec.visibility_of_element_located((byo.XPATH, "//input[@name='email']")))
    browser.find_element_by_xpath("//input[@name='email']").send_keys(username)
    browser.find_element_by_xpath("//input[@name='pass']").send_keys(password)
    browser.find_element_by_xpath("//button[@name='login']").click()


def spam(browser,wait, ec, byo, count, inp, msg):
    import time
    browser.get("https://www.facebook.com/messages/t/")
    wait.until(ec.visibility_of_element_located((byo.XPATH, "//input[@class='_58al _7tpc']")))
    browser.find_element_by_xpath("//input[@class='_58al _7tpc']").send_keys(inp)
    wait.until(ec.visibility_of_element_located((byo.XPATH, "//div[2]/ul/li/a/div/div[2]/div/div")))
    browser.find_element_by_xpath("//div[2]/ul/li/a/div/div[2]/div/div").click()
    time.sleep(1)

    for i in range(0, int(count)):
        try:
            browser.find_element_by_xpath("//div[@aria-label='Type a message...']").send_keys(msg)
            time.sleep(2)
            browser.find_element_by_xpath("//a[@class='_30yy _38lh _7kpi']").click()
        except:
            pass

