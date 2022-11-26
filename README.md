<h1>ArchFixMountingDiskIssue</h1>

This repo contains the files needed to fix "Mounting disk issue during install"

Credit goes to [svartkanin](https://github.com/svartkanin)

<h1>Downloading Archinstall</h1>

First, we need to get the latest version of archinstall. Guide at archinstall [github page](https://github.com/archlinux/archinstall) (or below here)

1. You need a working network connection
2. Install the build requirements with `pacman -Sy; pacman -S git python-pip`
   *(note that this may or may not work depending on your RAM and current state of the squashfs maximum filesystem free space)*
3. Uninstall the previous version of archinstall with `pip uninstall archinstall`
4. Now clone the latest repository with `git clone https://github.com/archlinux/archinstall`

<h1>Modifying Archinstall</h1>

1. Download the fixed files with `git clone https://github.com/timhagel/ArchFixMountingDiskIssue`
2. Move fixed diskinfo.py with `mv diskinfo.py (wherever your archinstaller is)/archinstall/lib/disk`
3. Move fixed helpers.py with `mv helpers.py (wherever your archinstaller is)/archinstall/lib/disk`

<h1>Installing Archinstall</h1>

1. Build the project and install it using `python setup.py install`
2. Start the installer with `python -m archinstall`
3. Go through the installation process as normal
