# jsoncache

**jsoncache** is a file-based cache though which you can put and fetch
data; thus giving you an ability to easily update a small chunk of data in
a JSON file. In short you can use this library to manipulate any JSON file.

## Motivation
For storing data in [bucket-list](https://github.com/arpitbbhayani/bucket-list)
for any external provider like Wunderlist, I used to make a lot of network
calls. Some of those calls were redundant. Because of these redundant calls
the utility became slower when any external provider is used. So I created
**jsoncache** which can help me cache the responses of some of the API calls
and eventually make the utility faster.

## Installation
Installing `jsoncache` is as easy as

```bash
pip install jsoncache
```

## Getting started with jsoncache

```python
>>> from jsoncache import JSONCache
>>> j = JSONCache()
>>> j.put('name', 'firstname', 'Arpit')
>>> j.get('name', 'firstname')
'Arpit'
>>> j.save()  # writes to the cache file
```

To initialize a JSONCache all you have to do is create its object. The default
cache file is `cache.json` and autosave feature is `off`. So all of your JSON
content will be saved in memory in a dictionary. For more information about the
options of JSONCache, go through the documentation.

`.put(*args)`, `.get(*args)` and `save()` are three methods exposed in
JSONCache object which are used to put something into cache, get something
from the cache and save the contents on the disk in a JSON file.
The last argument passed in `put` method should be the value (object) to be
stored in cache and this object should be JSON serializable.

If something is not cache and you are trying to fetch it,
`NotInCacheError` error is raised.

More info about `get`, `put`, `delete`, `save` and `errors` can be found in
documentation [here](../../wiki).

## Advantages
Now you may say, what's new with this; I can simply use `import json`.

But hold on, there is one advantage using this library and that is syntactic sugar and convinience.
Suppose you have to fetch firstname from json below

```json
{
    "home_user": {
        "name": {
            "firstname": "Arpit"
        }
    }
}
```
If you use `json` module, your code wil look something like this
```python
name = j.get('home_user').get('name').get('firstname')
```

With this piece of code, you have to check if key exists and if not handle exceptions
and/or None values.

With this library you can do just this
```python
j.get('home_user', 'name', 'firstname')
```
Above code will raise an exception if any of the key does not exist.

Similarly while putting data into JSON. You have to explicitly take care that all intermediatory
keys exist. But with this you can do simply this

```python
j.put('home_user', 'name', 'firstname', 'Arpit')
```

## Documentation
A compehensive documentation can be found [here](../../wiki).
Lot of efforts have been put into this, hope you find it useful :smile:

## Contribution
In case you loved this utility and have a great feature idea, then feel free
to contribute . The complete utility is written in
[Python](https://docs.python.org/). So for contributing all you need to have
is working knowledge of Python.

You can find source code [here](https://github.com/arpitbbhayani/jsoncache).

Here are some [ideas](../../wiki/Future-Features) that you may love to work on.

## Issues
Please report any glitch, bug, error or an unhandled exception :frowning: Feel
free to [create one](../../issues/new).
