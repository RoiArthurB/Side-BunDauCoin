from flask import current_app, g
from flask.cli import with_appcontext

import datetime

from . import block

def genesisBlock():
    return block.Block(index=0, previousHash="0", timestamp=datetime.datetime.now(), data="Genesis Bun Dau Block")