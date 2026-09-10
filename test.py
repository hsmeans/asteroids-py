from collections.abc import Callable
from enum import Enum
from typing import Any


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


RawCSVData = list[list[object]]
PreparedCSVData = list[list[str]]
CSVStatusResult = tuple[str, PreparedCSVData | str]

# Don't touch above this line


def get_csv_status(status: CSVExportStatus, data: Any) -> CSVStatusResult:
    prep: Callable[[RawCSVData], PreparedCSVData] = lambda d: list(map(lambda x: list(map(str, x)), d))
    proc: Callable[[PreparedCSVData], str] = lambda d: "\n".join(map(lambda x: ",".join(x), d))
    match status:
        case CSVExportStatus.PENDING:
            return ("Pending...", prep(data))
        case CSVExportStatus.PROCESSING:
            return ("Processing...", proc(data))
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            return ("Unknown error, retrying...", proc(prep(data)))
        case _:
            raise Exception("unknown export status")
