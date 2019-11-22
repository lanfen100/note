import json
import os
import re

def get_catalog(file_path):
    with open(file_path, 'rb') as f:
        catalog = json.load(f)
    return catalog


def get_md_list(catalog):
    def read_md(catalog, md_list):
        for chapter in catalog:
            if chapter['have_children']:
                read_md(chapter['children'], md_list)
            else:
                md_path = chapter['path']
                md_name = chapter['name']
                md_list.append({
                    'name': md_name,
                    'path': md_path
                })
        return md_list

    md_list = read_md(catalog['catalog'], [])

    return md_list


def get_all_md_path():
    md_path_list = []
    for home, dirs, files in os.walk('bookcatalog'):
        for filename in files:
            file_path = os.path.join(home, filename)
            catalog = get_catalog(file_path)
            md_list = get_md_list(catalog)
            for md in md_list:
                md_path_list.append(md['path'])
    return md_path_list


if __name__ == '__main__':
    print(get_all_md_path())