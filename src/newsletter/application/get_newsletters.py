from dataclasses import dataclass

from .common.interactor import Interactor
from .common.newsletter_gateway import NewslettersReader
from ..domain.models.newsletter import Newsletter


@dataclass
class NewslettersResultDTO:
    newsletters: list[Newsletter]


class GetNewsletters(Interactor[None, NewslettersResultDTO]):
    def __init__(
            self,
            newsletter_db_gateway: NewslettersReader,
    ):
        self.newsletter_db_gateway = newsletter_db_gateway

    async def __call__(self, data=None) -> NewslettersResultDTO:
        newsletters = await self.newsletter_db_gateway.get_newsletters()

        return NewslettersResultDTO(newsletters=newsletters)
