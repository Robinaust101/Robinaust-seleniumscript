
from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://google.com")


# 3. Full Screen
driver.maximize_window()
# window_size = (driver.get_window_size())
# print(window_size)  # {'width': 1382, 'height': 744}
# print("Maximize window width is: " + window_size['width'])

# driver.fullscreen_window()

# 4. Set window size
# driver.set_window_size(768, 500)

# 5. Title of Web page
title = driver.title
print("Title is: " + title)

# 6. Url of current web page
url = driver.current_url
print("URL is: " + url)

# 7. Navigation
driver.get("https://demo.opencart.com/")
print("Open cart open successfully")

driver.back()  # google
print("After back, Title is: " + driver.title)

driver.forward()  # Your store
print("After forward, Title is: " + driver.title)

driver.get("https://apple.com")
print("Apple open successfully")
driver.refresh()
print("page refreshed")

driver.back()  # Your store
print("After back, Title is: " + driver.title)

# Close Browser
#driver.close()
#print("Test Complete.Browser Closed.")
# driver.quit()
