# 📊 Procesador de Asistencia Zoom - Semillero Digital

**🚀 [¡HAZ CLIC AQUÍ PARA USAR LA APLICACIÓN EN VIVO!](https://semillero-asistencia.streamlit.app/) 🚀**

Esta es una aplicación web ligera construida con...

Esta es una aplicación web ligera construida con Streamlit diseñada para automatizar la limpieza, unificación y cálculo de minutos de los reportes de asistencia generados por Zoom.

## 🚀 Características Principales

Extracción Inteligente de DNI: Detecta automáticamente números de DNI (de 7 a 8 dígitos) dentro de los nombres de los usuarios de Zoom, incluso si contienen puntos.
Limpieza de Nombres: Elimina caracteres extraños (guiones, paréntesis, corchetes, palitos |) y borra automáticamente la palabra "DNI" escrita por error junto al nombre.
Fusión de Duplicados: Si un alumno se desconecta y vuelve a entrar, el sistema unifica sus registros bajo un mismo DNI y suma los minutos totales que estuvo conectado.
Exportación a Excel: Transforma el caótico CSV de Zoom en un archivo Excel (.xlsx) limpio, ordenado y listo para cruzar datos (BUSCARV).

## 📂 Estructura de Archivos

Para que la aplicación funcione, solo necesitas dos archivos en tu repositorio:
app_asistencia.py: Contiene toda la lógica de Python y la interfaz de Streamlit.
requirements.txt: Lista de librerías necesarias para que la nube sepa qué instalar.

## ☁️ Cómo desplegar en Streamlit Cloud (Gratis)

La forma más fácil de compartir esta herramienta con tu equipo es alojándola en la nube de Streamlit.
Sube los archivos app_asistencia.py y requirements.txt a un repositorio público en GitHub.
Entra a Streamlit Cloud e inicia sesión con tu cuenta de GitHub.
Haz clic en "New app".
Selecciona tu repositorio, asegúrate de que la rama sea main y en "Main file path" escribe app_asistenciaV2.py.
Haz clic en "Deploy". En un par de minutos tendrás un enlace público para compartir con los moderadores.

## 💻 Instalación Local (Para pruebas en tu PC)

Si prefieres correr la aplicación en tu propia computadora, sigue estos pasos:
Asegúrate de tener Python instalado.
Abre tu terminal o consola de comandos y navega hasta la carpeta del proyecto.
Instala las dependencias ejecutando:
pip install -r requirements.txt


Ejecuta la aplicación de Streamlit:

streamlit run app_asistenciaV2.py


Se abrirá automáticamente una pestaña en tu navegador web con la herramienta funcionando.

## 🛠️ Tecnologías Utilizadas

Python: Lenguaje principal.

Streamlit: Framework para crear la interfaz web de forma rápida.

Pandas: Para la manipulación, agrupación y limpieza de los datos.

Regex (Expresiones Regulares): Para buscar y aislar los DNIs y limpiar el texto con precisión matemática.

XlsxWriter: Motor para exportar los DataFrames a formato Excel.
