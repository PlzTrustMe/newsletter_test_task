from dataclasses import dataclass
from typing import Optional, NewType

NewsletterId = NewType("NewsletterId", str)


@dataclass
class Newsletter:
    id: Optional[NewsletterId]
    title: str
    summary: str
    tags: list[str]
    content: str
