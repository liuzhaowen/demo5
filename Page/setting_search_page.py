from selenium.webdriver.common.by import By

from Base.base import Base

search_loc = By.ID, "com.android.settings:id/search"
search_input_loc = By.ID, "android:id/search_src_text"
search_back_loc = By.ID, "android.widget.ImageButton"
search_elements_loc = By.ID, "com.android.settings:id/title"

class SearchPage(Base):

    def page_search_click(self):
        self.base_click_element(search_loc)

    def page_search_input(self, text):
        self.base_input_element(search_input_loc, text)

    def page_search_back(self):
        self.base_click_element(search_back_loc)

    def page_search_elements_text(self):
        return [i.text for i in self.base_find_elements(search_elements_loc)]
    