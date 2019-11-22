import json
import xlwt
import random
from book_tag.get_md_list import get_md_list, get_catalog


def load_catalog_dict(json_file):
    with open(json_file, 'rb') as f:
        return json.load(f)


def write_xl(catalog_dict):
    data_file = open('{}.data'.format(catalog_dict['bookname']),'w+',encoding='utf-8')
    book = xlwt.Workbook(encoding='utf-8')
    sheet1 = book.add_sheet(catalog_dict['bookname'])
    row_1 = ['TA', 'TB', 'TC', 'TD', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'NA', 'NB', 'NC', 'ND']   # json_key
    for i in range(len(row_1)):
        sheet1.write(0, i, row_1[i])

    line_number = 1
    for catalog_1 in catalog_dict['catalog']:
        if not catalog_1['expended']:
            row = write_row(catalog_1)
            row[10] = str(line_number)
            xxx = dict(zip(row_1,row))
            data_file.write(json.dumps(xxx))
            data_file.write('\n')
            print(json.dumps(xxx))
            for i in range(len(row)):
                sheet1.write(line_number, i, row[i])
            line_number += 1

    book.save('{}.xls'.format(catalog['bookname']))
    data_file.close()


def write_row(catalog):
        md_path = catalog['path'].split('-')
        md_name = md_path[1:].pop()
        md_lines = []
        with open('/'.join(md_path), 'rb') as f:
            for line in f:
                line = line.decode()
                line = line.rstrip()

                if not (line.startswith('#') or '![]' in line or line == ''):
                    md_lines.append(line)
        row = [catalog['name'], ''.join([i for i in md_lines]), '', '', ';'.join(i for i in md_path[1:-1]), '2', '', md_name, '', str(random.randint(1,5)), '', '',
                           '', '']  # json_value
        return  row


def get_tag():
    catalog = get_catalog()
    data_file = open('{}.data'.format(catalog['bookname']), 'w+', encoding='utf-8')
    book = xlwt.Workbook(encoding='utf-8')
    sheet1 = book.add_sheet(catalog['bookname'])
    row_1 = ['TA', 'TB', 'TC', 'TD', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'NA', 'NB', 'NC', 'ND']

    md_list = get_md_list()
    for md in md_list:
        md_name = md['name']
        md_path = md['path']




if __name__ == '__main__':
    catalog = load_catalog_dict('./bookCatalog.json')

    write_xl(catalog)




