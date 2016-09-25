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
    print "\nHash Alg.:   %s" % hash_name
    print "Salt:        %s" % salt
    print "Hashed PWD:  %s" % hashed_pwd

    # Check for unsupported hash algorithms
    if hash_mech is None:
        print "Sorry, At this time %s is not supported by ShadowCrack" % hash_name
        return

    print "\nStarting crack..."

    # Check for the hash against hashes of each dictionary entry
    with open(utils.PASSWORD_LIST, mode='r') as pwd_dict:
        start = timer()
        for pwd in pwd_dict:
            formatted_salt = "$%s$%s$" % (hash_alg, salt)  # crypt.crypt takes salt as '$6$salt'
            compare = hash_mech(pwd.strip(), formatted_salt)

            if formatted_salt + hashed_pwd == compare:
                end = timer()
                pwd_dict.close()
                print "Password cracked!    %s      in     %s" % \
                      (pwd, str(datetime.timedelta(seconds=(end - start))))
                return

    # Clean up
    print "Password has not been found against the dictionary."
    pwd_dict.close()
    return

if __name__ == '__main__':
    utils.welcome()
    shadow_file_path = utils.get_shadow_path()
    
    with open(shadow_file_path, mode='r') as shadow_file:
        while True:
            user_line = utils.get_user_line(shadow_file)
            shadow_crack(user_line)

            if raw_input("\nAgain? (y/n)").lower() not in ['y', 'yes']:
                break
