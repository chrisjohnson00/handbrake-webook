from api_client.client import get_full_file_path
import pytest, json


@pytest.mark.parametrize("test_input,expected", [(
                                                 """{"episodes":[{"id":20877,"episodeNumber":1,"seasonNumber":4,"title":"Echoes","airDate":"2017-02-01","airDateUtc":"2017-02-02T01:00:00Z","quality":"WEBRip-1080p","qualityVersion":1,"sceneName":"The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"}],"episodeFile":{"id":80407,"relativePath":"Season 4/The 100 - S04E01 - Echoes WEBRip-1080p.mkv","path":"/downloads/The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC.mkv","quality":"WEBRip-1080p","qualityVersion":1,"sceneName":"The.100.S04E01.Echoes.1080p.AMZN.WEBRip.DD5.1.HEVC"},"isUpgrade":"False","downloadClient":"Docker","downloadId":"818E46E811C1A960F4B502C5AF0AC654E120E31C","eventType":"Download","series":{"id":182,"title":"The 100","path":"/tv/The 100","tvdbId":268592,"tvMazeId":6,"imdbId":"tt2661044","type":"standard"}}""",
                                                 "/tv/The 100/Season 4/The 100 - S04E01 - Echoes WEBRip-1080p.mkv")])
def test_get_full_file_path(test_input, expected):
    assert expected == get_full_file_path(json.loads(test_input))
