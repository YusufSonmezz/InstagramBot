from time import sleep 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver 

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("http://www.instagram.com")

sleep(3)

InstagramtoFacebook = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button")
InstagramtoFacebook.click()

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input")\
    .send_keys("your e-mail")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input")\
    .send_keys("your password")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button")\
    .click()
sleep(10)

# go to account page
driver.get("https://www.instagram.com/your_account/")	# your account name will replace your_account
sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()

sleep(2)

jsKomut = """
sayfa = document.querySelector(".isgrP");
sayfa.scrollTo(0,sayfa.scrollHeight);
var sayfaSonu = sayfa.scrollHeight;
return sayfaSonu;
"""
sayfaSonu = driver.execute_script(jsKomut)
sleep(2)
while True:
    son = sayfaSonu 
    sleep(1)
    sayfaSonu = driver.execute_script(jsKomut)

    if son == sayfaSonu:
	    break

followerss = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
followers = []
for follower in followerss:
    followers += [follower.text]
sleep(5)
driver.refresh()

sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
sleep(2)

sayfaSonu = driver.execute_script(jsKomut)

sleep(2)
while True:
    son = sayfaSonu 
    sleep(1)
    sayfaSonu = driver.execute_script(jsKomut)

    if son == sayfaSonu:
	    break
sleep(2)
followings = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for following in followings:
    control = 0
    #print("following..:"+following.text+"\n")
    for follower in followers:
        #print("\tfollower..:"+follower.text+"\n")
        if following.text == follower:
            control += 1
    if(control == 0):
        print("Not Following Back..:" + following.text)
