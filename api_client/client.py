def get_full_file_path(api_json):
    """
    From the api json, grab the series.path and then append that to the episodeFile.relativePath to get the full path
    :param api_json: a dict containing the json
    :return: The full file path for the file from the json
    """
    base_path = api_json['series']['path']
    relative_path = api_json['episodeFile']['relativePath']
    return "{}/{}".format(base_path, relative_path)
