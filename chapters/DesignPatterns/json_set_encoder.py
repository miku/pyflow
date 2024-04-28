# Customization of serialization by passing a custom encoder to json.dumps. The
# custom class inherits from the default so keeps all the behavior except for
# the specific use case, which in this case is support for set encoding.

import json

class SetEncoder(json.JSONEncoder):
    """
    Helper to encode python sets into JSON lists.

    So you can write something like this:

        json.dumps({"things": set([1, 2, 3])}, cls=SetEncoder)
    """

    def default(self, obj):
        """
        Decorate call to standard implementation.
        """
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

data = {"things": set((1, 2, 3, 4))}
print(json.dumps(data, cls=SetEncoder))
