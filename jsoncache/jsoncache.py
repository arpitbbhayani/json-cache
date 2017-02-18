import os

from . import fileio
from . import utils
from .errors import CacheError, CacheInitError, ArgumentError, CacheIOError


class JSONCache:
    def __init__(self, cache_filepath):
        self.fp = cache_filepath

        if os.path.isdir(self.fp):
            raise CacheInitError("Error while initializing cache: {}"
                                 .format("Folder exists instead of file"))

        try:
            if not os.path.exists(self.fp):
                fileio.write_json(self.fp, {})
            fileio.read_json(self.fp)
        except CacheIOError as e:
            raise CacheInitError("Error while initializing cache: {}"
                                 .format(str(e.description)))

    def get(self, *args):
        if len(args) == 0:
            raise ArgumentError("Atleast one key should be given.")

        data = fileio.read_json(self.fp)
        try:
            for k in args:
                data = data.get(k)
        except KeyError as e:
            raise NotInCacheError("Path {} does not exist in cache"
                                  .format(args))
        return data

    def put(self, *args):
        if len(args) == 0:
            raise ArgumentError("Atleast key and value should be given")

        if len(args) == 1:
            raise ArgumentError("Value to be stored not given")

        data = fileio.read_json(self.fp)
        utils.update_dict(data, args)
        fileio.write_json(self.fp, data)
