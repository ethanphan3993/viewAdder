from selenium import webdriver

fileName = "videoList.txt"
videoFile = open(fileName)
listVideos = videoFile.readlines();
#print(listVideos)
buttonPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"

# open browser
browser = webdriver.Chrome("/Users/ethanphan/Documents/Personal Project/ViewAdding/chromedriver")

index = 0

#open url
browser.get(listVideos[index])

playButton = browser.find_element_by_css_selector(buttonPlaySelector)
playButton.click()