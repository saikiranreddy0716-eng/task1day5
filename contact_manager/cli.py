
"""Command-line Contact Manager."""

from pathlib import Path

from contact_manager.operations import (
    Contact,
    create_contact,
    delete_contact,
    list_contacts,
    search_contact,
    update_contact,
)
from contact_manager.storage import load_contacts, save_contacts


DATA_FILE = Path(__file__).resolve().parent.parent / "contacts.json"


def show_menu() -> None:
    """Display the available actions."""
    print("\n===== Contact Manager =====")
    print("1. Create contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")


def main() -> None:
    """Load saved contacts and handle menu choices."""
    try:
        contacts: list[Contact] = load_contacts(DATA_FILE)
    except (ValueError, OSError) as error:
        print(f"Could not load contacts: {error}")
        print("Please inspect or repair the JSON file before continuing.")
        return

    print(f"Data file: {DATA_FILE}")

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        try:
            if choice == "1":
                contact_id = input("Enter contact ID: ")
                name = input("Enter name: ")
                phone = input("Enter phone number: ")

                contact = create_contact(
                    contacts, contact_id, name, phone
                )
                save_contacts(DATA_FILE, contacts)
                print(f"Contact '{contact['name']}' created.")

            elif choice == "2":
                records = list_contacts(contacts)

                if not records:
                    print("No contacts found.")
                else:
                    for contact in records:
                        print(
                            f"ID: {contact['id']} | "
                            f"Name: {contact['name']} | "
                            f"Phone: {contact['phone']}"
                        )

            elif choice == "3":
                contact_id = input("Enter contact ID to search: ")
                contact = search_contact(contacts, contact_id)

                if contact is None:
                    print("Contact not found.")
                else:
                    print(
                        f"ID: {contact['id']} | "
                        f"Name: {contact['name']} | "
                        f"Phone: {contact['phone']}"
                    )

            elif choice == "4":
                contact_id = input("Enter contact ID to update: ")
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")

                # Prepare a copy so a failed save does not change memory.
                updated_contacts = [
                    dict(contact) for contact in contacts
                ]
                updated = update_contact(
                    updated_contacts, contact_id, name, phone
                )
                save_contacts(DATA_FILE, updated_contacts)
                contacts[:] = updated_contacts
                print(f"Contact '{updated['name']}' updated.")

            elif choice == "5":
                contact_id = input("Enter contact ID to delete: ")
                contact = search_contact(contacts, contact_id)

                if contact is None:
                    raise ValueError(
                        f"Contact ID '{contact_id.strip()}' was not found."
                    )

                remaining = [
                    item for item in contacts
                    if item["id"] != contact["id"]
                ]
                save_contacts(DATA_FILE, remaining)
                contacts[:] = remaining
                print(f"Contact '{contact['name']}' deleted.")

            elif choice == "6":
                print("Thank you for using Contact Manager.")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 6.")

        except ValueError as error:
            print(f"Error: {error}")
        except OSError as error:
            print(f"File error: Could not save changes. {error}")


if __name__ == "__main__":
    main()
