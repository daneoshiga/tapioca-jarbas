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


jarbas = Jarbas()

# Get receipt url
receipt = jarbas.receipt(document_id=5920249).get()
receipt().data['url']
>>> http://www.camara.gov.br/cota-parlamentar/documentos/publ/2398/2016/5920249.pdf'

# Get specific reimbursement data
reimbursement = jarbas.reimbursement(year=2009, applicant_id=1701, document_id=1700354).get()
reimbursement().data
>> {'all_net_values': [80.34],
 'all_reimbursement_numbers': [3111],
 'all_reimbursement_values': None,
 'applicant_id': 1701,
 'batch_number': 431196,
 'cnpj_cpf': '05874470000106',
 'congressperson_document': 484,
 'congressperson_id': 74391,
 'congressperson_name': 'VIGNATTI',
 'document_id': 1700354,
 'document_number': '085273',
 'document_type': 0,
 'document_value': 80.34,
 'installment': 0,
 'issue_date': '2000-09-29',
 'leg_of_the_trip': '',
 'month': 9,
 'party': 'PT',
 'passenger': '',
 'probability': None,
 'receipt': {'fetched': True, 'url': None},
 'remark_value': 0.0,
 'state': 'SC',
 'subquota_description': 'Fuels and lubricants',
 'subquota_group_description': 'Veículos Automotores',
 'subquota_group_id': 1,
 'subquota_id': 3,
 'supplier': 'POSTO MARCON',
 'suspicions': None,
 'term': 2007,
 'term_id': 53,
 'total_net_value': 80.34,
 'total_reimbursement_value': None,
 'year': 2009
}

# Example deserialization
reimbursement.issue_date().to_datetime()
>> datetime.datetime(2000, 9, 29, 0, 0, tzinfo=tzutc())

total_net_value = reimbursement.total_net_value().to_decimal()
round(total_net_value, 2)
>> Decimal('80.34')

# Example pagination
subquota = jarbas.subquota().get()
subquota().data['count']
>>> 22

all_subquotas = [page().data for page in subquota().pages()]
len(all_subquotas)
>>> 22

# Example filtering
filtering = jarbas.reimbursement_list().get(params={'year': 2016, 'month': 1})

# Example search
applicants = jarbas.applicant().get(params={'q': 'liderança'})
applicants().data['results']
>>> [{'applicant_id': 2442, 'congressperson_name': 'LIDERANÇA DO PSDB'},
{'applicant_id': 2439, 'congressperson_name': 'LIDERANÇA DO PT'}]

```

No more documentation needed.

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
