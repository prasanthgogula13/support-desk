from typing import Annotated, Literal

from pydantic import BaseModel, StringConstraints


NonEmptyText = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        strict=True,
    ),
]


class TicketCreate(BaseModel):
    title: NonEmptyText
    description: NonEmptyText


class TicketResponse(TicketCreate):
    status: Literal["open"]
