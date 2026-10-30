from fastapi import FastAPI, status

from schemas import TicketCreate, TicketResponse
from tickets import create_ticket


app = FastAPI(title="Support Desk API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tickets", status_code=status.HTTP_201_CREATED)
def create_support_ticket(ticket_data: TicketCreate) -> TicketResponse:
    ticket = create_ticket(
        title=ticket_data.title,
        description=ticket_data.description,
    )

    return TicketResponse.model_validate(ticket)
