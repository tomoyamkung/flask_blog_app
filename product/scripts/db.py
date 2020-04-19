from flask_script import Command

from product.models.entries import Entry


class DataBaseInitialization(Command):
    def run(self):
        if not Entry.exists():
            Entry.create_table(read_capacity_units=5, write_capacity_units=2)
