import xlsxwriter

def write_to_workbook(row, file, dictionary):
    '''
        Takes the list of products and writes it to an Excel File.
    '''
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()
    worksheet.write(f'A{row}', dictionary['title'])
    worksheet.write(f'B{row}', dictionary['link'])
    worksheet.write(f'C{row}', dictionary['price'])
    
    workbook.close()