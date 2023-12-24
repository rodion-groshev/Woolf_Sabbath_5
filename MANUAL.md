# Commands

    help
        All possible commands
---
    exit
        Close program       
---
    add-contact <name> <address> <phone> <email> <birthday>

    Add contact.
        name - Contact's Name
        address - Contact's Address
            The address must contain from 5 to 100 characters.
            And shouldn't contain special characters: !@#$%^&*()
        phone - Contact's Phone number
            Phone must start from "+38" following 9 or 10 digits
        email - Contact's E-Mail
        birthday - Contact's Birthday Date
            Should follow DD.MM.YYYY format

---
    add-phone <name> <phone>

    Add the phone to contact
        name - Contact's Name
        phone - Contact's Phone number
            Phone must start from "+38" following 9 or 10 digits

---              
    add-email <name> <email>

    Add email to contact
        name - Contact's Name
        email - Contact's E-Mail

---
    add-address <name> <address>
    
    Add address to contact
        name - Contact's Name
        address - Contact's Address
            The address must contain from 5 to 100 characters.
            And shouldn't contain special characters: !@#$%^&*()

---

    add-birthday <name> <birthday>
    
    Add the birthday to the contact
        name - Contact's Name
        birthday - Contact's Birthday Date
            Should follow DD.MM.YYYY format

---

    edit-phone <name> <old_phone> <new_phone>
    
    Change the phone number in the contact
        name - Contact's Name
        old_phone - Contact's Old Phone number
            Phone must start from "+38" following 9 or 10 digits
        new_phone - Contact's New Phone number
            Phone must start from "+38" following 9 or 10 digits

---

    edit-email <name> <old_email> <new_email>
    
    Add email to contact
        name - Contact's Name
        old_ email - Contact's Old E-Mail
        new_email - Contact's New E-Mail

---

    edit-address <name> <new_address>
    
    Change address in contact
        name - Contact's Name
        new_address - Contact's New Address, will replace the old address
            The address must contain from 5 to 100 characters.
            And shouldn't contain special characters: !@#$%^&*()

---

    edit-birthday <name> <new_birthday>
    
    Change birthday in contact
        name - Contact's Name
        birthday - Contact's New Birthday Date to replace
            Should follow DD.MM.YYYY format

---

    show-all

    Display all contacts

---

    show-phone <name>

    Display phone number by name  
        name - Contact's Name          

---

    show-email <name>
    
    Display email by name
        name - Contact's Name 

---

    show-address <name>

    Display address by name
        name - Contact's Name

---

    show-birthday <name>

    Display birthday by name
        name - Contact's Name

---

    delete-contact <name>

    Delete contact
        name - Contact's Name to delete

---

    delete-phone <name> <phone>

    Delete phone in contact
        name - Contact's Name
        phone - Contact's Phone number to delete
            Phone must start from "+38" following 9 or 10 digits

---

    delete-email <name> <email>

    Delete the email from the contact
        name - Contact's Name
        email - Contact's E-Mail to delete

---

    delete-address <name>

    Delete the address from the contact
        name - Contact's Name to delete address

---

    delete-birthday <name>

    Delete birthday in contact
        name - Contact's Name
