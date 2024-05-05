import pickle
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None


m = User.parse_obj({'id': 123, 'name': 'James'})
print(m)
#> id=123 signup_ts=None name='James'

try:
    User.parse_obj(['not', 'a', 'dict'])
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    __root__
      User expected dict not list (type=type_error)
    """

# assumes json as no content type passed
m = User.parse_raw('{"id": 123, "name": "James"}')
print(m)
#> id=123 signup_ts=None name='James'

pickle_data = pickle.dumps({
    'id': 123,
    'name': 'James',
    'signup_ts': datetime(2017, 7, 14)
})
m = User.parse_raw(
    pickle_data, content_type='application/pickle', allow_pickle=True
)
print(m)
#> id=123 signup_ts=datetime.datetime(2017, 7, 14, 0, 0) name='James'

path = Path('data.json')
path.write_text('{"id": 123, "name": "James"}')
m = User.parse_file(path)
print(m)
#> id=123 signup_ts=None name='James'