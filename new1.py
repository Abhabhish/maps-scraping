from bs4 import BeautifulSoup


# Assuming you have the HTML in a file called "example.html"
with open('example.html',encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# Converting the HTML to JSON
json_data = {}
for tag in soup.find_all(True):
    tag_name = tag.name
    if tag.attrs:
        tag_attrs = {}
        for attr, value in tag.attrs.items():
            tag_attrs[attr] = value
        if tag_name in json_data:
            json_data[tag_name].append(tag_attrs)
        else:
            json_data[tag_name] = [tag_attrs]
    else:
        if tag_name in json_data:
            json_data[tag_name].append(tag.string)
        else:
            json_data[tag_name] = [tag.string]



for i in json_data['img']:
    line = i['src']
    with open('main.txt','a') as f:
        f.write(line+'\n')




