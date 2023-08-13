from utils import BaseInstaller

__all__ = ("ide_installer", )

OPTIONS = [
    {
        "id": 1,
        "name": "Android Studio",
        # https://itslinuxfoss.com/install-android-studio-ubuntu-22-04/
        "install_steps": [
            "sudo apt install openjdk-11-jdk",
            # https://launchpad.net/~maarten-fonville/+archive/ubuntu/android-studio
            "sudo add-apt-repository ppa:maarten-fonville/android-studio",
            "sudo apt update",
            "sudo apt install android-studio -y",
        ]
    },
    {
        "id": 2,
        "name": "Sublime Text",
        # https://linuxhint.com/install-sublime-text3-ubuntu-22-04/
        "install_steps": [
            "curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add",
            "sudo add-apt-repository 'deb https://download.sublimetext.com/ apt/stable/'",
            "sudo apt install sublime-text",
        ]
    },
    {
        "id": 3,
        "name": "Codium",
        # https://vscodium.com/#install-on-debian-ubuntu-deb-package
        "install_steps": [
            "wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | " +\
                "gpg --dearmor | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg",
            "echo 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] " +\
                "https://download.vscodium.com/debs vscodium main' | sudo tee /etc/apt/sources.list.d/vscodium.list",
            "sudo apt update && sudo apt install codium -y"
        ]
    },
    {
        "id": 4,
        "name": "VSCode",
        # https://code.visualstudio.com/docs/setup/linux#_debian-and-ubuntu-based-distributions
        "install_steps": [
            "wget -c https://go.microsoft.com/fwlink/?LinkID=760868 -P ~/Downloads -O vscode.deb",
            "sudo apt install ~/Downloads/vscode.deb",
        ]
    }
]

ide_installer = BaseInstaller(OPTIONS)
