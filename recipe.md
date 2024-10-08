# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

-> need to record names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

-> passing in the same name and a new date should update the birthday for that name

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

-> need a method to pass in an existing name and a new name to replace that with

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

-> need a method that lists upcoming birthdays

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

-> include the age friends will be turning when listing upcoming birthdays


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class BirthdayTracker():
    def __init__(self):
        self.birthday_list = []

    def add_birthday(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        # PARAMETERS: name and birthdate of the person to be added
        # FUNCTIONALITY: appends a dictionary to the list containing the name and birthday
        # and if name already exists, update the birthdate
        # RETURNS nothing

    def change_names(self, old_name, new_name):
        # PARAMETERS: old name and the new name
        # FUNCTIONALITY: replacing the existing name
        # RETURNS nothing

    def list_upcoming_birthdays(self):
        # PARAMETERS: none
        # RETURNS a list of the next 5 names/birthdays and how old they will be turning



    # [{'name': 'Jim', 'birthdate': 120}   ]
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

'''
Testing that adding one birthday/name combination will add that combination to birthday_list
'''
def test_add_one_birthday_returns_one_birthday():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim','1990-10-10')
    assert birthday_tracker.birthday_list == [{'name': 'Jim','birthdate':'1990-10-10'}]

'''
Testing that adding another birthday/name combination will append to the existing list:
'''
def test_add_another_birthday_full_list():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim','1990-10-10')
    birthday_tracker.add_birthday('Dave','1990-01-01')
    assert birthday_tracker.birthday_list == [{'name': 'Jim','birthdate':'1990-10-10'},{'name': 'Dave','birthdate':'1990-01-01'}]

'''
Testing that adding a name/birthday combination when the name already exists, updates the birthday
'''
def test_name_already_exists_updates_only_birthday():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim','1990-10-10')
    birthday_tracker.add_birthday('Dave','1990-01-01')
    birthday_tracker.add_birthday('Jim','2020-10-20')
    assert birthday_tracker.birthday_list == [{'name': 'Jim','birthdate':'2020-10-20'},{'name': 'Dave','birthdate':'1990-01-01'}]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
