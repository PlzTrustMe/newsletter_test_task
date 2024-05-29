from dataclasses import dataclass


class ApplicationError(Exception):
    pass


@dataclass(eq=False)
class NewsletterIdNotExistError(ApplicationError):
    pass
