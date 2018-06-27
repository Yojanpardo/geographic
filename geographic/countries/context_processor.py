from django.urls import reverse
def get_context_data(request):
    afganistan = {
        'name': 'Afganistán', 'code':'AFG', 'description':'Un pais que vive en guerra',
        'detail_url': reverse('countries:country_detail', kwargs={'code': 'AFG'})
    }
    argentina = {
        'name': 'Argentina', 'code':'ARG', 'description':'Narizones que se creen Europeos',
        'detail_url': reverse('countries:country_detail', kwargs={'code': 'ARG'})
    }
    brasil = {'name': 'Brasil', 'code':'BRA', 'description':'Gentesiña hablando rariño',
    'detail_url': reverse('countries:country_detail', kwargs={'code': 'BRA'})
    }
    chile = {'name': 'Chile', 'code':'CHI', 'description':'No lo sé, no tengo queja de Chile xdxd',
    'detail_url': reverse('countries:country_detail', kwargs={'code': 'CHI'})
    }
    colombia = {'name': 'Colombia', 'code':'CO', 'description':'El país donde los niños se mueren de hambre y la peor plaga de la historia se roba la plata de todos los colombianos',
    'detail_url': reverse('countries:country_detail', kwargs={'code': 'CO'})
    }
    dember = {'name': 'Dember', 'code':'DEM', 'description':'Solo sé que es el alias de un personaje de la casa de papel',
    'detail_url': reverse('countries:country_detail', kwargs={'code': 'DEM'})
    }
    dinamarca = {'name': 'Dinamarca', 'code':'DIN', 'description':'Iguanas verdes de Dinamarca',
    'detail_url': reverse('countries:country_detail', kwargs={'code': 'DIN'})
    }
    estocolmo = {'name': 'Estocolmo', 'code':'EST', 'description':'No sé nada de este país',
    'detail_url': reverse('countries:country_detail', kwargs={'code': 'EST'})
    }
    countries = [afganistan,argentina,brasil,chile,colombia,dember,dinamarca,estocolmo]

    africa = {'name':'África','description':'Hot', 'code_id':0}
    antartida = {'name':'Antártida', 'description':'Cold', 'code_id':1}
    america = {'name':'América','description':'new world', 'code_id':2}
    asia = {'name':'Asia','description':'Chinos', 'code_id':3}
    europa = {'name':'Europa','description':'conquers', 'code_id':4}
    oseania = {'name':'Oseania','description':'kangaroos', 'code_id':5}
    continents=[africa,antartida,america,asia,europa,oseania]
    return {'continents':continents,'countries':countries}
