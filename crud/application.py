import requests
import json

URL = "http://127.0.0.1:8000/studentget/"

# Getiing the data from the API
def get_data(id = None):
    data = {}    
    if id :
     data = {
            'id': id
        }
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url=URL, data=json_data, headers=headers)

    data = r.json()
    print(data)


# Creating a data in the API
def create_data():
    name = input("Enter the name of the student: ")
    age  = int(input("Enter the age of the student: "))
    email = input("Enter the email of the student: ")
    data = {
        'name': name,
        'age': age,
        'email': email
    }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)


# Updating a data in the API
def update_data():
    id = input("Enter the ID of the student to update: ")
    name = input("Enter the new name of the student: ")
    email = input("Enter the new email of the student: ")
    data = {
        'id': id,
        'name': name,
        'email': email
    }
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.put(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)

# Deleting a data in the API
def delete_data(id = None):
    data = {}
    if id:
        data = {
            'id': id
        }
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.delete(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)  

while True:
    print("1. Get Data")
    print("2. Create Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == '1':
        id = input("Enter the ID of the student or press Enter to get all students: ")
        get_data(id)

    elif choice == '2':
        create_data()

    elif choice == '3':
        update_data()

    elif choice == '4':
        id = input("Enter the ID of the student to delete: ")
        delete_data(id)

    elif choice == '5':
        print("Exiting the program.")
        break
    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice!")