#!/usr/bin/env python3

import subprocess

class moduleMitmf():

    cmd = subprocess.run('sudo bash evilMITM/mitm.sh', shell=True)
