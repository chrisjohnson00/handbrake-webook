from api_client.client import SonarrClient, RadarrClient
import pytest
import json


@pytest.mark.parametrize("test_input,expected", [(
        """{"episodes":[{"id":20877,"episodeNumber":1,"seasonNumber":4,"title":
        "Echoes","airDate":"2017-02-01","airDateUtc":"2017-02-02T01:00:00Z",
        "quality":"WEBRip-1080p","qualityVersion":1,"sceneName":
        "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"}],"episodeFile":{
        "id":80407,"relativePath":
        "Season 4/The 100 - S04E01 - Echoes WEBRip-1080p.mkv","path":
        "/downloads/The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC.mkv",
        "quality":"WEBRip-1080p","qualityVersion":1,"sceneName":
        "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"},"isUpgrade":
        "False","downloadClient":"Docker","downloadId":
        "818E46E811C1A960F4B502C5AF0AC654E120E31C","eventType":"Download",
        "series":{"id":182,"title":"The 100","path":"/tv/The 100",
        "tvdbId":268592,"tvMazeId":6,"imdbId":"tt2661044","type":
        "standard"}}""",
        "/tv/The 100/Season 4/The 100 - S04E01 - Echoes WEBRip-1080p.mkv")])
def test_sonarr_get_full_file_path(test_input, expected):
    assert expected == SonarrClient(json.loads(test_input)).get_full_file_path()


@pytest.mark.parametrize("test_input,expected", [(
        """{"episodes":[{"id":20877,"episodeNumber":1,"seasonNumber":4,"title":
        "Echoes","airDate":"2017-02-01","airDateUtc":"2017-02-02T01:00:00Z",
        "quality":"WEBRip-1080p","qualityVersion":1,"sceneName":
        "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"}],"episodeFile":{
        "id":80407,"relativePath":
        "Season 4/The 100 - S04E01 - Echoes WEBRip-1080p.mkv","path":
        "/downloads/The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC.mkv",
        "quality":"WEBRip-1080p","qualityVersion":1,"sceneName":
        "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"},"isUpgrade":
        "False","downloadClient":"Docker","downloadId":
        "818E46E811C1A960F4B502C5AF0AC654E120E31C","eventType":"Download",
        "series":{"id":182,"title":"The 100","path":"/tv/The 100",
        "tvdbId":268592,"tvMazeId":6,"imdbId":"tt2661044","type":
        "standard"}}""",
        "1080p"),
    (
            """{"episodes":[{"id":20877,"episodeNumber":1,"seasonNumber":4,"title":
            "Echoes","airDate":"2017-02-01","airDateUtc":"2017-02-02T01:00:00Z",
            "quality":"WEBRip-1080p","qualityVersion":1,"sceneName":
            "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"}],"episodeFile":{
            "id":80407,"relativePath":
            "Season 4/The 100 - S04E01 - Echoes WEBRip-1080p.mkv","path":
            "/downloads/The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC.mkv",
            "quality":"WEBRip-720p","qualityVersion":1,"sceneName":
            "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"},"isUpgrade":
            "False","downloadClient":"Docker","downloadId":
            "818E46E811C1A960F4B502C5AF0AC654E120E31C","eventType":"Download",
            "series":{"id":182,"title":"The 100","path":"/tv/The 100",
            "tvdbId":268592,"tvMazeId":6,"imdbId":"tt2661044","type":
            "standard"}}""",
            "720p"),
    (
            """{"episodes":[{"id":20877,"episodeNumber":1,"seasonNumber":4,"title":
            "Echoes","airDate":"2017-02-01","airDateUtc":"2017-02-02T01:00:00Z",
            "quality":"WEBRip-1080p","qualityVersion":1,"sceneName":
            "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"}],"episodeFile":{
            "id":80407,"relativePath":
            "Season 4/The 100 - S04E01 - Echoes WEBRip-1080p.mkv","path":
            "/downloads/The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC.mkv",
            "quality":"WEBRip-480p","qualityVersion":1,"sceneName":
            "The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"},"isUpgrade":
            "False","downloadClient":"Docker","downloadId":
            "818E46E811C1A960F4B502C5AF0AC654E120E31C","eventType":"Download",
            "series":{"id":182,"title":"The 100","path":"/tv/The 100",
            "tvdbId":268592,"tvMazeId":6,"imdbId":"tt2661044","type":
            "standard"}}""",
            "720p")
])
def test_sonarr_get_quality_level(test_input, expected):
    assert expected == SonarrClient(json.loads(test_input)).get_quality_level()


@pytest.mark.parametrize("test_input, expected", [(
        """{
  "movie":{
    "id":1118,
    "title":"Caddyshack",
    "releaseDate":"1980-10-23",
    "folderPath":"/movies/Caddyshack (1980) {imdb-tt0080487}",
    "tmdbId":11977,
    "imdbId":"tt0080487"
  },
  "remoteMovie":{
    "tmdbId":11977,
    "imdbId":"tt0080487",
    "title":"Caddyshack",
    "year":1980
  },
  "movieFile":{
    "id":1123,
    "relativePath":"Caddyshack (1980) {imdb-tt0080487}.mp4",
    "path":"/downloads/Caddyshack (1980) [1080p]/Caddyshack.1980.1080p.BRrip.x264.YIFY.mp4",
    "quality":"Bluray-1080p",
    "qualityVersion":1,
    "releaseGroup":"1080p",
    "size":1610487095
  },
  "isUpgrade":false,
  "downloadId":"956406E27B6DE70155557C9CCE136F9E27C2C298",
  "eventType":"Download"
}""",
        "/movies/Caddyshack (1980) {imdb-tt0080487}/Caddyshack (1980) {imdb-tt0080487}.mp4"),

])
def test_radarr_get_full_file_path(test_input, expected):
    assert RadarrClient(json.loads(test_input)).get_full_file_path() == expected


@pytest.mark.parametrize("test_input, expected", [(
        """{
  "movie":{
    "id":1118,
    "title":"Caddyshack",
    "releaseDate":"1980-10-23",
    "folderPath":"/movies/Caddyshack (1980) {imdb-tt0080487}",
    "tmdbId":11977,
    "imdbId":"tt0080487"
  },
  "remoteMovie":{
    "tmdbId":11977,
    "imdbId":"tt0080487",
    "title":"Caddyshack",
    "year":1980
  },
  "movieFile":{
    "id":1123,
    "relativePath":"Caddyshack (1980) {imdb-tt0080487}.mp4",
    "path":"/downloads/Caddyshack (1980) [1080p]/Caddyshack.1980.1080p.BRrip.x264.YIFY.mp4",
    "quality":"Bluray-1080p",
    "qualityVersion":1,
    "releaseGroup":"1080p",
    "size":1610487095
  },
  "isUpgrade":false,
  "downloadId":"956406E27B6DE70155557C9CCE136F9E27C2C298",
  "eventType":"Download"
}""",
        "1080p"),

])
def test_radarr_get_quality_level(test_input, expected):
    assert RadarrClient(json.loads(test_input)).get_quality_level() == expected
