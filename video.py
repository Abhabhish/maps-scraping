from bs4 import BeautifulSoup
import urllib.request
import concurrent.futures
import requests

def download_video(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"Video downloaded as {filename}")


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

# Outputting the JSON data to a file called "example.json"

    
destination = input('enter destination: ')
urls = []

for i in json_data['img']:
    line = i['src'].split('=')[0]+'=s0*#@' + i['src'].split('=')[0].split('/')[-1]+'.jpg'
    vid = line.replace('/p/','/ggms/').replace('=s0','=m18').replace('.jpg','.mp4')
    urls.append(vid)


       
n=0
def main(url):
    print(url)
    global n
    try:
      download_video(url.split('*#@')[0],destination+"\\"+url.split('*#@')[1])
    except Exception as e:      
        print(e)
    n+=1
    print(n)


def main2():
    # Run request concurrently.
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as Executor:
        # Local variable.
        # Load executor with url to fetch and work on.
        future_to_url = {Executor.submit(
            main, url=url): url for url in urls}
        # Loop over futures request and mark them completed.
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                # Raise exception.
                raise(e)
if __name__ == '__main__':
    main2()





