# pylint: disable=W0246

from zero_to_one_hundred.configs.a_config_map import AConfigMap

SAFARI_BOOKS = "safari-books"


class SBConfigMap(AConfigMap):
    def __init__(self, map_yaml_path, persist_fs):
        super().__init__(map_yaml_path, persist_fs)

    @property
    def get_books_path(self):
        """use relative folder to simplify the usage in browser"""
        return "."

    @property
    def get_download_engine_path(self):
        return self.load["configs"]["download_engine_path"]

    @property
    def get_download_engine_books_path(self):
        return self.load["configs"]["download_engine_books_path"]

    @property
    def get_oreilly_username(self):
        return self.load["configs"]["oreilly_username"]

    @property
    def get_oreilly_userpassword(self):
        return self.load["configs"]["oreilly_userpassword"]

    @property
    def get_split_pdf_pages(self):
        return int(self.load["configs"]["split_pdf_pages"])
