  ____  _               _                ____                _
 / ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | __
 \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |   | '__/ _` |/ __| |/ /
  ___) | | | | (_| | (_| | (_) \ V  V /| |___| | | (_| | (__|   <
 |____/|_| |_|\__,_|\__,_|\___/ \_/\_/  \____|_|  \__,_|\___|_|\_\
						                           Mori Asano 2016

Overview:
This python tool can be used to crack/recover a password from the
shadow file in linux systems. Currently, the mode of attack is a
dictionary attack, further modes may be implemented in the future.

The default dictionary is the 'phpbb.txt' leaked password dictionary.
The dictionary is specified in utils.py as a constant.
To use a different dictionary, add the dictionary to the directory
and specify the filename in utils.py @ PASSWORDS = 'filename.txt'

Currently ShadowCrack only supports passwords hashed with SHA512



Usage:
The code is to be interpreted with Python 2.7 (currently not tested against 3.x)
                * This tool only works with linux systems *

From the terminal, navigate to the assignment2 directory.
Type: 'sudo python assignment2.py'
System may prompt for root credentials.

Continue to follow the tool prompts.

