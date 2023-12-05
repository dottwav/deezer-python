from _deezer.client import Client
from _deezer.pagination import PaginatedList
from _deezer.resources import (
    Album,
    Artist,
    Chart,
    Editorial,
    Episode,
    Genre,
    Playlist,
    Podcast,
    Radio,
    Resource,
    Track,
    User,
)

__version__ = "6.1.1"
__all__ = [
    "Album",
    "Artist",
    "Chart",
    "Client",
    "Editorial",
    "Episode",
    "Genre",
    "PaginatedList",
    "Playlist",
    "Podcast",
    "Radio",
    "Resource",
    "Track",
    "User",
]

USER_AGENT = f"_deezer Python API Wrapper v{__version__}"
