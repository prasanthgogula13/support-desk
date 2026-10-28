import pytest

from tickets import create_ticket


def test_create_ticket_with_valid_input():
    ticket = create_ticket(
        title="  Unable to connect to VPN  ",
        description="  Connection fails from home.  ",
    )

    assert ticket == {
        "title": "Unable to connect to VPN",
        "description": "Connection fails from home.",
        "status": "open",
    }


def test_create_ticket_rejects_blank_title():
    with pytest.raises(ValueError, match="Title must not be empty"):
        create_ticket(
            title="   ",
            description="Connection fails from home.",
        )


def test_create_ticket_rejects_blank_description():
    with pytest.raises(ValueError, match="Description must not be empty"):
        create_ticket(
            title="Unable to connect to VPN",
            description="   ",
        )
