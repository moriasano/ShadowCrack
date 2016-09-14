""" This code cracks the password for a given user from the shadow file """
import ui


def shadow_crack(shadow_file, username):
    """
    Main logic flow for the shadow file crack
    :param shadow_file: the shadow file
    :param username: the username of the password to crack
    :return: the cracked password
    """
    pass

if __name__ == '__main__':
    ui.welcome()
    shadow_path, username = ui.get_sc_params()
