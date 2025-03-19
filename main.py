from repositories import ContactSeeder, FileRepository


def main():
    file_repo = FileRepository('storage/contacts.json')
    faker = ContactSeeder('hr_HR')
    gen_contact = faker.seed_contact()
    file_repo.save_to_file(gen_contact)

    generated_contacts = faker.seed_contacts(5)
    file_repo.save_to_file(generated_contacts)


if __name__ == '__main__':
    main()
