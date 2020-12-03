from selenium import webdriver
import time
fileName = "videoList.txt"
videoFile = open(fileName)
listVideos = videoFile.readlines();
#print(listVideos)
buttonPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"

# open browser
browser = webdriver.Chrome("/Users/ethanphan/Documents/Personal Project/ViewAdder/chromedriver")

index = 0

#open url
browser.get(listVideos[index])
time.sleep(1)
playButton = browser.find_element_by_css_selector(buttonPlaySelector)
playButton.click()


# Open new tab
time.sleep(0.5)
index = index + 1
js = "window.open('"+listVideos[index].strip()+"')"
browser.execute_script(js)

