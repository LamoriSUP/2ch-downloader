import requests
from bs4 import BeautifulSoup as bs4
import os

def general_link(link):
        if "https://2ch.hk/b/res/" not in link:
            link = "https://2ch.hk/b/res/"+link

        if ".html" not in link:
            link += '.html'
        return(link)

def image_url(image):

    if image.has_attr('data-src'):
        return image['data-src']

def get_file(url):
    r=requests.get(url, stream = True) 
    return r

def get_name(url):
    name = url.split('/')[-1]
    
    folder=url.split('/')[-2]
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    path = os.path.abspath(folder)
    return path + '/' + name

def save_image(name, file_object):
    with open (name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)




def main():
    urls=[]
    link = input("Введите ссылку на тред или его номер: ") #пример: https://2ch.hk/b/res/2281337322.html или 2281337322
    r = requests.get(general_link(link), stream=True)
    soup = bs4(r.content, 'html.parser')
    images = soup.find_all('img') 



    for img in images:
        if image_url(img) != None:
            urls.append("https://2ch.hk"+image_url(img))
    print(urls)
    
    for url in urls:
        print(get_name(url))
        save_image(get_name(url),get_file(url))
        
    print("файлы успешно сохранились в директории",get_name(url))

if __name__ == '__main__':
    main()
    input()