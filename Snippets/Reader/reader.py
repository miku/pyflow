# The "read" method is implemented by various types.
#
# If you implement an access method and there is a way to go from some
# identifier to its content, think about implementing a read function - this
# would satisfy the principle of least surprise.

from urllib.request import urlopen

def cat(fileobj):
    print(fileobj.read())


# We can read a file.
with open("reader.py") as f:
    cat(f)

# We use the same function for a URL.
cat(urlopen("https://heise.de"))
