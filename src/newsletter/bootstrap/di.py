from fastapi import Depends

from newsletter.adapters.database.fake_newsletter_db import FakeNewsletterDB
from newsletter.application.common.newsletter_gateway import (
    NewslettersReader,
    NewsletterReader
)
from newsletter.application.get_newsletter import GetNewsletter
from newsletter.application.get_newsletters import GetNewsletters


def get_newsletters_interactor(
        newsletter_db_gateway: NewslettersReader = Depends(FakeNewsletterDB)
) -> GetNewsletters:
    return GetNewsletters(newsletter_db_gateway)


def get_newsletter_interactor(
        newsletter_db_gateway: NewsletterReader = Depends(FakeNewsletterDB)
) -> GetNewsletter:
    return GetNewsletter(newsletter_db_gateway)
