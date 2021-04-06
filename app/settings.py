import os
import sys
from custom_functions import*

OS = os.name
SERVER_IP = get_ip(OS)
print('SERVER_IP:', SERVER_IP)
print('OS:', os_translate[OS])