import concurrent.futures
import subprocess
import main
import platform
import openpyxl
from datetime import datetime

def ping_ip(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return "not work"
        else:
            return  "work"
    except Exception:
            return  "not work"

def get_date():
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    return date_time


def edit_file(workbook_obj, address_name, status, time):
    # # Give the location of the file
    # path = "C:\\Users\\David\\Desktop\\code projects\\pingger\\source\\data.xlsx"
    #
    # # To open the workbook, workbook object is created
    # workbook_obj = openpyxl.load_workbook(path)

    # Get workbook active sheet object from the active attribute
    sheet_obj = workbook_obj.active
    cell_positions = ''
    for row in sheet_obj.rows:
        element = row[0]
        if element.value == address_name:
            cell_col_position = 'C'
            cell_row_position = element.row
            cell_positions = cell_col_position + str(cell_row_position)
            time_cell_positions = 'D' + str(cell_row_position)

    if status == 'work':
        sheet_obj[cell_positions] = "work"
        sheet_obj[cell_positions].fill = fill = openpyxl.styles.GradientFill(stop=("80ff72", "7ee8fa"))
        # print( sheet_obj[cell_positions].value)

    else:
        sheet_obj[cell_positions] = "not work"
        # print(sheet_obj[cell_positions].value)
        sheet_obj[cell_positions].fill = fill = openpyxl.styles.GradientFill(stop=("fc9842", "fe5f75"))

    sheet_obj[time_cell_positions] = time


if __name__ == '__main__':

    path = "C:\\Users\\David\\Desktop\\code projects\\pingger\\source\\data.xlsx"
    workbook_obj = openpyxl.load_workbook(path)

    dict_of_all_addresses = main.get_data_from_file(workbook_obj) #dict

    list_address = []
    for key in dict_of_all_addresses:
        list_address.append(dict_of_all_addresses[key].ip)

    print(list_address)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(ping_ip,list_address)

    i=0
    results = list(results)
    for key in dict_of_all_addresses:
        dict_of_all_addresses[key].status = results[i]
        time = get_date()
        dict_of_all_addresses[key].modify = time
        i+=1

    for key in dict_of_all_addresses:
        edit_file(workbook_obj, key, dict_of_all_addresses[key].status, dict_of_all_addresses[key].modify)

    workbook_obj.save('data.xlsx')

