import folium #é uma biblioteca para criação de mapas interativos
 
mapa = folium.Map( #cria um objeto de mapa
    location=[-23.5505, -46.6333], #define as coordenadas geograficas
    zoom_start=12 #determina a aproximiação incial
)

folium.Marker( #cria um marcardor geografico
    location=[-23.5505, -46.6333],
    popup="Centro de São Paulo", #define o texto exibido ao clicar no marcador
    tooltip="Clique para visualizar"
).add_to(mapa)

locais = [
    {
        "nome": "Avenida Paulista",
        "latitude": -23.5614,
        "longitude": -46.6565,
        "categoria": "turismo"
    },
    {
        "nome": "Parque ibirapuera",
        "latitude": -23.5874,
        "longitude": -46.6576,
        "categoria": "parque"
    }
]

def adicionar_marcador(mapa, nome, latitude, longitude, categoria):
    print(f"Local cadastrado: {nome}, {categoria}")
    categoria = "parque"

    if categoria == "parque":
        cor = "green"
    elif categoria == "turismo":
        cor = "blue"
    else:
        cor = "red"

    folium.Marker(
        location=[latitude, longitude],
        popup=nome
        icon=folium.icon(color=cor)
    ).add_to(mapa)

for local in locais:
    adicionar_marcador(
        mapa,
        local["nome"],
        local["latitude"],
        local["longitude"],
        local["categoria"]
    )
    print(local["nome"], local["categoria"])

mapa.save("mapa.html") #pega a variavel do objeto criado e salva em um arquivo