import csv

input_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
output_file = 'formatted_output.csv'
fieldnames = ['sales', 'date', 'region']

with open(output_file, mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for filename in input_files:
        with open(f'./data/{filename}', mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if row[0] == "pink morsel":
                    price = float(row[1].replace("$", ""))
                    sales = price * int(row[2])
                    writer.writerow({
                        'sales': sales,
                        'date': row[3],
                        'region': row[4]
                    })
                    # print(f'\t{row[0]} sales ${sales} on date {row[3]}.')

print("✅ All data combined and written to combined_output.csv")