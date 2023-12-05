from __future__ import annotations

import pytest

import _deezer

pytestmark = pytest.mark.vcr


class TestPodcast:
    def test_get_episodes(self, client):
        podcast = client.get_podcast(699612)

        episodes = podcast.get_episodes()
        assert isinstance(episodes, _deezer.PaginatedList)
        episode = episodes[0]
        assert isinstance(episode, _deezer.Episode)
        assert episode.title == "Episode 9: Follow the money"
        assert len(episodes) == 12
