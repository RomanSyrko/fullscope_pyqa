import pytest
import time


@pytest.mark.ui_novaposhta
def test_ui_novaposhta(search_track_number_iu_novaposhta):
    # Navigate to the Nova Poshta page
    search_track_number_iu_novaposhta.go_to()

    # Close the banner if it appears and wait for a second
    search_track_number_iu_novaposhta.close_banner()
    time.sleep(1)

    # Enter a tracking number into the search field
    search_track_number_iu_novaposhta.try_to_find_track_number('5325325235235')

    # Click the submit button
    search_track_number_iu_novaposhta.click_submit()

    # Assert that the tracking form appears on the page
    assert search_track_number_iu_novaposhta.check_appears_tracking_form() is not None
