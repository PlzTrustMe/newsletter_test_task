from typing import Optional

from newsletter.application.common.newsletter_gateway import NewslettersReader, \
    NewsletterReader
from newsletter.domain.models.newsletter import Newsletter

newsletter_post_data: list[dict] = [
    {
        "id": "1",
        "title": "First post",
        "summary": "This is the first post",
        "tags": ["tag1", "tag2"],
        "content": "This is the first post",
    },
    {
        "id": "2",
        "title": "Second post",
        "summary": "This is the second post",
        "tags": ["tag3", "tag4"],
        "content": "This is the first post",
    },
    {
        "id": "3",
        "title": "Third post",
        "summary": "This is the third post",
        "tags": ["tag5", "tag6"],
        "content": "This is the first post",
    },
    {
        "id": "4",
        "title": "Fourth post",
        "summary": "This is the fourth post",
        "tags": ["tag7", "tag8"],
        "content": "This is the first post",
    },
    {
        "id": "5",
        "title": "Fifth post",
        "summary": "This is the fifth post",
        "tags": ["tag9", "tag10"],
        "content": "This is the first post",
    }
]


class FakeNewsletterDB(NewslettersReader, NewsletterReader):
    async def get_newsletters(self) -> list[Newsletter]:
        return [
            Newsletter(
                id=item.get("id"),
                title=item.get("title"),
                summary=item.get("summary"),
                tags=item.get("tags"),
                content=item.get("content"),
            ) for item in newsletter_post_data
        ]

    async def get_newsletter_with_id(
            self,
            newsletter_id: str
    ) -> Optional[Newsletter]:
        newsletter = next(
            (
                newsletter for newsletter in newsletter_post_data if
                newsletter["id"] == newsletter_id),
            None
        )

        if newsletter is None:
            return None
        return Newsletter(
            id=newsletter.get("id"),
            title=newsletter.get("title"),
            summary=newsletter.get("summary"),
            tags=newsletter.get("tags"),
            content=newsletter.get("content"),
        )
