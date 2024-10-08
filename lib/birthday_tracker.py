class BirthdayTracker():
    def __init__(self):
        self.birthday_list = []

    def add_birthday(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

        name_updated = False

        for birthday_dictionary in self.birthday_list:
            if birthday_dictionary['name'] == name:
                birthday_dictionary['birthdate'] = birthdate
                name_updated = True
        if name_updated == False:
            self.birthday_list.append({'name':name,'birthdate':birthdate})
        # FUNCTIONALITY: appends a dictionary to the list containing the name and birthday
        # and if name already exists, update the birthdate
        # RETURNS nothing

        # FORMAT: [{'name': 'Jim','birthdate':'1990-10-10'}]

    def change_names(self, old_name, new_name):
        pass
        # PARAMETERS: old name and the new name
        # FUNCTIONALITY: replacing the existing name
        # RETURNS nothing

    def list_upcoming_birthdays(self):
        pass
        # PARAMETERS: none
        # RETURNS a list of the next 5 names/birthdays and how old they will be turning
