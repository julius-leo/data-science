from selenium import webdriver

website = 'https://www.idx.co.id/id/perusahaan-tercatat/laporan-keuangan-dan-tahunan'
path ='/Users/soju/Documents/notebooks/chromedriver/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)


# filter_button = driver.find_element_by_xpath('//label')
filter_button = driver.find_element(By.className("btn-filter-input")).click()
filter_button.click()

# driver.execute_script('''window.open('about:blank', 
#                           'secondtab');''')
  
# # It is switching to second tab now
# driver.switch_to.window('secondtab')
  
# # In the second tab, it opens geeksforgeeks
# driver.get('https://www.geeksforgeeks.org/')

driver.quit()