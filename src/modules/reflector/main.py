#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import shutil
import os


def reflector_process():

    MIRRORLIST = "/etc/pacman.d/mirrorlist"
    MIRRORLIST_BACKUP = "/etc/pacman.d/mirrorlist.bak"
    FETCH_MIRRORS = "reflector --verbose --latest 10 --protocol https --download-timeout 25 --sort rate --save /etc/pacman.d/mirrorlist"

    shutil.copyfile(MIRRORLIST, MIRRORLIST_BACKUP)

    try:
        subprocess.call(FETCH_MIRRORS.split(' '))
    except:
        os.remove(MIRRORLIST)
        os.rename(MIRRORLIST_BACKUP, MIRRORLIST)


def run():

    try:
        reflector_process()
    except:
        pass
