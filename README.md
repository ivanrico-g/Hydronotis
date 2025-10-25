<p align="center">
  <img src="https://iili.io/KrntDRp.png" alt="Hydronotis" width="480" />
</p>

> Sistema automático para scraping y envío de mensajes por WhatsApp para notificar turnos de cortes de agua en Bogotá.

---

## 🔎 Descripción
Hydronotis es una pequeña herramienta en Python que automatiza la detección de avisos de cortes de agua y notifica al usuario vía WhatsApp usando la API de CallMeBot. Está pensada para procesar la información públicamente publicada sobre cortes, transformar los datos relevantes y distribuir alertas.

---

## 🧰 Tecnologías
- Python
- FastAPI (opcional para exponer endpoints o API interna)
- Requests / BeautifulSoup (para scraping)
- API: `Callmebot` (envío de mensajes por WhatsApp)
- GitHub Actions (CI / CD)

---

## ✨ Características
- Scraping a la pagina oficial de la alcaldia para buscar informacion actual de los turnos de cortes de agua.
- Envío programado de alertas activadas por GitHub Actions programadas para ciertas horas.
- Hooks / endpoints para disparar scrapes y reintentos.
