""" Shadow Crack! A tool to crack/recovery passwords on linux systems """
import utils
import datetime
from timeit import default_timer as timer


def shadow_crack(hashed_pwd, salt, hash_mech):
    """
    Main logic flow for the shadow file crack
    :param hashed_pwd: hash we are
    :param username: the username of the password to crack
    :param hash_mech: the hash function to use
    """
    print "\nStarting crack..."

    # Check for the hash against hashes of each dictionary entry
    pwd_dict = open(utils.PASSWORD_LIST, mode='r')
    start = timer()
    for pwd in pwd_dict:
        compare = hash_mech(pwd, salt)

        if compare == hashed_pwd:
            end = timer()
            pwd_dict.close()
            print "Password cracked!\n    %s      in     %d" % \
                  (compare, datetime.timedelta(seconds=(end - start)))
            return

    # Tear down
    print "Password has not been found against the dictionary."
    pwd_dict.close()
    return

if __name__ == '__main__':
    utils.welcome()
    while True:
        file_path, user_name = utils.get_sc_params()
        hashed_pwd, salt, hash_mech = utils.get_user_data_from_shadow(file_path, user_name)
        if hash_mech is not None:
            shadow_crack(hashed_pwd, salt, hash_mech)

        loop = raw_input("Again? (y/n)")
        if loop.lower() not in ['y', 'yes']:
            break
