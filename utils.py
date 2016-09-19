""" Varies utility functions """
import os
from hashlib import (md5, sha256, sha512)

HASH_ALGS = {
    "0": ("DES", None),
    "1": ("MD5", md5),
    "2a": ("Blowfish", None),
    "5": ("SHA256", sha256),
    "6": ("SHA512", sha512)
}
PASSWORDS = ""


def welcome():
    """ Prints the welcome screen """
    print("  ____  _               _                ____                _    ")
    print(" / ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | __")
    print(" \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |   | '__/ _` |/ __| |/ /")
    print("  ___) | | | | (_| | (_| | (_) \ V  V /| |___| | | (_| | (__|   < ")
    print(" |____/|_| |_|\__,_|\__,_|\___/ \_/\_/  \____|_|  \__,_|\___|_|\_\ ")


def get_sc_params():
    """
    Prompt the user for the 'Shadow Crack' params
    :return: shadow file path, username
    """
    loop = True
    while loop:
        file_path = input("Enter the file path for the shadow file:")
        if os.access(file_path, os.F_OK):
            if os.access(file_path, os.R_OK):
                loop = False
            print("That file path cannot be read. Check the file privileges.")
        print("That file path does not exist. Try again.")

    user_name = input("Who's password are we cracking? Enter the username:")
    return file_path, user_name
