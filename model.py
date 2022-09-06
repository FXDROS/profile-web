import csv

def addComment(add):
    result.append(add)
    return result

def addContact(nama, nomor, email, pesan):
    newContact = [nama.strip(), nomor.strip(), email.strip(), pesan]
    contactList = []
    
    with open('contactData.csv') as toRead :
        csv_reader = csv.reader(toRead, delimiter = ",")
        for item in csv_reader:
            contactList.append(item)
        contactList.append(newContact)

    with open ('contactData.csv', mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ",", quotechar="\"", quoting = csv.QUOTE_MINIMAL)
        for index in contactList :
            csv_writer.writerow(index)

    csv_file.close()

    return contactList

