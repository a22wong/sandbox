import os
print(os.path)
DIR = 'alwaysListening/'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
