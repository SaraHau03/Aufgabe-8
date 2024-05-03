from my_classes import Person, Subject

# Test creating a new person
person = Person("John", "Doe", "01-01-1990", "male")
person.put()

# Test updating email
subject = Subject("John", "Doe", "01-01-1990", "male", "john@example.com")
subject.update_email()
