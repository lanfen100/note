import pdfkit
import os

path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' #安装位置 , wkhtmltopdf程序位置

config = pdfkit.configuration(wkhtmltopdf = path_wk)

options = {
    'page-size': 'Letter',
    'margin-top': '0.85in',
    'margin-right': '0.85in',
    'margin-bottom': '0.85in',
    'margin-left': '0.85in',
    'encoding': "UTF-8",
}


for home, dirs, files in os.walk('MD'):
    for filename in files:
        file_path = os.path.join(home, filename)
        with open(file_path, encoding='utf-8') as f:
            pdfkit.from_file(
                f,
                './PDF/{}.pdf'.format(filename.split('.')[0]),
                configuration=config,
                options=options
            )


