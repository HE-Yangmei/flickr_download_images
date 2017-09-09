import flickrapi
import urllib.request
import os

project_path = '/home/harrysha/Desktop/flickr_download_images'
photos_per_tag = 5
filenames = ['Category1.txt', 'Category2.txt']


def download_files(flickr, t, category, num_photos):
    # Downloads the files of a specific tag
    os.mkdir(t)
    os.chdir(t)
    s = []
    for photo in flickr.walk(tag_mode='all', sort='relevance', tags=t, license=4, per_page=50):
        url = 'https://farm{}.staticflickr.com/{}/{}_{}.jpg'.format(photo.get('farm'),
                             photo.get('server'), photo.get('id'), photo.get('secret'))
        s.append(url)
        if len(s) == num_photos:
            break
    for i in range(len(s)):
        filename = '{}_{}_{}.jpg'.format(category, t, str(i))
        urllib.request.urlretrieve(s[i], filename)
    os.chdir(os.path.join(project_path, category))


if __name__ == '__main__':
    # Creates flickr object
    # These keys should be requested from flickr
    api_key = u'replace_with_your_api_key'
    api_secret = u'replace_with_your_api_secret_key'
    flickr = flickrapi.FlickrAPI(api_key, api_secret)

    # Runs the program, cycles through the emotions and downloads the images for each tag.
    os.chdir(project_path)
    for fname in filenames:
        categ = fname[:-4]
        with open(fname, 'r') as f:
            tags = f.read().splitlines()
        os.mkdir(categ)
        os.chdir(categ)
        for t in tags:
            download_files(flickr, t, categ, photos_per_tag)
        os.chdir(project_path)
