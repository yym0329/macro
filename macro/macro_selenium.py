from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException        
import time
  # helper functions

def xpath_gen(kind_seat, place_num):
  if kind_seat == 'standard':
    xpath = f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{place_num+1}]/td[7]/a'
  elif kind_seat == 'special':
    xpath = f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{place_num+1}]/td[6]/a'
  else:
    print('wrong input')

  return xpath

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
      

# ================== Initial Settings ===========================
# basic configuration
reservation_site_add = 'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
site_add = 'https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
driver_path = r"chromedriver.exe"

# User info
phone_number = '01023613055'
passwd = 'youym010329#'

# Travel info
city_from = '동탄'
city_to = '대전'
date = '20220703'
departure_time = '18'
from_item = 0
num_items = 2

if __name__ == '__main__':
  input("Press Enter go to reservation page")
  # load driver
  chrome_options = Options()
  driver = Chrome(options=chrome_options, executable_path = driver_path)

  # open login site
  driver.get(site_add)
  print('done')

  # print(driver.current_url)
  # login

  phone_num_login = driver.find_element_by_id('srchDvCd3')
  phone_num_login.click()
  print('clicked')

  input_phone_num = driver.find_element_by_css_selector('input#srchDvNm03.input')
  print('found phone num input')
  input_phone_num.send_keys(phone_number)

  input_passwd = driver.find_element_by_css_selector('input#hmpgPwdCphd03.input')
  input_passwd.send_keys(passwd)

  submit_btn = driver.find_element_by_css_selector('input.submit.btn_midium')
  submit_btn.submit()

  # login done!

  # goto reservation site
  # print(driver.current_url)
  # input("Press Enter to go to reservation site...")
  driver.get(reservation_site_add)
  departure = driver.find_element_by_xpath('//*[@id="dptRsStnCdNm"]')
  arrival = driver.find_element_by_xpath('//*[@id="arvRsStnCdNm"]')
  
  departure.clear()
  departure.send_keys(city_from)
  arrival.clear()
  arrival.send_keys(city_to)

  departure_date_selector = Select(driver.find_element_by_xpath('//*[@id="dptDt"]')) 
  departure_date_selector.select_by_value(date)

  departure_time_selector = Select(driver.find_element_by_xpath('//*[@id="dptTm"]'))
  departure_time_selector.select_by_visible_text(departure_time)

  querry_btn = driver.find_element_by_xpath('//*[@id="search_top_tag"]/input')
  querry_btn.submit()
  
  # daejeon -> dongtan

  # set the reservation screen
  input("Press Enter to start reservation...")

  xpath_list = [xpath_gen('standard', i) for i in range(from_item, from_item + num_items)]
  # print(xpath_list)
  prev_address = driver.current_url
  print(driver.current_url)
  while (1):
    for xpath in xpath_list:
      if check_exists_by_xpath(driver, xpath):
        # print('XPATH AVAILABLE---------------------------')
        driver.find_element_by_xpath(xpath).click()
        
    # print('prev add: ', prev_address)
    # print('curr add: ', driver.current_url)

    if (prev_address == driver.current_url) or ((prev_address + '#none') == driver.current_url):
      print('not reserved')
      time.sleep(0.1)
      driver.refresh()

    else:
      print('--------------------- Reservation complete! --------------------------')
      break