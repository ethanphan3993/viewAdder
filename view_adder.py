from selenium import webdriver
import time
fileName = "videoList.txt"
videoFile = open(fileName)
listVideos = videoFile.readlines();
#print(listVideos)
buttonPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"

videoIndex = 0
tabIndex = 0

NUMBER_OF_TAB = 4
NUMBER_OF_VIDEO = len(listVideos)

# open browser
browser = webdriver.Chrome("/Users/ethanphan/Documents/Personal Project/ViewAdder/chromedriver")


#open url 1st, tabIndex = 0
browser.get(listVideos[videoIndex])
time.sleep(2)
playButton = browser.find_element_by_css_selector(buttonPlaySelector)
playButton.click()


# Open new tab 2nd video, tabIndex = 1
time.sleep(1)
videoIndex = videoIndex + 1
js = "window.open('"+listVideos[videoIndex].strip()+"')"
browser.execute_script(js)

# Use previous tab to play new video
time.sleep(1)
tabIndex = 0
handle = browser.window_handles[tabIndex]
browser.switch_to.window(handle)

videoIndex = videoIndex + 1;
browser.get(listVideos[videoIndex])
