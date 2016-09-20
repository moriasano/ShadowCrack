""" This code cracks the password for a given user from the shadow file """
import utils


def shadow_crack(shadow_file, username):
    """
    Main logic flow for the shadow file crack
    :param shadow_file: the shadow file
    :param username: the username of the password to crack
    :return: the cracked password
    """
    # Scan file for the relevant line
    user_line = None
    for line in open(shadow_file, 'r').readlines():
        if username in line:
            user_line = line
            break

    # Break if user is not found
    if user_line is None:
        print("User '%s' was not found" % username)
        return

    # Extract the needed data from the line
    hash_alg, salt, hashed_pwd = user_line.split(":")[1].split("$")[1:]
    print("Hash Alg.:   %s" % utils.HASH_ALGS[hash_alg][0])
    print("Salt:        %s" % salt)
    print("Hashed PWD:  %s" % hashed_pwd)

    # Check for unsupported hash algorithms
    if hash_alg == "0" or hash_alg == "2a":
        print "Sorry. At this time %s is not supported by ShadowCrack" % utils.HASH_ALGS[hash_alg][0]
        return

    # Check for the hash against hashes of each dictionary entry
    pwd_dict = open(utils.PASSWORDS, mode='r')
    for pwd in pwd_dict:
        salted_pwd = salt + pwd
        hash_mech = utils.HASH_ALGS[hash_alg][0]

        with hash_mech(salted_pwd) as compare:
            if hashed_pwd == compare:
                print "Password cracked!    %s" % compare
                pwd_dict.close()
                return

    # Tear down
    print "Password has not been found against the dictionary."
    pwd_dict.close()

if __name__ == '__main__':
    utils.welcome()
    shadow_crack(utils.get_sc_params())
