import csv

# Open the CSV file
with open('F1Drivers_Dataset.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Read the header (optional)
    header = next(reader)
    
    # Loop through rows
    for row in reader:
        print(row)  # each row is a list of values
