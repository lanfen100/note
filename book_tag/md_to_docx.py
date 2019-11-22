import pypandoc

output = pypandoc.convert_file('./5.1/bcs/FAQ/faq.md', 'docx', outputfile='faq.docx')