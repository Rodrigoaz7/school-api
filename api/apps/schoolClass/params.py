from .models import Class
from utils.general import getSpecificFilter, getObject
from drf_yasg import openapi

def getSwaggerParams():
    listParams = [
        openapi.Parameter('name', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        openapi.Parameter('name_subclass', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        openapi.Parameter('order', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        openapi.Parameter('quant_by_page', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        openapi.Parameter('page', openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    ]
    return listParams

def getFiltersRequest(params):
    queryset = {}
    basicFilters = ['name', 'name_subclass', 'quant_by_page', 'page']
    fieldsStringContain = ['name', 'email', 'name_subclass']
    fieldsBoolean = []
    fieldsForeignKeys = []
    for field in basicFilters:
        filter = getSpecificFilter(params, field)
        if filter is not None:
            if field in fieldsStringContain:
                queryset[field+"__icontains"] = filter
                continue
            if field in fieldsBoolean:
                queryset[field] = True if filter.upper() in ['TRUE', '1'] else False
                continue
            if field in fieldsForeignKeys:
                queryset[field+"__pk"] = filter
                continue
            queryset[field] = filter

    return queryset

def getOrderingRequest(params):
    orderingString = getSpecificFilter(params, 'order')
    if not orderingString:
        return 'name' # default
    orderingArray = orderingString.strip().split(',')
    return orderingArray[0] if len(orderingArray) == 1 else orderingArray