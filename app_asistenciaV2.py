import streamlit as st
import pandas as pd
import re
import io

st.set_page_config(page_title="Procesador de Asistencia Zoom", page_icon="📊")

st.title("📊 Procesador de Asistencia Zoom")
st.markdown("Sube tu archivo `.csv` de Zoom. El sistema unificará los DNIs duplicados, sumará los minutos y limpiará los nombres.")

# Función para extraer el DNI
def extraer_dni(texto):
    match = re.search(r'(\d[\d\.]{6,10}\d)', str(texto))
    if match:
        return match.group(0).replace('.', '')
    return "Sin DNI"

# Función para limpiar el nombre
def limpiar_nombre(texto):
    nombre = str(texto)
    # 1. Quitar los números de DNI
    nombre = re.sub(r'(\d[\d\.]{6,10}\d)', '', nombre)
    # 2. Quitar la palabra literal "Dni" o "DNI" (sin importar mayúsculas)
    nombre = re.sub(r'(?i)\bdni\b', '', nombre)
    # 3. Quitar caracteres especiales como - | ( ) [ ]
    nombre = re.sub(r'[\-\|()\[\]]', '', nombre)
    # 4. Limpiar espacios dobles o extra
    nombre = " ".join(nombre.split())
    
    return nombre.title() # Pone la primera letra en mayúscula

uploaded_file = st.file_uploader("Elige el archivo CSV de Zoom", type="csv")

if uploaded_file is not None:
    try:
        # Leer el archivo
        df = pd.read_csv(uploaded_file)
        
        # Identificar las columnas (por si Zoom cambia levemente el nombre)
        col_nombre = [c for c in df.columns if 'Nombre' in c][0]
        col_duracion = [c for c in df.columns if 'Duración' in c][0]
        
        # Aplicar limpieza
        df['dni'] = df[col_nombre].apply(extraer_dni)
        df['nombre_apellido'] = df[col_nombre].apply(limpiar_nombre)
        
        # --- LA MAGIA CONTRA LOS DUPLICADOS ---
        
        # Separamos los que tienen DNI de los que no (para no mezclar a todos los invitados)
        df_con_dni = df[df['dni'] != "Sin DNI"]
        df_sin_dni = df[df['dni'] == "Sin DNI"]
        
        # Agrupamos SOLO por DNI. 
        # Sumamos la duración y nos quedamos con el "primer" nombre que aparezca.
        agrupado_dni = df_con_dni.groupby('dni', as_index=False).agg({
            'nombre_apellido': 'first', 
            col_duracion: 'sum'
        })
        
        # A los que no tienen DNI los agrupamos por nombre
        agrupado_sin_dni = df_sin_dni.groupby('nombre_apellido', as_index=False).agg({
            'dni': 'first',
            col_duracion: 'sum'
        })
        
        # Unimos las dos tablas
        df_final = pd.concat([agrupado_dni, agrupado_sin_dni], ignore_index=True)
        
        # Ordenamos las columnas para el Excel
        df_final = df_final[['dni', 'nombre_apellido', col_duracion]]
        df_final.columns = ['DNI', 'Nombre y Apellido', 'Minutos Totales']
        
        st.success("¡Archivo procesado! Duplicados eliminados y minutos sumados.")
        st.dataframe(df_final)

        # Preparar Excel para descargar
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_final.to_excel(writer, index=False, sheet_name='Asistencia Limpia')
        
        st.download_button(
            label="📥 Descargar Excel Limpio",
            data=output.getvalue(),
            file_name="asistencia_zoom_limpia.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
    except Exception as e:
        st.error(f"Hubo un problema al procesar el archivo: {e}")