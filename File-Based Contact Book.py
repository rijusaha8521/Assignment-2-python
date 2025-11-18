#ASSIGNMENT : 2

'''---------------------------------------------------------------
            Name: Riju kumar saha
                Roll No.:2501940018
                    MCA(AI & ML)  
------------------------------------------------------------------'''



import csv
import json
import os

FILE_CSV = "contacts.csv"
FILE_JSON = "contacts.json"

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name or not phone or not email:
        print("All fields are required.")
        return

    file_exists = os.path.exists(FILE_CSV)
    with open(FILE_CSV, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"Name": name, "Phone": phone, "Email": email})
    print("Contact added successfully!")

def view_contacts():
    if not os.path.exists(FILE_CSV):
        print("No contacts found.")
        return
    with open(FILE_CSV, "r") as f:
        reader = csv.DictReader(f)
        contacts = list(reader)
        if not contacts:
            print("Contact list is empty.")
            return
        print("\nAll Contacts:")
        for c in contacts:
            print(f"{c['Name']} | {c['Phone']} | {c['Email']}")

def search_contact():
    if not os.path.exists(FILE_CSV):
        print("No contacts found.")
        return
    name = input("Enter name to search: ").strip().lower()
    with open(FILE_CSV, "r") as f:
        reader = csv.DictReader(f)
        found = False
        for c in reader:
            if name in c['Name'].lower():
                print(f"Found: {c['Name']} | {c['Phone']} | {c['Email']}")
                found = True
        if not found:
            print("No contact found.")

def update_contact():
    if not os.path.exists(FILE_CSV):
        print("No contacts found.")
        return
    name = input("Enter contact name to update: ").strip().lower()
    with open(FILE_CSV, "r") as f:
        contacts = list(csv.DictReader(f))
    updated = False
    for c in contacts:
        if c["Name"].lower() == name:
            c["Phone"] = input("Enter new phone: ").strip()
            updated = True
    if updated:
        with open(FILE_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
            writer.writerows(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    if not os.path.exists(FILE_CSV):
        print("No contacts found.")
        return
    name = input("Enter name to delete: ").strip().lower()
    with open(FILE_CSV, "r") as f:
        contacts = list(csv.DictReader(f))
    new_contacts = [c for c in contacts if c["Name"].lower() != name]
    if len(new_contacts) == len(contacts):
        print("Contact not found.")
    else:
        with open(FILE_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
            writer.writerows(new_contacts)
        print("Contact deleted successfully!")

def export_json():
    if not os.path.exists(FILE_CSV):
        print("No contacts found.")
        return
    with open(FILE_CSV, "r") as f:
        contacts = list(csv.DictReader(f))
    with open(FILE_JSON, "w") as f:
        json.dump(contacts, f, indent=4)
    print("Contacts exported to JSON!")

def import_json():
    if not os.path.exists(FILE_JSON):
        print("No JSON file found.")
        return
    with open(FILE_JSON, "r") as f:
        contacts = json.load(f)
    print("\nContacts from JSON:")
    for c in contacts:
        print(f"{c['Name']} | {c['Phone']} | {c['Email']}")

def main():
    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to JSON")
        print("7. Import from JSON")
        print("8. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1': add_contact()
        elif choice == '2': view_contacts()
        elif choice == '3': search_contact()
        elif choice == '4': update_contact()
        elif choice == '5': delete_contact()
        elif choice == '6': export_json()
        elif choice == '7': import_json()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
