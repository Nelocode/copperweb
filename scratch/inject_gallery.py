import re

# Translation mapping for gallery texts
translations = {
    "Content Gallery": "Galería de Contenido",
    "Videos": "Videos",
    "Photo Gallery": "Galería de Fotos",
    "Geology Part 4 | Mocoa's Magmatic Heart": "Geología Parte 4 | El Corazón Magmático de Mocoa",
    "Geology Part 3 | Magma Fertility": "Geología Parte 3 | Fertilidad del Magma",
    "Geology Part 2 | Tectonic Setting": "Geología Parte 2 | Configuración Tectónica",
    "Episode 2 | Why Mocoa": "Episodio 2 | Por qué Mocoa",
    "Meet the Team Part 2 | Joey Wilkins": "Conoce al Equipo Parte 2 | Joey Wilkins",
    "Meet the Team Part 3 | Joey Wilkins": "Conoce al Equipo Parte 3 | Joey Wilkins",
    "Geology Part 1 | The Making of a Copper Giant": "Geología Parte 1 | La Creación de un Gigante del Cobre",
    "Episode 1: Why Mocoa": "Episodio 1: Por qué Mocoa",
    "Meet The Team | Thyana Álvarez": "Conoce al Equipo | Thyana Álvarez",
    "Rule Symposium 2025 | Copper Giant": "Simposio Rule 2025 | Copper Giant",
    "Copper Giant Launches | Backed by Frank Giustra": "Lanzamiento de Copper Giant | Respaldado por Frank Giustra",
    "Libero Copper Announces Full 1,141-Metre Drill Hole from Surface Average 0.46% CuEq at Mocoa": "Libero Copper Anuncia un Pozo Completo de 1,141 Metros desde la Superficie con Promedio de 0.46% CuEq en Mocoa",
    "News Release - November 6, 2024 | 14,000 Metre Exploration Program at Mocoa Update": "Comunicado de Prensa - 6 de Noviembre de 2024 | Actualización del Programa de Exploración de 14,000 Metros en Mocoa",
    "Libero Copper Extracts Copper Metal from the Mocoa Deposit with the National University of Colombia": "Libero Copper Extrae Cobre Metálico del Yacimiento Mocoa con la Universidad Nacional de Colombia",
    "ESG: Libero Copper Works Together with the Community at Putumayo": "ESG: Libero Copper Trabaja Junto a la Comunidad en Putumayo",
    "Pedestrian Bridge": "Puente Peatonal",
    "Bridge Aerial View": "Vista Aérea del Puente",
    "Water Sampling": "Muestreo de Agua",
    "Libero Cobre Team": "Equipo de Libero Cobre",
    "Mocoa Valley Landscape": "Paisaje del Valle de Mocoa",
    "Nursery &amp; Reforestation": "Vivero y Reforestación",
    "Nursery & Reforestation": "Vivero y Reforestación",
    "Community Engagement": "Compromiso Comunitario",
    "Community Presentation": "Presentación a la Comunidad",
    "Community Meeting": "Reunión Comunitaria",
    "Field Crew in the Jungle": "Personal de Campo en la Selva",
    "Community Event": "Evento Comunitario",
    "Community Gathering": "Reunión de la Comunidad",
    "Community Town Hall": "Asamblea Comunitaria",
    "Core Sample Inspection": "Inspección de Muestras de Testigo",
    "Community Speaker": "Orador Comunitario",
    "Community Forum": "Foro Comunitario",
    "Community Dialogue": "Diálogo Comunitario",
    "Aerial View of Site": "Vista Aérea del Sitio",
    "Community Voice": "Voz de la Comunidad",
    "Community Workshop": "Taller Comunitario",
    "Ruta Verde Event": "Evento Ruta Verde",
    "Ruta Verde Gathering": "Reunión Ruta Verde",
    "Night Community Event": "Evento Comunitario Nocturno",
    "Core Samples Close-up": "Primer Plano de Muestras de Testigo",
    "Tree Planting": "Plantación de Árboles",
    "Workshop Activity": "Actividad de Taller",
    "Reforestation Work": "Trabajo de Reforestación",
    "Ridge Trail": "Sendero de la Cumbre",
    "Mineralized Core": "Testigo Mineralizado",
    "Field Water Sampling": "Muestreo de Agua en Campo",
    "Workers Descending Hill": "Trabajadores Descendiendo la Colina",
    "Worker Sawing Wood": "Trabajador Cortando Madera",
    "Bridge Community Group": "Grupo Comunitario del Puente",
    "Core Handling": "Manipulación de Testigos",
    "Drill Rig Equipment": "Equipo de la Plataforma de Perforación",
    "Drill Rig Operations": "Operaciones de la Plataforma de Perforación",
    "Team in the Field": "Equipo en el Campo",
    "Crew Lining Up": "Personal en Fila",
    "Geologists Examining Core": "Geólogos Examinando Testigos",
    "Team Photo": "Foto del Equipo",
    "Core Sample Analysis": "Análisis de Muestras de Testigo",
    "Geologist with Core": "Geólogo con Testigo",
    "Jungle Trail": "Sendero en la Selva",
    "Carrying Equipment": "Transporte de Equipo",
    "Cobbler Artisan": "Artesano Zapatero",
    "Embroidery Machine": "Máquina de Bordado",
    "Libero Cobre Staff": "Personal de Libero Cobre",
    "Community Planning Session": "Sesión de Planificación Comunitaria",
    "Drill Rig Control Room": "Sala de Control de la Plataforma de Perforación"
}

with open('scratch/mocoa_content_gallery_clean.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the backslash issues
html = html.replace(r'<\/div>', '</div>')

# Perform translations
for eng, esp in translations.items():
    # Replace in attributes like alt="..." and text content
    html = html.replace(f'alt="{eng}"', f'alt="{esp}"')
    html = html.replace(f'alt="{eng.replace("&", "&amp;")}"', f'alt="{esp}"')
    html = html.replace(f'>{eng}<', f'>{esp}<')
    html = html.replace(f'"{eng}"', f'"{esp}"')

# Wrap in section structure
gallery_section = f"""
    <!-- Content Gallery Section -->
    <section class="section-padding" id="gallery" style="background: rgba(10, 10, 10, 0.4); backdrop-filter: blur(24px); border-top: 1px solid rgba(255, 255, 255, 0.05);">
        <div class="container fade-up">
            <div class="text-eyebrow">Multimedia</div>
            {html}
        </div>
    </section>
"""

# Read mocoa.html
with open('mocoa.html', 'r', encoding='utf-8') as f:
    mocoa_content = f.read()

# Inject before footer
footer_tag = '<!-- Footer -->'
if footer_tag in mocoa_content:
    parts = mocoa_content.split(footer_tag)
    new_mocoa_content = parts[0] + gallery_section + "\n    " + footer_tag + parts[1]
    
    with open('mocoa.html', 'w', encoding='utf-8') as f:
        f.write(new_mocoa_content)
    print("Successfully injected gallery into mocoa.html")
else:
    print("Error: Could not find footer tag in mocoa.html")
