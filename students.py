import json
import csv

# Step 1: Open and read JSON file
json_file = open("students.json", "r")
data = json.load(json_file)
json_file.close()

# Step 2: Open CSV file for writing
csv_file = open("students.csv", "w", newline="")

# Step 3: Get headers from JSON keys
headers = data[0].keys()
writer = csv.DictWriter(csv_file, fieldnames=headers)

# Step 4: Write header and rows
writer.writeheader()
writer.writerows(data)

# Step 5: Close CSV file
csv_file.close()

print("Conversion completed! Check students.csv file.")