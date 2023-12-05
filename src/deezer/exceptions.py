from __future__ import annotations

import requests


class _deezerAPIException(Exception):
    """Base exception for API errors."""


class _deezerRetryableException(_deezerAPIException):
    """A request failing with this might work if retried."""


class _deezerHTTPError(_deezerAPIException):
    """Specialisation wrapping HTTPError from the requests library."""

    def __init__(self, http_exception: requests.HTTPError, *args: object) -> None:
        if http_exception.response is not None and http_exception.response.text:
            url = http_exception.response.request.url
            status_code = http_exception.response.status_code
            text = http_exception.response.text
            super().__init__(status_code, url, text, *args)
        else:
            super().__init__(http_exception, *args)

    @classmethod
    def from_http_error(cls, exc: requests.HTTPError) -> _deezerHTTPError:
        """Initialise the appropriate internal exception from a HTTPError."""
        if exc.response is not None:
            if exc.response.status_code in {502, 503, 504}:
                return _deezerRetryableHTTPError(exc)
            if exc.response.status_code == 403:
                return _deezerForbiddenError(exc)
            if exc.response.status_code == 404:
                return _deezerNotFoundError(exc)
        return _deezerHTTPError(exc)


class _deezerRetryableHTTPError(_deezerRetryableException, _deezerHTTPError):
    """A HTTP error due to a potentially temporary issue."""


class _deezerForbiddenError(_deezerHTTPError):
    """A HTTP error cause by permission denied error."""


class _deezerNotFoundError(_deezerHTTPError):
    """For 404 HTTP errors."""


class _deezerErrorResponse(_deezerAPIException):
    """A functional error when the API doesn't accept the request."""

    def __init__(self, json_data: dict[str, str]) -> None:
        self.json_data = json_data


class _deezerUnknownResource(_deezerAPIException):
    """The resource type couldn't be determined."""
