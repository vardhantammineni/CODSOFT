contacts=[]

def add_contact():
    name=input("Enter Name:")
    phone=input("Enter Phone Number:")
    Email=input("Enter Email:")
    address=input("Enter Address:")
    
    contact={
        "name":name,
        "phone":phone,
        "Email":Email,
        "address":address
    }
    
    contacts.append(contact)
    print("Contact Added Successfully")
    
def view_contacts():
    if not contacts:
        print("no contacts found")
    else:
        print("\n  Contacts List   ")
        for contact in contacts:
            print("name:",contact["name"])
            print("phone:",contact["phone"])
            print("Email:",contact["Email"])
            print("address:",contact["address"])
            print()
def search_contact():
    name=input("Enter name to search:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            print("\n contact found  ")
            print("name:",contact["name"])
            print("phone:",contact["phone"])
            print("Email:",contact["Email"])
            print("address:",contact["address"])
            return
        else:
            print("contact not found")
def update_contact():
    name=input("Enter name to update:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contact["phone"]=input("Enter new phone number:")
            contact["Email"]=input("Enter new Email:")
            contact["address"]=input("Enter new address:")
            print("contact updated successfully")
            return
        else:
            print("contact not found")
def delete_contact():
    name=input("Enter name to delete:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("contact deleted successfully")
            return
        else:
            print("contact not found")
while True:
    print("\n***Contact Book***")
    print("1.Add Contact")
    print("2.View Contact")
    print("3.search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.exit")
    choice=input("Enter Choice:")
    if choice=="1":
        add_contact()
    elif choice=="2":
        view_contacts()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        update_contact()
    elif choice=="5":
        delete_contact()
    elif choice=="6":
        print("Exited successfully")
        break
    else:
        print("Invalid Choice")
            
        
    