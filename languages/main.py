from utils import BaseInstaller

__all__ = ('language_installer', )

OPTIONS = [
    {
        "id": 1,
        "name": "Java",
        # https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04
        "install_steps": [
            "sudo apt install default-jre default-jdk -y",
        ]
    },
    {
        "id": 2,
        "name": "NodeJS",
        # https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04
        "install_steps": [
            "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash",
            "nvm install --lts",
        ]
    },
    {
        "id": 3,
        "name": "PHP",
        # https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-22-04#step-3-installing-php
        "install_steps": [
            "sudo apt install php -y"
        ]
    },
]


language_installer = BaseInstaller(OPTIONS)
