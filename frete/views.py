from .models import Hamburgueria, FaixaFrete
from django.shortcuts import render
import requests

def calcula_frete(request):
    resultado = None

    if request.method == 'POST':
        rua = request.POST['rua']
        num = request.POST['num']
        city = request.POST['city']

        # Código para obter latitude e longitude do endereço do cliente

        end = rua + ',' + num + ',' + city

        url2 = f'https://api.tomtom.com/search/2/geocode/{end}.json?storeResult=false&countrySet=brazil&view=Unified&key=ZGcQ0Al5GgxUVhPBpYLQCF7xWYoKyZqZ'

        response1 = requests.get(url2, timeout=6)
        data2 = response1.json()

        if response1.status_code == 200:

            latitude = str(data2['results'][0]['position']['lat'])
            longitude = str(data2['results'][0]['position']['lon'])

            endereco = latitude + ',' + longitude

        else:
        
            print(f'Geocoding failed! Error={response1.status_code}\n')


        # Obtendo as coordenadas da hamburgueria a partir do modelo
        hamburgueria = Hamburgueria.objects.first()  # Obtém a primeira hamburgueria (altere conforme necessário)

        latitude_hamburgueria = str(hamburgueria.latitude)
        longitude_hamburgueria = str(hamburgueria.longitude)

        l1 = str(latitude_hamburgueria + ',' + longitude_hamburgueria)

        url = f'https://api.tomtom.com/routing/1/calculateRoute/{l1}:{endereco}/json?routeType=eco&travelMode=car&key=ZGcQ0Al5GgxUVhPBpYLQCF7xWYoKyZqZ'

        response = requests.get(url, timeout=6)
        data = response.json()

        if response.status_code == 200:

            Distancia = data['routes'][0]['summary']['lengthInMeters']

            distancia_em_km = (Distancia / 1000)

        else:
        
            print(f'Routing failed! Error={response.status_code}\n')


        # Cálculo da distância usando latitude e longitude do cliente e da hamburgueria
        

        faixa_frete = FaixaFrete.objects.filter(hamburgueria=hamburgueria,
                                                distancia_minima__lte=distancia_em_km,
                                                distancia_maxima__gte=distancia_em_km).first()

        if faixa_frete:
            Frete = f'R$ {faixa_frete.valor_frete} reais.'
        else:
            Frete = 'Região não atendida!'

        resultado = f'O frete para {rua}, {num}, {city} é: {Frete}'

    return render(request, 'calcula_frete.html', {'resultado': resultado})

