from abc import abstractmethod
from asyncio import Protocol
from typing import Optional

from newsletter.domain.models.newsletter import Newsletter


class NewslettersReader(Protocol):
    @abstractmethod
    async def get_newsletters(self) -> list[Newsletter]:
        raise NotImplementedError


class NewsletterReader(Protocol):
    @abstractmethod
    async def get_newsletter_with_id(
            self,
            newsletter_id: str
    ) -> Optional[Newsletter]:
        raise NotImplementedError
