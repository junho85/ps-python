import sysconfig
import random

print(sysconfig.get_config_vars())
print(random.randint(0, 10))

if "king" in "king of test":
    print("king is there")