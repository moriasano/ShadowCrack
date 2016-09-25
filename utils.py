""" Utilities for shadow_crack """
import os
import crypt

PASSWORD_LIST = 'phpbb.txt'
HASH_ALGS = {
    # Entries are in the form:
    # "Shadow file code": ("Mechanism_name", hash_function)
    "0": ("DES", None),
    "1": ("MD5", None),
    "2": ("Blowfish", None),
    "2a": ("eksBlowfish", None),
    "5": ("SHA256", None),
    "6": ("SHA512", crypt.crypt)
}


def welcome():
    """ Print the welcome screen """
    print("  ____  _               _                ____                _    ")
    print(" / ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | __")
    print(" \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |   | '__/ _` |/ __| |/ /")
    print("  ___) | | | | (_| | (_| | (_) \ V  V /| |___| | | (_| | (__|   < ")
    print(" |____/|_| |_|\__,_|\__,_|\___/ \_/\_/  \____|_|  \__,_|\___|_|\_\ \n")
    print("                                                   Mori Asano 2016")
    print "\n\nCurrent using the %s dictionary.\n" % PASSWORD_LIST


def get_shadow_path():
    """
    Get the shadow file path w/ input validation
    :return: shadow file path
    """
    while True:
        file_path = raw_input("Enter the file path for the shadow file (Typically /etc/shadow):\n")
        if os.access(file_path, os.F_OK):
            if os.access(file_path, os.R_OK):
                return file_path
            print("That file path cannot be read. Check the file privileges.")
        else:
            print("That file path does not exist. Try again.")


def get_user_line(shadow_file):
    """
    Get the line from the shadow file relevant to a specified user
    :param shadow_file: file object
    :return: valid username
    """
    print "\nWho's password are we cracking?"
    while True:
        username = raw_input("Enter the username:")
        
        shadow_file.seek(0)
        for line in shadow_file.readlines():
            if username in line:
                return line

        print "'%s' was not found in the shadow file. Try another username" % username
