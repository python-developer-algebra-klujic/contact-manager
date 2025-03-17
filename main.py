from repositories import FakerDataSeeder

faker = FakerDataSeeder('hr_HR')
gen_contact = faker.seed_contacts()

print(gen_contact)
print(gen_contact.date_of_birth.strftime('%d.%m.%Y %H:%M:%S'))
print(gen_contact.website)
