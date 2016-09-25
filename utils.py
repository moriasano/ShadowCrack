""" Utilities for shadow_crack """
import os
import crypt

SHADOW_FILE_PATH = '/etc/shadow'
PASSWORD_LIST = "phpbb.txt"
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
    """ Prints the welcome screen """
    print("  ____  _               _                ____                _    ")
    print(" / ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | __")
    print(" \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |   | '__/ _` |/ __| |/ /")
    print("  ___) | | | | (_| | (_| | (_) \ V  V /| |___| | | (_| | (__|   < ")
    print(" |____/|_| |_|\__,_|\__,_|\___/ \_/\_/  \____|_|  \__,_|\___|_|\_\ \n")
    print("                                                   Mori Asano 2016")
    print "\n\nCurrent using the %s dictionary.\n" % PASSWORD_LIST


def get_sc_params():
    """
    Prompt the user for the 'Shadow Crack' params
    :return: shadow file path, username
    """
    while True:
        file_path = raw_input("Enter the file path for the shadow file (Typically /etc/shadow):")
        if os.access(file_path, os.F_OK):
            if os.access(file_path, os.R_OK):
                break
            print("That file path cannot be read. Check the file privileges.")
        else:
            print("That file path does not exist. Try again.")

    user_name = raw_input("Who's password are we cracking? Enter the username:")
    return file_path, user_name


def get_user_data_from_shadow(file_path, user_name):
    """
    :param file_path: shadow file path
    :param user_name: username to search for
    :return: hashed_pwd, salt, hash_mech:
            the hashed password, salt, and hash mech for the specified user
    """
    # Scan file for the relevant line
    user_line = None
    for line in open(file_path, 'r').readlines():
        if user_name in line:
            user_line = line
            break

    # Break if user is not found
    if user_line is None:
        print("User '%s' was not found" % user_name)
        return

    # Extract the needed data from the line
    hash_alg, salt, hashed_pwd = user_line.split(":")[1].split("$")[1:]
    print("\nHash Alg.:   %s" % HASH_ALGS[hash_alg][0])
    print("Salt:        %s" % salt)
    print("Hashed PWD:  %s" % hashed_pwd)

    # Check for unsupported hash algorithms
    if HASH_ALGS[hash_alg][1] is None:
        print "Sorry. At this time %s is not supported by ShadowCrack" % HASH_ALGS[hash_alg][0]
        return

    return hashed_pwd, salt, HASH_ALGS[hash_alg][1]
