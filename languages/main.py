import subprocess
from os import environ
import time

home = environ['HOME']


def get_java():
    print('Installing Java')
    time.sleep(2)
    subprocess.call('sudo apt install default-jre', shell=True)
    subprocess.call('sudo apt install default-jdk', shell=True)


def get_node():
    print('Installing Node.js with NVM')
    time.sleep(2)
    subprocess.call('sudo apt install curl', shell=True)
    curl_link = 'curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh -o install_nvm.sh'

    subprocess.call(curl_link, shell=True, cwd=home)
    subprocess.call('bash install_nvm.sh', shell=True, cwd=home)
    subprocess.call('nvm install --lts', shell=True)
    subprocess.call('nvm use --lts', shell=True)


def get_php():
    print('Installing PHP')
    time.sleep(2)
    subprocess.call('sudo apt-get install php libapache2-mod-php', shell=True)


def get_python():
    print('Installing Python3')
    time.sleep(2)
    subprocess.call('sudo apt install python3 python3-pip', shell=True)


cases = {
    '1': get_java,
    '2': get_php,
    '3': get_node,
    '4': get_python
}


def install_language(languageList):
    for i in languageList:
        function = cases.get(i, lambda: 'Invalid value')

        function()
        subprocess.call('clear', shell=True)
