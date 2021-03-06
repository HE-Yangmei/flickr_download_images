import flickrapi
import urllib.request
import os

# Change the follwing variables to match your own needs
project_path = 'watercolor/'
photos_per_text = 1800
filenames = ['watercolor.txt']


def download_files(flickr, t, category, num_photos):
    # Downloads the files of a specific text
    os.mkdir(t)
    os.chdir(t)
    s = []
    for photo in flickr.walk(text = t, sort='relevance', per_page = 50):
        url = 'https://farm{}.staticflickr.com/{}/{}_{}.jpg'.format(photo.get('farm'),
                             photo.get('server'), photo.get('id'), photo.get('secret'))
        s.append(url)
        if len(s) == num_photos:
            break
    for i in range(len(s)):
        filename = '{}_{}.jpg'.format(category, str(i))
        urllib.request.urlretrieve(s[i], filename)
    os.chdir(os.path.join(project_path, category))


if __name__ == '__main__':
    # Creates flickr object
    # These keys should be requested from flickr
    api_key = u'c0eadeb742d657f4e119f176812ed91d'
    api_secret = u'a1d7e391b1a8f470'
    flickr = flickrapi.FlickrAPI(api_key, api_secret)

    # Runs the program, cycles through the emotions and downloads the images for each text.
    os.chdir(project_path)
    for fname in filenames:
        categ = fname[:-4]
        with open(fname, 'r') as f:
            texts = f.read().splitlines()
        os.mkdir(categ)
        os.chdir(categ)
        for t in texts:
            download_files(flickr, t, categ, photos_per_text)
        os.chdir(project_path)
