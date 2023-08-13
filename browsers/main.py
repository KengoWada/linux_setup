# import subprocess
# from os import environ
# import time


# home = environ['HOME']


# def get_brave():
#     print('Installing Brave')
#     time.sleep(2)

#     subprocess.call('sudo snap install brave')


# def get_chrome():
#     print('Installing Chrome')
#     time.sleep(2)

#     deb_url = 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
#     subprocess.call(deb_url, shell=True, cwd=home)

#     subprocess.call(
#         'sudo dpkg -i google-chrome-stable_current_amd64.deb', shell=True, cwd=home)


# def get_chromium():
#     print('')
#     time.sleep(2)

#     subprocess.call('sudo apt install chromium-browser', shell=True)


# def get_firefox():
#     print('Installing Firefox')
#     time.sleep(2)

#     subprocess.call('sudo snap install firefox', shell=True)


# def get_opera():
#     print('Installing Opera')
#     time.sleep(2)

#     subprocess.call('sudo snap install opera', shell=True)


# cases = {
#     '1': get_chrome,
#     '2': get_chromium,
#     '3': get_opera,
#     '4': get_firefox,
#     '5': get_brave
# }


# def install_browsers(browser_list):
#     print('This is going to use Snap packages for some browsers')
#     time.sleep(2)

#     print('Installing Snap')
#     subprocess.call('sudo apt install snapd', shell=True)

#     for i in browser_list:
#         function = cases.get(i, lambda: 'Invalid Value')

#         function()
#         subprocess.call('clear', shell=True)
