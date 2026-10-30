def create_ticket(title: str, description: str) -> dict[str, str]:
    title = title.strip()
    description = description.strip()

    if not title:
        raise ValueError("Title must not be empty.")

    if not description:
        raise ValueError("Description must not be empty.")

    return {
        "title": title,
        "description": description,
        "status": "open",
    }
