import subprocess
import time
from os import environ

home = environ['HOME']


def get_mongodb():
    print('Installing MongoDB for')
    time.sleep(2)

    get_public_key = 'sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4'
    subprocess.call(get_public_key, shell=True, cwd=home)

    create_list_file = 'echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list'
    subprocess.call(create_list_file, shell=True, cwd=home)

    subprocess.call('sudo apt update', shell=True)
    subprocess.call('sudo apt install mongodb-org', shell=True)


def get_mysql():
    print('Installing MySQL')
    time.sleep(2)
    subprocess.call('sudo apt install mysql-server')
    print('Please ensure to set a password after this')
    time.sleep(2)


def get_postgres():
    print('Installing PostgreSQL')
    time.sleep(2)
    subprocess.call('sudo apt install postgresql postgresql-contrib')
    print('Please ensure to set a password after this')
    time.sleep(2)


cases = {
    '1': get_mysql,
    '2': get_postgres,
    '3': get_mongodb
}


def install_databases(databases_list):
    for i in databases_list:
        function = cases.get(i, lambda: 'Invalid Value')

        function()
        subprocess.call('clear', shell=True)
