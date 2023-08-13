from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from languages import language_installer
from ides import ide_installer
from utils import select_options


parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "-l", "--languages",
    help="Programming languages to install. Numbers should be comma separated."
)
parser.add_argument(
    "-i", "--ides",
    help="IDEs to install. Numbers should be comma separated."
)
# parser.add_argument(
#     "-d", "--databases",
#     help="Databases to install. Numbers should be comma separated."
# )
# parser.add_argument(
#     "-b", "--browsers",
#     help="Browsers to install. Numbers should be comma separated."
# )
args = vars(parser.parse_args())


if args["languages"] is not None:
    language_args = args["languages"].split(',')
    language_installer.install(language_args)
else:
    selected_options = select_options("Programming Languages", language_installer)
    if selected_options is not None:
        language_installer.install(selected_options.split(','))

if args["ides"] is not None:
    ide_args = args["ides"].split(',')
    ide_installer.install(language_args)
else:
    selected_options = select_options("IDEs", ide_installer)
    if selected_options is not None:
        ide_installer.install(selected_options.split(','))
