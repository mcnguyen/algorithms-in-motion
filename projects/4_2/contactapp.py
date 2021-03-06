'''
ASSIGNMENT - 4.2 Quicksort
Do not modify this file. Create the quicksort function in 'quicksort.py'.
To check your work, run this file and test if all the print function in the menu
works correctly.
'''

import quicksort

def print_menu():
    print('1. Print Contacts')
    print('2. Add a Contact')
    print('3. Remove a Contact')
    print('4. Lookup a Contact')
    print('5. Quit')
    print('')

people = [{'name' : 'Judah', 'age' : 2}, {'name' : 'Beau', 'age' : 33}, {'name' : 'Aditya', 'age' : 29}]

menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        sort_by = raw_input("Sort by name or age: ")
        while not(sort_by == 'name' or sort_by == 'age'):
            sort_by = raw_input("Must enter 'name' or 'age': ")
        sorted_people = quicksort.sort(people, sort_by)
        for person in sorted_people:
            print(person)
        print('')
    elif menu_choice == 2:
        print("Add Contact")
        name = raw_input("Name: ")
        age = raw_input("Age: ")
        people.append({'name' : name, 'age' : int(age)})
    elif menu_choice == 3:
        print("Remove Contact")
        name = raw_input("Name: ")
        removed = False
        for person in people :
            if person['name'] == name :
                people.remove(person)
                removed = True
        if removed:
            print(name + " was deleted")
        else:
            print(name + " was NOT found")
    elif menu_choice == 4:
        print("Lookup Contact")
        name = raw_input("Name: ")
        found = False
        for person in people :
            if person['name'] == name :
                print(person)
                found = True
        if not found:
            print(name + " was not found")

    elif menu_choice != 5:
        print_menu()