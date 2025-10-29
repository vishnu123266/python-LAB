contacts1 ={
    "Anu":"9876543210",
    "teena":"8765432109"
}
contacts2={
    "john":"7654321098",
    "priya":"6543210987"
}
print("Contact1:",contacts1)
print("contact2:",contacts2)

merged_contacts = contacts1.copy()
merged_contacts.update(contacts2)

print("merged Contacts:")
print(merged_contacts)
