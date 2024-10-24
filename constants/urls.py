from typing import Final
from urllib.parse import ParseResult, urlparse

UNLUCKY_HOUSE_THREAD: Final[ParseResult] = urlparse(
    "https://unluckyhouse.com/showthread.php"
)
