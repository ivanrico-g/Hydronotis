import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

url = "https://bogota.gov.co/"
response = requests.get(url, headers=headers)

print("✅ Inicio Proceso")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    div_element = soup.find(id="reporte1")

    if div_element:
        a_element = div_element.find("a")
        print("✅ Elemento div encontrado")

        if a_element:
            enlace = a_element.get("href", "No encontrado")
            enlace_completo = urljoin(url, enlace)  # Manejo de enlaces relativos

            subResponse = requests.get(enlace_completo, headers=headers)

            if subResponse.status_code == 200:
                subSoup = BeautifulSoup(subResponse.text, "html.parser")
                titlesElements = subSoup.find_all("h1")

                for title in titlesElements:
                    textTitle = title.get_text(strip=True)
                    print(f"textTitle: {textTitle}")

                    if "racionamiento" in textTitle.lower():
                        match = re.search(r"¡(.*?)!", textTitle)
                        cycle = match.group(1) if match else "No encontrado"

                        print(f"Ciclo encontrado: {cycle}")

                        strMenssage = ""
                        
                        if cycle.lower() == "turno 3" or cycle.lower() == "turno tres":
                            print("🔹 Es Turno 3")
                            strMenssage = "Mañana Corte de Agua!"
                        elif cycle.lower() == "turno 4" or cycle.lower() == "turno cuatro":
                            print("🔹 Es Turno 4")
                            strMenssage = "HOY Corte de Agua!"

                        # Solo enviar mensaje si hay contenido en strMenssage
                        if strMenssage:
                            subUrl = "https://api.callmebot.com/whatsapp.php?source=web&phone=+1234567890&apikey=1234567&text=" + urllib.parse.quote(strMenssage)
                            responseWhats = requests.get(subUrl, headers=headers)

                            if responseWhats.status_code == 200:
                                print("✅ Mensaje enviado con éxito")
                            else:
                                print(f"⚠️ Error al enviar mensaje. Código: {responseWhats.status_code}")

                        break  # Sale del for una vez encontrado un turno
                else:
                    print("⚠️ No se encontró un turno válido, no se enviará mensaje.")
            else:
                print(f"⚠️ Error al hacer sub Peticion. Código: {subResponse.status_code}")
        else:
            print("⚠️ No se encontró el enlace en el div reporte1")
    else:
        print("⚠️ No se encontró el div con la clase 'reporte1'")
else:
    print(f"⚠️ Error al obtener la página. Código: {response.status_code}")
