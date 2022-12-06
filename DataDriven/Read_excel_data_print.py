from DataDriven import excel_utils

excel_file = 'Login_data.xlsx'

number_of_rows = excel_utils.get_row_count(excel_file, 'Login_invalid')
print("Number of Row is: ", + number_of_rows)

number_of_columns = excel_utils.get_column_count(excel_file, 'Login_invalid')
print("Number of Column is: ", + number_of_columns)

for r in range(2, number_of_rows + 1):
    username = excel_utils.read_data(excel_file, 'Login_invalid', r, 1)
    print(username)

for r in range(2, number_of_rows + 1):
    passward = excel_utils.read_data(excel_file, 'Login_invalid', r, 2)
    print(passward)

