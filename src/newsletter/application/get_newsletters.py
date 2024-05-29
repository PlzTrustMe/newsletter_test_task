from dataclasses import dataclass

from .common.interactor import Interactor
from .common.newsletter_gateway import NewslettersReader, GetNewslettersFilters
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

    async def __call__(
            self,
            filters: GetNewslettersFilters
    ) -> NewslettersResultDTO:
        newsletters = await self.newsletter_db_gateway.get_newsletters(
            filters=filters
        )

        return NewslettersResultDTO(newsletters=newsletters)
