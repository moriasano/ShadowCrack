""" Shadow Crack! A tool to crack/recovery passwords on linux systems """
import utils
import datetime
from timeit import default_timer as timer


def shadow_crack(user_line):
    """
    Main logic flow for 'Shadow Crack'
    :param user_line: the line from the shadow file
    """
    # Extract the needed data from the line
    hash_alg, salt, hashed_pwd = user_line.split(":")[1].split("$")[1:]
    hash_name, hash_mech = utils.HASH_ALGS[hash_alg]
    print("\nHash Alg.:   %s" % hash_name)
    print("Salt:        %s" % salt)
    print("Hashed PWD:  %s" % hashed_pwd)

    # Check for unsupported hash algorithms
    if hash_mech is None:
        print "Sorry, At this time %s is not supported by ShadowCrack" % hash_name
        return

    print "\nStarting crack..."

    # Check for the hash against hashes of each dictionary entry
    pwd_dict = open(utils.PASSWORD_LIST, mode='r')
    start = timer()
    for pwd in pwd_dict:
        formated_salt = "$%s$%s$" % (hash_alg, salt)
        compare = hash_mech(pwd.strip(), formated_salt)

        if hashed_pwd == compare:
            end = timer.close()
            pwd_dict.close()
            print "Password cracked!\n    %s      in     %d" % \
                  (compare, datetime.timedelta(seconds=(end - start)))

        # Tear down
        print "Password has not been found against the dictionary."
        pwd_dict.close()
        return


if __name__ == '__main__':
    utils.welcome()
    while True:
        shadow_file_path = utils.get_shadow_path()
        shadow_file = open(shadow_file_path, mode='r')

        user_line = utils.get_user_line(shadow_file)
        shadow_crack(user_line)

        if raw_input("Again? (y/n)").lower() not in ['y', 'yes']:
            break
