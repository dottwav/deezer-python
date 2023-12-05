from __future__ import annotations

import pytest

import _deezer

pytestmark = pytest.mark.vcr


class TestChart:
    @pytest.fixture()
    def chart(self, client):
        return client.get_chart(0)

    def test_get_tracks(self, chart):
        tracks = chart.get_tracks()
        assert isinstance(tracks, _deezer.PaginatedList)
        track = tracks[0]
        assert isinstance(track, _deezer.Track)
        assert repr(track) == "<Track: LA FAMA>"
        assert len(tracks) == 10

    def test_get_artists(self, chart):
        artists = chart.get_artists()
        assert isinstance(artists, _deezer.PaginatedList)
        artist = artists[0]
        assert isinstance(artist, _deezer.Artist)
        assert repr(artist) == "<Artist: Jul>"
        assert len(artists) == 10

    def test_get_albums(self, chart):
        albums = chart.get_albums()
        assert isinstance(albums, _deezer.PaginatedList)
        album = albums[0]
        assert isinstance(album, _deezer.Album)
        assert repr(album) == "<Album: Multitude>"
        assert len(albums) == 10

    def test_get_playlists(self, chart):
        playlists = chart.get_playlists()
        assert isinstance(playlists, _deezer.PaginatedList)
        playlist = playlists[0]
        assert isinstance(playlist, _deezer.Playlist)
        assert repr(playlist) == "<Playlist: Les titres du moment>"
        assert len(playlists) == 10

    def test_get_podcasts(self, chart):
        podcasts = chart.get_podcasts()
        assert isinstance(podcasts, _deezer.PaginatedList)
        podcast = podcasts[0]
        assert isinstance(podcast, _deezer.Podcast)
        assert repr(podcast) == "<Podcast: Les Grosses Têtes>"
        assert len(podcasts) == 10
