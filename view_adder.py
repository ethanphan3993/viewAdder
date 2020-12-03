from selenium import webdriver
import time
fileName = "videoList.txt"
viewFileName = "viewCount.txt"
videoFile = open(fileName)
listVideos = videoFile.readlines();
#print(listVideos)
buttonPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"

videoIndex = 0
tabIndex = 0
tabCount = 1
viewCount = 0

LOOP_TIME = 3


NUMBER_OF_TAB = 4
NUMBER_OF_VIDEO = len(listVideos)

# open browser
browser = webdriver.Chrome("/Users/ethanphan/Documents/Personal Project/ViewAdder/chromedriver")

#open url 1st, tabIndex = 0
browser.get(listVideos[videoIndex])
time.sleep(2)
playButton = browser.find_element_by_css_selector(buttonPlaySelector)
playButton.click()
time.sleep(1)

while True:
    videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEO
    tabIndex = (tabIndex + 1) % NUMBER_OF_TAB

    if tabCount < NUMBER_OF_TAB: 
        tabCount = tabCount + 1
        browser.execute_script("window.open('"+listVideos[videoIndex].strip()+"')")
    
    else:
        browser.switch_to.window(browser.window_handles[tabIndex])
        time.sleep(1)
        browser.get(listVideos[videoIndex])
    
    viewCount = viewCount + 1
    saveFile = open(viewFileName, "w")
    saveFile.write(str(viewCount))
    saveFile.close()

    time.sleep(LOOP_TIME)






