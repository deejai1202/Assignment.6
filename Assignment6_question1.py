import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
employee_data={"employees":[
    {
        "Name": "Deepa",
      "DOB": "1985-02-12",
      "Height": 170,
      "City": "Chennai",
      "State": "Tamilnadu"
    },
    {
      "Name": "Sujay",
      "DOB": "1987-05-14",
      "Height": 151,
      "City": "Chennai",
      "State": "Tamilnadu"
    },
    {
      "Name": "Hewin",
      "DOB": "1986-04-15",
      "Height": 160,
      "City": "Madurai",
      "State": "Tamilnadu"
    },
    {
      "Name": "Jeyachandran",
      "DOB": "1980-02-12",
      "Height": 150,
      "City": "Namakkal",
      "State": "Tamilnadu"
    },
    {
      "Name": "Vasanth",
      "DOB": "1956-02-10",
      "Height": 167,
      "City": "Bangalore",
      "State": "Karnataka"
    }
  ]
}


with open('employee.json', 'w') as file:
    json.dump(employee_data, file)

with open('employee.json') as file:
    data = json.load(file)
    employee_list = []

    for employee_data in data['employees']:
        name = employee_data['Name']
        dob = employee_data['DOB']
        height = employee_data['Height']
        city = employee_data['City']
        state = employee_data['State']
        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print("Name:", employee.name)
    print("DOB:", employee.dob)
    print("Height:", employee.height)
    print("City:", employee.city)
    print("State:", employee.state)
    print()


# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
indian_states = {
    "Tamilnadu": "Chennai",
    "Telangana": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Maharashtra": "Mumbai",
    }
with open('states and capital.json', 'w') as file:
    json.dump(indian_states, file)

print("Indian states and capitals have been written to indian_states.json.")



