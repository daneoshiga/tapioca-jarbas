RESOURCE_MAPPING = {
    'reimbursement': {
        'resource': 'reimbursement/{year}/{applicant_id}/{document_id}',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apireimbursementyearapplicant_iddocument_id',
    },
    'receipt': {
        'resource': 'reimbursement/{year}/{applicant_id}/{document_id}/receipt',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apireimbursementyearapplicant_iddocument_idreceipt',
    },
    'reimbursement_list': {
        'resource': 'reimbursement/',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apireimbursement',
    },
    'reimbursement_list_year': {
        'resource': 'reimbursement/{year}',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apireimbursementyear',
    },
    'reimbursement_list_year_applicant': {
        'resource': 'reimbursement/{year}/{applicant_id}',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apireimbursementyearapplicant_id',
    },
    'subquota': {
        'resource': 'subquota',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apisubquota',
    },
    'applicant': {
        'resource': 'applicant',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apiapplicant',
    },
    'company': {
        'resource': 'company/{cnpj}',
        'docs': 'https://github.com/datasciencebr/jarbas#get-apicompanycnpj',
    },
}
