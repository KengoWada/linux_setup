import subprocess
import time
from languages.main import install_language
from ides.main import install_editors
from databases.main import install_databases
from browsers.main import install_browsers

print('Welcome to Linux setup tool')
print('We shall start by updating and upgrading your system.')

# subprocess.call('sudo apt update && upgrade', shell=True)
# print('All Done.')
# time.sleep(1)
# subprocess.call('clear', shell=True)


def printColumns(nested_list):
    col_width = max(len(word) for row in nested_list for word in row) + 2
    for row in nested_list:
        print(''.join(word.ljust(col_width) for word in row))


def install_packages(function):
    try:
        selected_packages = raw_input(
            'Select numerical value(s) seperated by spaces. Leave empty if none needed: ')
    except:
        selected_packages = input(
            'Select numerical value(s) seperated by spaces. Leave empty if none needed: ')

    if selected_packages:
        function(selected_packages)

    return 0


programming_languages = [['[1] Java', '[2] PHP'], [
    '[3] Node.js', '[4] Python3']]

print('=========================================')
print('Select Programming Languages To Install')
print('=========================================')

printColumns(programming_languages)
print('\n')

install_packages(install_language)


text_editors = [['[1] VS Code', '[2] Sublime Text'], [
    '[3] Atom', '[4] Android Studio'], ['[5] PyCharm', '[6] WebStorm']]

print('=========================================')
print('Select Text Editors/IDEs To Install')
print('=========================================')

printColumns(text_editors)
print('\n')

install_packages(install_editors)


databases = [['[1] MySQL', '[2] PostgreSQL'], ['[3] Mongo']]

print('=========================================')
print('Select Databases To Install')
print('=========================================')

printColumns(databases)
print('\n')

install_packages(install_databases)


web_browsers = [['[1] Chrome', '[2] Chromium'], [
    '[3] Opera', '[4] Firefox'], ['[5] Brave']]

print('=========================================')
print('Select Web Browsers To Install')
print('=========================================')

printColumns(web_browsers)
print('\n')

install_packages(install_browsers)
