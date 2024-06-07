import pytest
from datetime import datetime, timezone


@pytest.mark.jsonplaceholder
def test_get_all_users(json_placeholder):
    # Verify the status code of the response
    status_code = json_placeholder.get_status_code()
    assert status_code == 200

    # Verify the number of users returned
    users = json_placeholder.get_all_users()
    assert len(users) == 10

    # Verify the name of the first user
    assert users[0]['name'] == 'Leanne Graham'

    # Verify the 'Date' header of the response matches the current date and time in GMT format
    headers = json_placeholder.get_headers()
    expected_date = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
    assert headers['Date'] == expected_date
