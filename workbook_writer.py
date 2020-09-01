import xlsxwriter

def write_to_workbook(row, file, products):
    '''
        Takes the list of products and writes it to an Excel File.
    '''
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()

    for dictionary in products:
        worksheet.write(f'A{row}', dictionary['title'])
        worksheet.write(f'B{row}', dictionary['link'])
        worksheet.write(f'C{row}', dictionary['price'])
        row += 1

    workbook.close()