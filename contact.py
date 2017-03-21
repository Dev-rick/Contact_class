# -*- coding: utf-8 -*-

class Contact(object):
    def __init__(self, first_name, last_name, phone_number, birth_year, email): #Hier definiert man den self! Das heisst wenn man das jetzt Ham nennen wuerde dann wuerde man im naechsten Schritt siehe 1 immer hm.first_name verwenden
        self.first_name = first_name #1. self macht dass es sich auf das Objekt bezieht wo man später first_name verwendet z.B. wenn man später diese Def bei Thomas verwendet wird dann bezieht sich first_name auf thomas
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email
    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    def get_age(self):
        return 2017 - self.birth_year

def get_list_of_names(contacts):
    for index, person in enumerate(contacts): #enumerate makes the contacts iterable= zählbar --> enables use of  index
        print "%s) %s\n" % (index + 1, person.get_full_name())


def get_everything(contacts):
    for index, person in enumerate(contacts): # index is an order number of the contact object in the contacts list
        print  "\nID: %s\n" \
               ">>first_name: %s\n" \
               ">>last_name: %s\n" \
               ">>phone_number: %s\n" \
               ">>birth_year: %s\n" \
               ">>email: %s\n" \
               %( index+1, person.first_name, person.last_name, person.phone_number, person.birth_year, person.email)
    if not contacts:
        print "\nSorry you don't have any contacts in your contact list!\n"




def add_new_contact(contacts):
        first_name=raw_input("First name?\n>> "),
        last_name=raw_input("Last name:\n>> "),
        phone_number=raw_input("Phone number:\n>> "),
        while True:
            try:
                birth_year=int(raw_input("Birth year:\n>> "))
                break
            except ValueError:
                print "\nPlease enter a valid date!\n"
                continue
        email=raw_input("Email:\n>> "),
        new = Contact(first_name = "%s" % first_name, last_name = "%s" % last_name, phone_number = "%s" % phone_number, birth_year = "%s" % birth_year, email = "%s" % email )
        contacts.append(new)
        print "\n%s was successfully added!" % new.get_full_name()




def edit_contact(contacts):
    print "Select a number of the contact you'd like to edit:\n"
    get_list_of_names(contacts)
    while True:
        try:
            selected_id = int(raw_input("What contact would you like to edit? (enter ID number):\n>> ")) - 1
            break
        except ValueError:
            print "\nOops! please enter a valid number!\n"
            continue
    selected_contact = contacts[selected_id]

    while True:
        try:
            selected_field = int(raw_input("Enter the number of what you want to change: "
              "\n 1=First name\n"
              " 2=Last name\n"
              " 3=phone number\n"
              " 4=birth year\n"
              " 5=Email\n>> "))
            break
        except ValueError:
            print "\nOops that was no number!\n"
            continue
    if selected_field == 1:
        selected_contact.first_name= raw_input("First name:\n>> ")
    elif selected_field == 2:
        selected_contact.last_name = raw_input("Last name:\n>> ")
    elif selected_field == 3:
        selected_contact.phone_number = raw_input("Phone number:\n>> ")
    elif selected_field == 4:
        selected_contact.birth_year = int(raw_input("Birth year"))
    elif selected_field == 5:
        selected_contact.email = raw_input("New Email:\n>> ")





def delete_contact(contacts):
    print "Select the number of the contact you'd like to delete"
    get_list_of_names(contacts)
    while True:
        try:
            selected_id = int(raw_input("What contact would you like to delete? (enter ID number):\n>> ")) - 1
            break
        except ValueError:
            print "\nOops that was no number!\n"
            continue
    selected_contact = contacts[selected_id]

    contacts.remove(selected_contact)
    print "\nYour contact was deleted successfully!\n"





#USING super()
#allows to add something to a definition of the base class without changing it in the base class
#If you edit the source code to switch the base class to some other mapping, the super() reference will automatically follow. You have a single source of truth:

#class Skype(Contact): #This class has all the same capabilities as its parent, dict, but it extends the __init__ method by creating a new model skype_address
#    def __init__(self, first_name, last_name, phone_number, birth_year, email, skype_address): #the Skype_class
#        self.skype_adress = skype_address
#        super(Skype, self).__init__(first_name, last_name, phone_number, birth_year, email ) #the parentclass
#    def get_everything(self):
#        return ">>first_name: %s\n>>last_name: %s\n>>phone_number: %s\n>>birth_year: %s\n>>email: %s\n>>skype_adress: %s\n" %( self.first_name, self.last_name, self.phone_number, self.birth_year, self.email, self.skype_adress)



def yes_or_no_question(Question_text):
    answer = raw_input(Question_text)
    if answer == "yes":
        return True
    elif answer == "no":
        print "Bye, Bye"
        return False




def main():
    thom = Contact ( "Thomas", "Schmidt", "00432929298", 1996, "rickwarling@gmail.com")

    marissa = Contact("Marissa", "Mayer", 83483204032, 1978, "marissa@yahoo.com")

    bruce = Contact("Bruce", "Wayne", 902432309443, 1939,"bruce@batman.com")

    contacts = [thom, marissa, bruce]


    print "Welcome to your Contact List!"

    while True:
        selection = raw_input("Please choose one of these options:\n"
                              "a) See all your contacts\n"
                              "b) Add a new contact\n"
                              "c) Edit a contact\n"
                              "d) Delete a contact\n"
                              "e) Quit the program\n>> ")

        if selection.lower() == "a":
            get_everything(contacts)
        elif selection.lower() == "b":
            add_new_contact(contacts)
        elif selection.lower() == "c":
            edit_contact(contacts)
        elif selection.lower() == "d":
            if len(contacts) > 0:
                delete_contact(contacts)
            elif len(contacts) == 0:
                print "Sorry there are no contacts to delete!"
        elif selection.lower() == "e":
            print "Chiao!"
            break
        else:
            print "PLEASE select one of these options!"
            continue




if __name__ == '__main__':
    main()