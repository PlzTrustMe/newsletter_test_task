from dataclasses import dataclass
from typing import Optional

from newsletter.application.common.exceptions import NewsletterIdNotExistError
from newsletter.application.common.interactor import Interactor
from newsletter.application.common.newsletter_gateway import NewsletterReader
from newsletter.domain.models.newsletter import NewsletterId


@dataclass
class NewsletterDTO:
    id: str
    title: str
    summary: str
    tags: list[str]
    content: str


class GetNewsletter(Interactor[NewsletterId, Optional[NewsletterDTO]]):
    def __init__(self, newsletter_db_gateway: NewsletterReader):
        self.newsletter_db_gateway = newsletter_db_gateway

    async def __call__(
            self,
            newsletter_id: NewsletterId
    ) -> Optional[NewsletterDTO]:
        newsletter = await self.newsletter_db_gateway.get_newsletter_with_id(
            newsletter_id
        )

        if newsletter is None:
            raise NewsletterIdNotExistError
        return NewsletterDTO(
            id=newsletter.id,
            title=newsletter.title,
            summary=newsletter.summary,
            tags=newsletter.tags,
            content=newsletter.content,
        )
