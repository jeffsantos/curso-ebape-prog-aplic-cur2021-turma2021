# Prerequirements:
# 
# 1. install firefox on the repl:
# install-pkg firefox
#
# 2. define firefox as installed browser:
# export BROWSER=firefox
#
# 3. run the code
#
# OBS.: busybox reboot (in case of freezing)

import sys, webbrowser

print(sys.argv)

endereco = " ".join(sys.argv[1:])

webbrowser.open(f"https://www.google.com/maps/place/{endereco}")
