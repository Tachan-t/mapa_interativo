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
        "categoria": "turismo",
        "descricao": "um dos pontos turisticos mais visitados de São Paulo"
    },
    {
        "nome": "Parque ibirapuera",
        "latitude": -23.5874,
        "longitude": -46.6576,
        "categoria": "parque",
        "descricao": "Um parque referencia no centro de São Paulo para relaxar"
    }
]

def adicionar_marcador(mapa, nome, latitude, longitude, categoria, descricao):

    if categoria == "parque":
        cor = "green"
    elif categoria == "turismo":
        cor = "blue"
    else:
        cor = "red"

    informacao = f"Local: {nome}, Categoria: {categoria}, Descricao: {descricao} "

    folium.Marker(
        location=[latitude, longitude],
        popup=folium.Popup(informacao, max_width=300),
        icon=folium.Icon(color=cor)
    ).add_to(mapa)

for local in locais:
    adicionar_marcador(
        mapa,
        local["nome"],
        local["latitude"],
        local["longitude"],
        local["categoria"],
        local["descricao"]
    )
    print(local["nome"], local["categoria"], local["descricao"])

mapa.save("mapa.html") #pega a variavel do objeto criado e salva em um arquivo