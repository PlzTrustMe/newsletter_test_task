from abc import abstractmethod
from asyncio import Protocol
from dataclasses import dataclass
from typing import Optional

from newsletter.domain.models.newsletter import Newsletter


@dataclass
class GetNewslettersFilters:
    tags: list[str]


class NewslettersReader(Protocol):
    @abstractmethod
    async def get_newsletters(
            self,
            filters: GetNewslettersFilters
    ) -> list[Newsletter]:
        raise NotImplementedError


class NewsletterReader(Protocol):
    @abstractmethod
    async def get_newsletter_with_id(
            self,
            newsletter_id: str,

    ) -> Optional[Newsletter]:
        raise NotImplementedError
