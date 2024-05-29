from typing import Type, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status

from newsletter.application.common.exceptions import NewsletterIdNotExistError
from newsletter.application.common.newsletter_gateway import (
    GetNewslettersFilters
)
from newsletter.application.get_newsletter import GetNewsletter
from newsletter.application.get_newsletter import NewsletterDTO
from newsletter.application.get_newsletters import (
    GetNewsletters,
    NewslettersResultDTO
)
from newsletter.bootstrap.di import (
    get_newsletters_interactor,
    get_newsletter_interactor
)
from newsletter.domain.models.newsletter import NewsletterId

newsletter_router = APIRouter(prefix="/newsletter", tags=["newsletter"])


@newsletter_router.get("/")
async def get_newsletters(
        tags: Annotated[list[str], Query(default_factory=list)],
        action: GetNewsletters = Depends(get_newsletters_interactor),
) -> NewslettersResultDTO:
    response = await action(filters=GetNewslettersFilters(
        tags=tags,
    ))

    return response


@newsletter_router.get("/{newsletter_id}")
async def get_newsletter(
        newsletter_id: str,
        action: GetNewsletter = Depends(get_newsletter_interactor),
) -> NewsletterDTO | None | Type[NewsletterIdNotExistError]:
    try:
        newsletter_id = NewsletterId(newsletter_id)

        response = await action(newsletter_id)

        return response
    except NewsletterIdNotExistError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Newsletter with id={newsletter_id} does not exist"
        )
