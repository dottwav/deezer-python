from __future__ import annotations

import pytest
import requests

from _deezer.exceptions import (
    _deezerForbiddenError,
    _deezerHTTPError,
    _deezerNotFoundError,
    _deezerRetryableHTTPError,
)


@pytest.mark.parametrize(
    ("status_code", "expected_exception"),
    [
        (403, _deezerForbiddenError),
        (404, _deezerNotFoundError),
        (418, _deezerHTTPError),
        (502, _deezerRetryableHTTPError),
    ],
)
def test__deezer_http_error(status_code, expected_exception):
    response = requests.Response()
    response.status_code = status_code
    http_error = requests.HTTPError(response=response)

    exc = _deezerHTTPError.from_http_error(http_error)
    assert isinstance(exc, expected_exception)
