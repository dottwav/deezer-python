from __future__ import annotations

import pytest

import _deezer

pytestmark = pytest.mark.vcr


class TestEditorial:
    @pytest.fixture
    def editorial(self, client):
        return client.get_editorial(106)

    def test_attributes(self, editorial):
        assert hasattr(editorial, "name")
        assert isinstance(editorial, _deezer.Editorial)
        assert repr(editorial) == "<Editorial: Electro>"

    def test_get_selection(self, editorial):
        albums = editorial.get_selection()
        assert isinstance(albums, list)
        assert len(albums) == 10
        album = albums[0]
        assert isinstance(album, _deezer.Album)
        assert album.title == "Terre Promise"

    def test_get_chart(self, editorial):
        charts = editorial.get_chart()
        assert isinstance(charts, _deezer.Chart)

        assert isinstance(charts.tracks[0], _deezer.Track)
        assert isinstance(charts.albums[0], _deezer.Album)
        assert isinstance(charts.artists[0], _deezer.Artist)
        assert isinstance(charts.playlists[0], _deezer.Playlist)

    def test_get_releases(self, editorial):
        albums = editorial.get_releases()
        assert isinstance(albums, _deezer.PaginatedList)
        album = albums[0]
        assert isinstance(album, _deezer.Album)
        assert repr(album) == "<Album: Girls>"
        assert len(albums) == 199
