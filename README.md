# 🛰️ RBMC Dashboard

## Autor

**GIGLAU**

Sempre por aí tentando conectar um receptor GNSS, frequentemente me deparei com problemas relacionados à escolha da estação NTRIP mais adequada, além das dificuldades causadas por soluções flutuantes, perda de precisão e a necessidade de interpretar grandes volumes de dados disponibilizados pelo IBGE.

Este projeto nasceu justamente dessa necessidade prática de campo.

---

## Objetivo

O IBGE disponibiliza os dados da RBMC (Rede Brasileira de Monitoramento Contínuo) através da Source Table do serviço NTRIP. Embora extremamente completa, essa informação é apresentada de forma textual e robusta, dificultando uma rápida análise espacial das estações disponíveis.

O objetivo deste projeto é transformar esses dados em uma visualização geográfica intuitiva, permitindo identificar rapidamente:

- Estações online da RBMC;
- Localização geográfica das bases;
- Distância em linha reta até o usuário;
- Estação mais próxima para conexão NTRIP;
- Informações técnicas de cada estação.

---

## Funcionalidades

### ✔ Mapa interativo

Visualização das estações da RBMC diretamente sobre o mapa do Brasil.

### ✔ Localização do usuário

Utiliza a geolocalização do dispositivo para posicionar o usuário no mapa.

### ✔ Estação mais próxima

Calcula automaticamente qual estação está mais próxima do usuário utilizando distância geodésica.

### ✔ Informações das estações

Ao clicar sobre uma estação é possível visualizar:

- Mountpoint
- Nome da estação
- Receptor utilizado
- Rede
- Formato RTCM
- Constelações suportadas
- Distância até o usuário

### ✔ Atualização da rede

Os dados podem ser atualizados diretamente a partir da Source Table disponibilizada pelo IBGE.

---

## Fonte dos Dados

Os dados utilizados pelo sistema são obtidos diretamente do serviço NTRIP da RBMC:

http://170.84.40.52:2101/

---

## Tecnologias Utilizadas

- Python
- Streamlit
- SQLite
- Folium
- CARTO
- Pandas

---

## Motivação Técnica

Em levantamentos GNSS utilizando correções NTRIP, a distância entre o rover e a estação de referência influencia diretamente a qualidade da solução.

Como regra prática frequentemente adotada em campo:

> A cada 100 km de distância até a estação de referência pode-se esperar aproximadamente 1 cm adicional de erro nas correções.

Por isso, conhecer rapidamente a estação mais próxima pode representar ganhos significativos de produtividade e precisão.

---

## Próximas Implementações
A decidir pela necessidade apresentada em campo 
---

## Dashboard Online

Acesse a versão pública do sistema:

https://rbmc-dashboard-hv5mzvaoev3czwhsduucxv.streamlit.app

---

## Licença

Projeto desenvolvido com fins educacionais, técnicos e de apoio à comunidade GNSS brasileira.
