from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'
# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)
# Создание экземпляра браузера
browser = webdriver.Chrome(service=chrome_service)
URL = "https://onlineselectors.netlify.app/composite-selectors"
try:
    # Открытие веб-страницы
    browser.get(URL)
    # Неявное ожидание для загрузки элементов страницы
    browser.implicitly_wait(10)
    # Элементы с классом title
    elements_by_class = browser.find_elements(By.CLASS_NAME, "title")
    print("Элементы с классом title:", len(elements_by_class))
    # Элементы с классом item
    elements_by_class = browser.find_elements(By.CLASS_NAME, "item")
    print("Элементы с классом item:", len(elements_by_class))
    # Элементы с тегом imh (рисунки)
    elements_by_tag = browser.find_elements(By.TAG_NAME, "img")
    print("Элементы с тегом img:", len(elements_by_tag))
    # Элементы с ID post2
    elements_by_id = browser.find_elements(By.ID, "post2")
    print("Элементы с ID post2:", len(elements_by_id))
    # Выбор элемента ввода, найденного по XPath "//img[@alt='suslik']"
    elements_by_xpath = browser.find_elements(By.XPATH, "//img[@alt='suslik']")
    print("Элементы с alt suslik:", len(elements_by_xpath))
finally:
 # закрываем браузер после всех манипуляций
 browser.quit()