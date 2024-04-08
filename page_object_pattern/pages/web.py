from selenium.webdriver.common.by import By


class TreesPage:
    URL = 'https://qa-test-selectors.netlify.app'
    VARIANT = 11
    HEADING = "Кроули"
    TITLE_TEXT = "Люцифер"
    
    def __init__(self, browser):
        self.browser = browser
 
    def load(self):
        self.browser.get(self.URL)
    
    def find_variant(self):
        # Выбор кнопки с 20 вариантом, как 19 элемента из списка всех кнопок страницы
        button = self.browser.find_elements(By.TAG_NAME,'button')[self.VARIANT-1] 
        # Выбор кнопки с 20 вариантом, по XPATH
        button = self.browser.find_element(By.XPATH, f'//button[@class="variant__btn"][text()="{self.VARIANT}"]')
        # Выбор кнопки с 20 вариантом, по CSS-селектору
        button = self.browser.find_element(By.CSS_SELECTOR,f'.variant__btn:nth-child({self.VARIANT})')
        # Нажатие на кнопку с вариантом
        button.click()
    
    def supernatural_elements_count(self):
        # Поиск элементов с data-type="supernatural"
        supernatural_elements = self.browser.find_elements(By.XPATH, '//*[@data-type="supernatural"]')
        return len(supernatural_elements)
    
    def dean_elements_count(self):
        # Поиск элементов с id="dean"
        dean_elements = self.browser.find_elements(By.ID, 'dean')
        return len(dean_elements)
    
    def john_winchester_elements_count(self):
        # Поиск элементов с class="chestnutTree"
        john_winchester_elements = self.browser.find_elements(By.CLASS_NAME, 'johnWinchester')
        return len(john_winchester_elements)
    
    def sam_winchester_elements_count(self):
        # Поиск элементов с name="sam-winchester"
        sam_winchester_elements = self.browser.find_elements(By.NAME,'sam-winchester')
        return len(sam_winchester_elements)
    
    def heading_images_count(self):
        # Поиск изображений с heading="Березка"
        heading_images = self.browser.find_elements(By.XPATH,f'//img[@heading="{self.HEADING}"]')
        return len(heading_images)
    
    def title_elements_count(self):
        # Поиск элементов с name="linden-tree"
        title_elements = self.browser.find_elements(By.XPATH,f'//h1[text()="{self.TITLE_TEXT}"]')
        return len(title_elements) 
    
    def images_loaded_count(self):
        images_loaded = self.browser.find_elements(By.CLASS_NAME, "imageContainer")
        return len(images_loaded)