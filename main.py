from repositories import ContactSeeder


faker = ContactSeeder('hr_HR')
gen_contact = faker.seed_contact()
print(gen_contact)
print(gen_contact.date_of_birth.strftime('%A %d.%m.%Y %H:%M:%S'))
print(gen_contact.website)
print()

generated_contacts = faker.seed_contacts(5)
for contact in generated_contacts:
    print(contact)
    print(contact.date_of_birth.strftime('%A %d.%m.%Y'))
    print(contact.website)
