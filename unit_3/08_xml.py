import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('00_data.xml')

# Get the root element
root = tree.getroot()

# Print the root tag
print("Root element:", root.tag)

# Iterate through the employees
for employee in root.findall('employee'):
    name = employee.find('name').text
    age = employee.find('age').text
    city = employee.find('city').text
    print(f"Name: {name}, Age: {age}, City: {city}")
