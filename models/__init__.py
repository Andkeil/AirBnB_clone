#!/usr/bin/python3
"""module: init"""


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
