from django.shortcuts import render
import requests

def calcula_frete(request):
    resultado = None

    if request.method == 'POST':
        rua = request.POST['rua']
        num = request.POST['num']
        city = request.POST['city']

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

        l1 = '-21.78883861232875,-48.15543298241844' #coordenadas hamburgueria

        url = f'https://api.tomtom.com/routing/1/calculateRoute/{l1}:{endereco}/json?routeType=eco&travelMode=car&key=ZGcQ0Al5GgxUVhPBpYLQCF7xWYoKyZqZ'

        response = requests.get(url, timeout=6)
        data = response.json()

        if response.status_code == 200:

            Distancia = data['routes'][0]['summary']['lengthInMeters']

            Km = (Distancia / 1000)

            #print(f'\nDistância = {data['routes'][0]['summary']['lengthInMeters']} metros\n')

            #print(f'Distância = {Km} Km\n')

        else:
        
            print(f'Routing failed! Error={response.status_code}\n')

        if Km > 5 and Km < 15:
            Frete = '15 reais'

        elif Km <= 5:
            Frete = '5 reais'

        else:
            Frete = 'Região não atendida!'

        print(f'Valor do Frete = {Frete}\n')
        
        resultado = f'O frete para {rua}, {num}, {city} é {Frete}'

    return render(request, 'form.html', {'resultado': resultado})
