from lib.birthday_tracker import BirthdayTracker

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