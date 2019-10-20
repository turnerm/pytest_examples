from unittest import mock
from datetime import datetime

import part2.is_it_the_weekend


@mock.patch('part2.is_it_the_weekend.datetime')
def test_is_weekend(mock_datetime):
    """
    TODO: Mock datetime to check that is_weekend returns true on the weekend
    """
    mock_datetime.today.return_value = datetime(2019, 10, 20)
    assert part2.is_it_the_weekend.is_weekend()
