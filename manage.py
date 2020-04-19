from flask_script import Manager

from product import app
from product.scripts.db import DataBaseInitialization

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("init_db", DataBaseInitialization())
    manager.run()
