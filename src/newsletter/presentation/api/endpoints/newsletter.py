from typing import Type, Optional, List, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status

from newsletter.adapters.database.fake_newsletter_db import FakeNewsletterDB
from newsletter.application.common.exceptions import NewsletterIdNotExistError
from newsletter.application.common.newsletter_gateway import (
    NewslettersReader,
    NewsletterReader, GetNewslettersFilters
)
from newsletter.application.get_newsletter import GetNewsletter
from newsletter.application.get_newsletter import NewsletterDTO
from newsletter.application.get_newsletters import (
    GetNewsletters,
    NewslettersResultDTO
)
from newsletter.domain.models.newsletter import NewsletterId

newsletter_router = APIRouter(prefix="/newsletter", tags=["newsletter"])


def get_newsletters_interactor(
        newsletter_db_gateway: NewslettersReader = Depends(FakeNewsletterDB)
) -> GetNewsletters:
    return GetNewsletters(newsletter_db_gateway)


def get_newsletter_interactor(
        newsletter_db_gateway: NewsletterReader = Depends(FakeNewsletterDB)
) -> GetNewsletter:
    return GetNewsletter(newsletter_db_gateway)


@newsletter_router.get("/")
async def get_newsletters(
        tags: Annotated[list, Query()] = list,
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
