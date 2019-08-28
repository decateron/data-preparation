import os
import tarfile
import zipfile
from six.moves import urllib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def fetch_data(url:str, path:str, file_name:str):
    """
    path - path to extract folder

    """
    
    if not os.path.isdir(path):
        os.makedirs(path)
        file_path = os.path.join(path, file_name)
        urllib.request.urlretrieve(url, file_path)
        
        
    if file_name.endswith("tar.gz"):
        tgz = tarfile.open(file_path, "r:gz")
        tgz.extractall(path=path)
        tgz.close()
    elif file_name.endswith("tar.bz2"):
        tgz = tarfile.open(file_path, "r:bz2")
        tgz.extractall(path=path)
        tgz.close()
    elif file_name.endswith("tgz"):
        tgz = tarfile.open(file_path)
        tgz.extractall(path=path)
        tgz.close()
    elif file_name.endswith("tbz"):
        tgz = tarfile.open(file_path)
        tgz.extractall(path=path)
        tgz.close()
    elif file_name.endswith("tar"):
        tar = tarfile.open(file_path)
        tar.extractall(path=path)
        tar.close()
    elif file_name.endswith("zip"):
        zf = zipfile.ZipFile(file_path, "r")
        zf.extractall(path=path)
        zf.close()
