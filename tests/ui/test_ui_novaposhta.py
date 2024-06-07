import pytest
import time
from modules.ui.page_objects.novaposhta_search_track_number import SearchTrackNumber


@pytest.mark.ui_novaposhta
def test_ui_novaposhta():
    # Create an instance of the SearchTrackNumber page object
    search_track_number = SearchTrackNumber()

    # Navigate to the Nova Poshta page
    search_track_number.go_to()

    # Close the banner if it appears and wait for a second
    search_track_number.close_banner()
    time.sleep(1)

    # Enter a tracking number into the search field
    search_track_number.try_to_find_track_number('5325325235235')

    # Click the submit button
    search_track_number.click_submit()

    # Assert that the tracking form appears on the page
    assert search_track_number.check_appears_tracking_form() is not None

    # Close the browser
    search_track_number.close()
