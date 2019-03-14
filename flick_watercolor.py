import flickrapi
import urllib.request
import os

# Change the follwing variables to match your own needs
project_path = 'flickr_download_images/'
photos_per_tag = 500
filenames = ['watercolor_flower.txt', 'cat.txt']


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
    api_key = u'c0eadeb742d657f4e119f176812ed91d'
    api_secret = u'a1d7e391b1a8f470'
    flickr = flickrapi.FlickrAPI(api_key, api_secret)

    # Runs the program, cycles through the emotions and downloads the images for each tag.
    os.chdir(project_path)
    for fname in filenames:
        watercoloreg = fname[:-4]
        with open(fname, 'r') as f:
            tags = f.read().splitlines()
        os.mkdir(watercoloreg)
        os.chdir(watercoloreg)
        for t in tags:
            download_files(flickr, t, watercoloreg, photos_per_tag)
        os.chdir(project_path)
