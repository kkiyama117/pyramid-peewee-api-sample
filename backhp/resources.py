from peewee import *
import pathlib
from pyramid.request import Request


def connect():
    pass


database_path = pathlib.Path().parent / 'main.sqlite'
# SQLite database using WAL journal mode and 64MB cache.
db = SqliteDatabase(database_path.absolute(), pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,  # 64MB
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})


class MyRequest(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        db.connect()
        self.add_finished_callback(self.finish)

    def finish(self, request):
        if not db.is_closed():
            db.close()
