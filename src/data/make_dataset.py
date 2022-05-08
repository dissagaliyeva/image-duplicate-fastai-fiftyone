import os
import shutil
import splitfolders

from simple_image_download import simple_image_download as simp


class ImageLoader:
    def __init__(self, theme, path='data', count=100):
        self.theme = theme
        self.path  = path
        self.count = count

        self.sample_download()

    def sample_download(self):
        # print(os.listdir())
        downloads = os.path.join(self.path, 'downloads')
        path      = os.path.join(downloads, self.theme)

        # create folders to store images
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            os.mkdir(downloads)
            os.mkdir(path)
        if not os.path.exists(downloads):
            os.mkdir(downloads)
            os.mkdir(path)
        if not os.path.exists(path):
            os.mkdir(path)




def get_title(title):
    if '.' not in title:
        return title.split('/')[-1]
    return title.split('/')[-1].split('.')[0]


dataset = ImageLoader('frodo')