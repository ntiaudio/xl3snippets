import logging
from typing import Union

class XL3Version:
    def __init__(self, maj: int, min: int, patch: int, rc: Union[int, str]):
        self._major = maj
        self._minor = min
        self._patch = patch
        if isinstance(rc, str):
            if rc.startswith('RC'):
                self._rc = int(rc[2:])
                self._build = 0
            else:
                self._rc = 0
                self._build = 0
                logging.error(f'XL3Version: version string has bad rc/build part ({rc})')
        else:
            self._build = int(rc)
            self._rc = 0

    def __str__(self) -> str:
        if self.is_rc:
            return f'{self._major}.{self._minor}.{self._patch}.RC{self._rc}'
        else:
            return f'{self._major}.{self._minor}.{self._patch}.{self._build}'

    @property
    def short_version(self) -> str:
        return f'{self._major}.{self._minor}.{self._patch}'

    @property
    def is_rc(self) -> bool:
        return self._rc > 0

    @classmethod
    def from_string(cls, ver: str):
        tokens = ver.split('.')
        maj = 0
        min = 0
        patch = 0
        rc = 0
        if len(tokens) >= 1:
            maj = int(tokens[0])
        if len(tokens) >= 2:
            min = int(tokens[1])
        if len(tokens) >= 3:
            patch = int(tokens[2])
        if len(tokens) >= 4:
            if tokens[3].startswith('RC'):
                rc = tokens[3]
            else:
                rc = int(tokens[3])

        return XL3Version(maj, min, patch, rc)
