
"""Tests for Contact Manager operations."""

import pytest

from contact_manager.operations import (
    create_contact,
    delete_contact,
    list_contacts,
    search_contact,
    update_contact,
)


@pytest.fixture
def contacts():
    """Give each test a fresh list."""
    return []


def test_create_contact(contacts):
    result = create_contact(contacts, "101", "Ravi", "9876543210")

    assert result == {
        "id": "101",
        "name": "Ravi",
        "phone": "9876543210",
    }
    assert len(contacts) == 1


def test_create_removes_outer_spaces(contacts):
    result = create_contact(contacts, " 101 ", " Ravi ", " 9876543210 ")

    assert result["id"] == "101"
    assert result["name"] == "Ravi"
    assert result["phone"] == "9876543210"


@pytest.mark.parametrize(
    ("contact_id", "name", "phone"),
    [
        ("", "Ravi", "9876543210"),
        ("101", "", "9876543210"),
        ("101", "Ravi", ""),
    ],
)
def test_create_rejects_empty_fields(contacts, contact_id, name, phone):
    with pytest.raises(ValueError):
        create_contact(contacts, contact_id, name, phone)

    assert contacts == []


def test_create_rejects_duplicate_id(contacts):
    create_contact(contacts, "101", "Ravi", "9876543210")

    with pytest.raises(ValueError, match="already exists"):
        create_contact(contacts, "101", "Priya", "9123456780")

    assert len(contacts) == 1


def test_list_empty_contacts(contacts):
    assert list_contacts(contacts) == []


def test_search_existing_contact(contacts):
    create_contact(contacts, "101", "Ravi", "9876543210")

    result = search_contact(contacts, "101")

    assert result is not None
    assert result["name"] == "Ravi"


def test_search_missing_contact(contacts):
    assert search_contact(contacts, "999") is None


def test_update_contact(contacts):
    create_contact(contacts, "101", "Ravi", "9876543210")

    result = update_contact(
        contacts, "101", "Ravi Kumar", "9000000000"
    )

    assert result["name"] == "Ravi Kumar"
    assert result["phone"] == "9000000000"


def test_update_missing_contact(contacts):
    with pytest.raises(ValueError, match="was not found"):
        update_contact(contacts, "999", "Ravi", "9876543210")


def test_update_rejects_empty_name(contacts):
    create_contact(contacts, "101", "Ravi", "9876543210")

    with pytest.raises(ValueError, match="name cannot be empty"):
        update_contact(contacts, "101", "", "9000000000")

    assert contacts[0]["name"] == "Ravi"


def test_delete_contact(contacts):
    create_contact(contacts, "101", "Ravi", "9876543210")

    result = delete_contact(contacts, "101")

    assert result["id"] == "101"
    assert contacts == []


def test_delete_missing_contact(contacts):
    with pytest.raises(ValueError, match="was not found"):
        delete_contact(contacts, "999")
