import pangu
import chardet

new_text = pangu.spacing_file('./test.md')

print(new_text)

with open('new_text.md', 'w', encoding='utf8') as f:
    f.write(new_text)

