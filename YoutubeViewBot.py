from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

Link=input("Youtube Video Link: - ")
TotalViews=int(input("Total Number of views you want: - "))
for _ in range(TotalViews):
	time.sleep(3)
	driver= webdriver.Firefox()
	#driver.get("https://youtu.be/7HwWmP3VmvA")
	driver.get(Link)
	time.sleep(3)
	play=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button')
	play.click()
	time.sleep(3)
