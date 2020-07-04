from django.core.paginator import Paginator

def getObject(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return None

def getSpecificFilter(params, filter):
    if filter in params:
        return params[filter]
    return None

def genericQuery(model, filters, ordering):

    results = []
    page = 1
    quantByPage = 20

    if filters:
        pageGetRequest = filters.pop('page', None)
        quantByPageGetRequest = filters.pop('quant_by_page', None)
        page = int(pageGetRequest) if pageGetRequest else 1
        quantByPage = int(quantByPageGetRequest) if quantByPageGetRequest else 20

    if ordering:
        if isinstance(ordering, list):
            results = model.objects.filter(**filters).order_by(*ordering)
        else:
            results = model.objects.filter(**filters).order_by(ordering)
    else:
        results = model.objects.filter(**filters)

    paginator = Paginator(results, quantByPage)
    finalResults = paginator.get_page(page)
    return finalResults

def updateObject(model, object, data):
    model.objects.filter(pk=object.pk).update(**data)
    return model.objects.get(pk=object.pk)