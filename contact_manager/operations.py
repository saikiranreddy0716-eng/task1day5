
"""Functions for managing contacts."""

from typing import TypedDict


class Contact(TypedDict):
    """Structure of one contact."""

    id: str
    name: str
    phone: str


def create_contact(
    contacts: list[Contact], contact_id: str, name: str, phone: str
) -> Contact:
    """Validate and create a new contact."""
    contact_id = contact_id.strip()
    name = name.strip()
    phone = phone.strip()

    if not contact_id:
        raise ValueError("Contact ID cannot be empty.")
    if not name:
        raise ValueError("Contact name cannot be empty.")
    if not phone:
        raise ValueError("Phone number cannot be empty.")
    if search_contact(contacts, contact_id) is not None:
        raise ValueError(f"Contact ID '{contact_id}' already exists.")

    contact: Contact = {
        "id": contact_id,
        "name": name,
        "phone": phone,
    }
    contacts.append(contact)
    return contact


def list_contacts(contacts: list[Contact]) -> list[Contact]:
    """Return a copy of all contacts."""
    return contacts.copy()


def search_contact(
    contacts: list[Contact], contact_id: str
) -> Contact | None:
    """Find a contact by ID."""
    contact_id = contact_id.strip()

    for contact in contacts:
        if contact["id"] == contact_id:
            return contact

    return None


def update_contact(
    contacts: list[Contact],
    contact_id: str,
    new_name: str,
    new_phone: str,
) -> Contact:
    """Update a contact's name and phone number."""
    contact_id = contact_id.strip()
    new_name = new_name.strip()
    new_phone = new_phone.strip()

    if not contact_id:
        raise ValueError("Contact ID cannot be empty.")
    if not new_name:
        raise ValueError("Contact name cannot be empty.")
    if not new_phone:
        raise ValueError("Phone number cannot be empty.")

    contact = search_contact(contacts, contact_id)

    if contact is None:
        raise ValueError(f"Contact ID '{contact_id}' was not found.")

    contact["name"] = new_name
    contact["phone"] = new_phone
    return contact


def delete_contact(
    contacts: list[Contact], contact_id: str
) -> Contact:
    """Delete and return a contact."""
    contact_id = contact_id.strip()

    if not contact_id:
        raise ValueError("Contact ID cannot be empty.")

    contact = search_contact(contacts, contact_id)

    if contact is None:
        raise ValueError(f"Contact ID '{contact_id}' was not found.")

    contacts.remove(contact)
    return contact
