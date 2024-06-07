from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from modules.ui.page_objects.constants.novaposhta_constants import SearchTrackNumberConstants


class SearchTrackNumber(BasePage):

    def __init__(self):
        # Call the constructor of the parent class to initialize the driver
        super().__init__()

    def go_to(self):
        # Open the Novaposhta page
        self.driver.get(SearchTrackNumberConstants.URL)

    def close_banner(self):
        # Close the banner on the page if it exists
        self.driver.find_element(By.XPATH, SearchTrackNumberConstants.BANNER_XPATH).click()

    def try_to_find_track_number(self, number_of_parcels):
        # Find the input field for the tracking number and enter it
        search_elem = self.driver.find_element(By.ID, 'cargo_number')
        search_elem.send_keys(number_of_parcels)

    def click_submit(self):
        # Find the submit button and click it
        self.driver.find_element(By.XPATH, SearchTrackNumberConstants.SUBMIT_BUTTON_XPATH).click()

    def check_appears_tracking_form(self):
        # Check if the tracking form appears on the page
        search_elem = self.driver.find_element(By.XPATH, SearchTrackNumberConstants.TRACKING_FORM_XPATH)
        return search_elem
