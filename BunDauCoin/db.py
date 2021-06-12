import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from . import block

"""
    +==============================+
    |   Singleton-like db access   |
    +==============================+
"""
##
## Gets the database.
##
## :returns:   The database.
## :rtype:     { return_type_description }
##
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

##
## Closes a database.
##
## :param      e:    { parameter_description }
## :type       e:    { type_description }
##
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

"""
    +=============+
    |   Builder   |
    +=============+
"""
##
## Initializes the database.
##
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

"""
    +===========================+
    |   Command line function   |
    +===========================+
"""
##
## Initializes the database command.
##
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

##
## Initializes within the application.
##
## :param      app:  The application
## :type       app:  { type_description }
##
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


"""
    +======================+
    |   Blockchain tools   |
    +======================+
"""

#
#   Getters
#

##
## Gets the blockchain length.
##
## :returns:   The blockchain length.
## :rtype:     int
##
def getBlockchainLength() -> int:
    return tuple(get_db().execute("SELECT COUNT(*) FROM bun_dau_blockchain").fetchone())[0]

##
## Gets the latest block.
##
## :returns:   The latest block.
## :rtype:     block.Block
##
def getLatestBlock() -> block.Block:
    lastRow = tuple(get_db().execute(
                'SELECT * FROM bun_dau_blockchain ORDER BY id DESC LIMIT 1'
            ).fetchone())[0]
    print(lastRow)
    return block.Block##(index=lastRow[0], previousHash=lastRow[1], timestamp=lastRow[2], data=lastRow[3], hash=lastRow[4])


#
#   Setters
#

##
## Adds a new block.
##
## :param      newBlock:  The new block to add in the chain
## :type       newBlock:  block.Block
##
## :returns:   Success saving the new block
## :rtype:     bool
##
def addNewBlock(newBlock: block.Block) -> bool:
    db = get_db()
    db.execute(
                'INSERT INTO bun_dau_blockchain (previousHash, timestamp, data, hash) VALUES (?, ?, ?, ?)',
                (newBlock.previousHash, newBlock.timestamp, newBlock.data, newBlock.hash)
            )
    return db.commit()

def replaceChain(newBlocks, startIndex: int) -> bool:
    success = False

    db = get_db()
    db.execute(
        'INSERT INTO user (username, password) VALUES (?, ?)',
        (username, generate_password_hash(password))
    )
    db.commit()

    return success