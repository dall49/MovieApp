
from os import getenv 

database = {
    'HOST' : getenv('HOST','localhost'),
    'DBUSER' : getenv('DBUSER','movieapp'),
    'PASSWORD' : getenv('PASSWORD','secret_user'),
    'DATABASE' : getenv('DATABASE','movieapp'),
    'PORT' : getenv('PORT','3306')
}

upload = {
    'upload_dir' : 'img/'
}
