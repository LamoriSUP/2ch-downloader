import requests
from bs4 import BeautifulSoup as bs4

general_link = "ССылка на тред" #пример: https://2ch.hk/b/res/2281337322.html
r = requests.get(general_link, stream=True)
soup = bs4(r.content, 'html.parser')
images = soup.find_all('img') 


urls=[]


def image_url(image):

    if image.has_attr('data-src'):
        return image['data-src']

def get_file(url):
    r=requests.get(url, stream = True) 
    return r

def get_folder(url):
    folder=url.split('/'[-2])
    return folder

def get_name(url):
    name = url.split('/')[-1]
    return name

def save_image(name, file_object):
    with open (name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)
            


def main():
    

    for img in images:
        if image_url(img) != None:
            urls.append("https://2ch.hk"+image_url(img))
    print(urls)
    
    for url in urls:
        print(get_name(url))
        save_image(get_name(url),get_file(url))



if __name__ == '__main__':
    main()