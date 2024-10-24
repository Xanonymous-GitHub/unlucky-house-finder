from typing import Final

import regex as re
import scrapy
from typing_extensions import Pattern

from constants.urls import UNLUCKY_HOUSE_THREAD


class ThreadSpider(scrapy.Spider):
    name: Final[str] = "article_spider"
    start_urls: Final[tuple[str]]

    __white_space_pattern: Final[Pattern] = re.compile(r"\s+")
    __thread_text_extraction_path: Final[str] = (
        '//div[starts-with(@id, "post_message_")]/text()'
    )

    def __init__(self, *, thread_number: int):
        super().__init__()
        self.start_urls = (f"{UNLUCKY_HOUSE_THREAD.geturl()}?t={thread_number}",)

    def __filter_contents(self, contents: tuple[str]) -> list[str]:
        white_space_removed = [
            re.sub(self.__white_space_pattern, "", content.strip())
            for content in contents
        ]
        empty_removed = [content for content in white_space_removed if content]
        return empty_removed

    def parse(self, response, **kwargs):
        item = {}
        contents: list[str] = self.__filter_contents(
            response.xpath(self.__thread_text_extraction_path).getall()
        )
        print(contents)
        item["contents"] = contents
        return item
