# Tapioca jarbas
[![CircleCI](https://circleci.com/gh/daneoshiga/tapioca-jarbas.svg?&style=shield)](https://circleci.com/gh/daneoshiga/tapioca-jarbas/)
[![PyPI version](https://badge.fury.io/py/tapioca-jarbas.svg)](https://badge.fury.io/py/tapioca-jarbas)

## Installation
```
pip install tapioca-jarbas
```

## Documentation
``` python
from tapioca_jarbas import Jarbas


api = Jarbas()
result = api.documents().get(params={'state':'SP'})
result().data

# Example access to supplier endpoint
cnpj = result().data['results'][2]['cnpj_cpf']
supplier = api.supplier(cnpj=cnpj).get()
supplier().data


# Example access to receipt endpoint
document_pk = result().data['results'][2]['id']
result = api.receipt(document_pk=document_pk).get()
result().data

```

No more documentation needed.

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
