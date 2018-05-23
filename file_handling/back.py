

import os
import shutil
target_file = "/var/www/html/index.html"

shutil.copyfile ("target_file", "target_file_backup")
f = open("/var/www/html/index.html" , "a")

f.write("Hello from python from agian hello")

f.close()
