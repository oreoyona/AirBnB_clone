#!/usr/bin/python3
"""Creates a FileStorage instance for the console"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
