import subprocess
import time


def get_android_studio():
    print('Installing Android Studio')
    time.sleep(2)
    subprocess.call('sudo snap install android-studio --classic', shell=True)


def get_atom():
    print('Installing Atom')
    time.sleep(2)
    subprocess.call('sudo snap install atom --classic', shell=True)


def get_pycharm():
    print('Installing PyCharm CE')
    time.sleep(2)
    subprocess.call(
        'sudo snap install pycharm-community --classic', shell=True)


def get_sublime_text():
    print('Installing Sublime Text')
    time.sleep(2)
    subprocess.call('sudo snap install sublime-text --classic', shell=True)


def get_vscode():
    print('Installing VS Code')
    time.sleep(2)
    subprocess.call('sudo snap install code --classic', shell=True)


def get_webstorm():
    print('WebStorm')
    time.sleep(2)
    subprocess.call('sudo snap install webstorm --classic', shell=True)


cases = {
    '1': get_vscode,
    '2': get_sublime_text,
    '3': get_atom,
    '4': get_android_studio,
    '5': get_pycharm,
    '6': get_webstorm
}


def install_editors(editors_list):
    print('This will use Snap packages')
    time.sleep(2)

    print('Installing Snap')
    subprocess.call('sudo apt install snapd', shell=True)

    for i in editors_list:
        function = cases.get(i, lambda: 'Invalid Value')

        function()
        subprocess.call('clear', shell=True)
