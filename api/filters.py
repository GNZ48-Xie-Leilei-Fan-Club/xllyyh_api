import re

from rest_framework_json_api.filters import QueryParameterValidationFilter

class CustomQueryParameterValidationFilter(QueryParameterValidationFilter):
        query_regex = re.compile(r'^(sort|include)$|^(filter|fields|page|spm)(\[[\w\.\-]+\])?$')
