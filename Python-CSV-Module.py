import csv

dialects = csv.list_dialects()
print('Available Dialects ->',dialects)

data_to_write = ['John Doe',28,'johndoe@gmail.com']

with open('my_csv.csv', 'w') as csv_fileobj:
    csv_writer = csv.writer(csv_fileobj,delimiter =';',dialect='excel')
    csv_writer.writerow(data_to_write)
    csv_writer.writerow(data_to_write)
    csv_writer.writerow(data_to_write)
    csv_writer.writerow(data_to_write)
    