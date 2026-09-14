# Campañas de Google Search — Consultora de Eficiencia Energética LE SAS

Estructura completa de Google Ads (Red de Búsqueda) para Valledupar y el Cesar,
lista para importar. Todo sale de `estructura.py`, que valida los límites de
caracteres de Google antes de escribir los archivos.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `estructura.py` | Fuente de verdad. Edita aquí y corre `python3 estructura.py` |
| `campanas-google-ads.csv` | Importar en Google Ads Editor |
| `negativas-cuenta.csv` | 74 negativas para la lista a nivel de cuenta |
| `REVISION.md` | Resumen con conteos y presupuestos (se regenera solo) |

## Antes de gastar el primer peso

Tres cosas tienen que estar listas o el dinero se va sin retorno:

1. **El sitio no está publicado.** Hoy `Index.html` vive solo en el repositorio
   y no hay despliegue en Vercel. Google no aprueba anuncios sin página de
   destino en línea.
2. **Los datos de contacto son de relleno.** El sitio tiene
   `contacto@consultora-le.com`, un teléfono `+34 900 123 456` (España) y
   "Sede Central de Innovación, Ciudad". Con eso Google puede suspender la
   cuenta por tergiversación, y quien llame no encuentra a nadie. Hay que poner
   correo, WhatsApp y dirección reales de Valledupar.
3. **No hay conversiones configuradas.** Sin medir leads, dos de las tres
   campañas usan *Maximize conversions* sobre nada y Google puja a ciegas.

Las URLs de destino del CSV apuntan a páginas por servicio
(`/paneles-solares-valledupar`, `/bombeo-solar`, …) que todavía no existen. Si
arrancas antes de tenerlas, cambia `DOMINIO` y las rutas de `URL` en
`estructura.py` por anclas de la página única (`/#servicios`, `/#contacto`) y
vuelve a generar. Funciona, pero el Nivel de Calidad baja y el CPC sube: una
landing por servicio se paga sola.

## Configuración de la cuenta

**Ubicación.** Valledupar + radio de 60 km, y el departamento del Cesar.
Importante: en *Opciones de ubicación* elegir **"Presencia: personas que están
o visitan con frecuencia"**, nunca la opción de interés. Si no, pagas clics de
Bogotá y México.

**Idioma.** Español.

**Red.** Solo Búsqueda. **Desactivar "Socios de búsqueda" y la Red de Display**
en todas las campañas. Google las deja activas por defecto y ahí se fuga el
presupuesto de las cuentas nuevas.

**Horario.** Lunes a sábado, 6:00 a 20:00. Fuera de ese rango nadie contesta el
WhatsApp y el lead se enfría.

**Dispositivos.** Sin ajuste al inicio. En Valledupar la mayoría busca desde el
celular; revisa a los 30 días y ajusta con datos.

**Plantilla de seguimiento** (Configuración → Seguimiento), para ver todo en
Google Analytics:

```
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={_campana}&utm_term={keyword}&utm_content={creative}
```

## Presupuesto

| Fase | Campaña | COP/día | COP/mes |
|---|---|---:|---:|
| 1 | Solar FV \| Valledupar | 22.000 | 660.000 |
| 1 | Bombeo Solar \| Agro Cesar | 10.000 | 300.000 |
| 1 | Marca | 2.000 | 60.000 |
| | **Total fase 1** | **34.000** | **1.020.000** |
| 2 | Climatización y Nebulización | 8.000 | 240.000 |
| 2 | Auditoría y Ley 1715 | 6.000 | 180.000 |
| | **Total fase 2** | **14.000** | **420.000** |

Las campañas de fase 2 vienen en el CSV como **Paused**. Enciéndelas cuando la
fase 1 lleve al menos 30 conversiones medidas, o cuando arranque la temporada
seca en el caso de nebulización.

**Qué esperar con la fase 1.** Con un CPC promedio estimado de $2.500–$4.000 COP
en este mercado, $1.020.000 COP/mes dan del orden de 250 a 400 clics. Con una
conversión de 4–6% —realista para una landing decente con WhatsApp visible— son
entre 10 y 24 leads al mes. Es una estimación, no una promesa: el número real
depende de la landing y de qué tan rápido contestes.

## Cómo importar

1. Descarga **Google Ads Editor** e inicia sesión en la cuenta.
2. `Cuenta → Importar → Desde archivo` y elige `campanas-google-ads.csv`.
3. Editor muestra la asignación de columnas. **Revísala antes de aceptar**: lo
   que más se desalinea es `Criterion Type` y las 15 columnas de `Headline`.
4. Revisa los cambios propuestos, corrige lo que marque en rojo y haz
   `Publicar`.
5. Carga `negativas-cuenta.csv` en `Herramientas → Listas de palabras clave
   negativas`, crea la lista **"Negativas generales LE"** y aplícala a todas
   las campañas.
6. Agrega las extensiones (van abajo, Editor no las importa en este mismo CSV).

## Extensiones (assets)

Súbelas a nivel de cuenta para que apliquen a todas las campañas.

**Enlaces de sitio** — Paneles Solares · Bombeo Solar · Auditoría Energética ·
Ley 1715 · Climatización · Contáctanos.

**Textos destacados** — Certificados RETIE · Garantía de 25 Años · Visita
Técnica Gratis · Cotización en 24 Horas · Ingeniería Propia · Somos de
Valledupar · Trámite Afinia Incluido · Financiación Disponible.

**Fragmentos estructurados** — *Servicios*: paneles solares, bombeo solar,
auditoría energética, climatización, iluminación LED, aislamiento térmico.

**Llamada** — el celular real de LE SAS, con horario 6:00–20:00.

**Ubicación** — vincular el perfil de Google Business. Si LE SAS todavía no lo
tiene, créalo antes que las campañas: en búsquedas locales el perfil trae leads
gratis y además mejora el rendimiento de los anuncios.

Los textos exactos están en `estructura.py` (`SITELINKS`, `TEXTOS_DESTACADOS`,
`FRAGMENTOS`) y ya están validados contra los límites de caracteres.

## Conversiones a medir

Sin esto, el resto no sirve. Configura en Google Ads → Objetivos → Conversiones:

| Conversión | Cómo se mide | Valor |
|---|---|---|
| Clic en WhatsApp | Evento en el botón flotante | Principal |
| Envío del formulario | Página de gracias o evento | Principal |
| Clic en llamar | Evento en el número | Principal |
| Solicitud de visita técnica | Formulario específico | Principal |
| Descarga de portafolio | Evento | Secundaria |

Marca solo las principales como *Conversión principal*. Las secundarias sirven
para observar, no para que Google optimice sobre ellas.

## Rutina de optimización

**Semana 1 y 2 — todos los días.** Abre el informe de *Términos de búsqueda*.
Todo lo que no tenga que ver con el negocio, agrégalo como negativa. Aquí se
gana o se pierde la cuenta: una cuenta nueva sin limpiar quema el 40% del
presupuesto en búsquedas basura.

**Semanal.** Términos de búsqueda, pausar palabras clave con más de 40 clics y
cero conversiones, revisar que el presupuesto no esté limitado en la campaña
de solar.

**Mensual.** Revisar el Nivel de Calidad —si está por debajo de 6, el problema
casi siempre es la landing, no el anuncio—, rotar los títulos con peor
rendimiento en los RSA, y reasignar presupuesto hacia el grupo que traiga
leads más baratos.

**Trimestral.** Evaluar encender fase 2, y revisar si vale la pena sumar
Riohacha y Santa Marta a la segmentación.

## Nota sobre la voz de los anuncios

Los textos están en español neutro-costeño, directos y sin promesas infladas.
Se cuidan dos cosas: no prometer ahorros garantizados en cifras exactas (Google
lo penaliza y además compromete legalmente), y sostener el ángulo que sí
diferencia a LE SAS frente a los vendedores de paneles de Bogotá — ingeniería
propia, RETIE, y que son de Valledupar y conocen el sol del Cesar.
