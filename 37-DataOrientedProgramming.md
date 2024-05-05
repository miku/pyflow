# Data Oriented Programming


# Data Validation with Pydantic

* allows to model data, with type annotations

```
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Jane Doe'
``` 

Models support a variety of extra methods, e.g. for exporting like `json`,
`dict` or JSON schema. Validation can be circumvented with `construct`.

Examples: [Snippets/Pydantic](Snippets/Pydantic)