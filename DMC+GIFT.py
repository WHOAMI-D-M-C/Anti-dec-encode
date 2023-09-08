import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from gift import dmc_main
    dmc_main()
elif bit == '32bit':
    from gift import dmc_main
    dmc_main()
