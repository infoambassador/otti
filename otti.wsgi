activate_this = '/var/www/otti/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/otti/")

from otti import app as application
application.secret_key = 'Podcaster1'
