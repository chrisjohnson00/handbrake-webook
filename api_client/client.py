from abc import ABC, abstractmethod


class ArrClient(ABC):

    def __init__(self, api_json):
        self.api_json = api_json

    @abstractmethod
    def get_full_file_path(self):
        """
        From the api json, grab the series.path and then append that to the episodeFile.relativePath to get the full
        path
        :return: The full file path for the file from the json
        """
        pass

    @abstractmethod
    def get_quality_level(self):
        """
        From the api json, determine the quality by inspecting episodeFile.quality
        :return:
        """
        pass

    def get_event_type(self):
        return self.api_json['eventType']


class SonarrClient(ArrClient):

    def get_full_file_path(self):
        """
        From the api json, grab the series.path and then append that to the episodeFile.relativePath to get the full
        path
        :return: The full file path for the file from the json
        """
        base_path = self.api_json['series']['path']
        relative_path = self.api_json['episodeFile']['relativePath']
        return "{}/{}".format(base_path, relative_path)

    def get_quality_level(self):
        """
        From the api json, determine the quality by inspecting episodeFile.quality
        :return:
        """
        quality = self.api_json['episodeFile']['quality']
        if "1080p" in quality:
            return "1080p"
        else:
            return "720p"


class RadarrClient(ArrClient):

    def get_full_file_path(self):
        """
        From the api json, grab the series.path and then append that to the episodeFile.relativePath to get the full
        path
        :return: The full file path for the file from the json
        """
        base_path = self.api_json['movie']['folderPath']
        relative_path = self.api_json['movieFile']['relativePath']
        return "{}/{}".format(base_path, relative_path)

    def get_quality_level(self):
        """
        From the api json, determine the quality by inspecting episodeFile.quality
        :return:
        """
        quality = self.api_json['movieFile']['quality']
        if "1080p" in quality:
            return "1080p"
        else:
            return "720p"
