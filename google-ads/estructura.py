#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estructura de campañas de Google Search de Consultora de Eficiencia Energética LE SAS.

Esta es la fuente de verdad. Editar aquí y volver a correr:

    python3 estructura.py

Genera:
  - campanas-google-ads.csv      -> importar en Google Ads Editor
  - negativas-cuenta.csv         -> lista de negativas a nivel de cuenta
  - REVISION.md                  -> resumen legible con conteos y avisos

Valida los límites de caracteres de Google antes de escribir nada:
  títulos 30, descripciones 90, rutas 15, textos destacados 25.
"""

import csv
import sys
from collections import Counter

# --------------------------------------------------------------------------
# Ajustes globales
# --------------------------------------------------------------------------

# OJO: el sitio todavía no está publicado. Cuando lo esté, reemplazar aquí.
DOMINIO = "https://www.consultora-le.com"

URL = {
    "solar":        f"{DOMINIO}/paneles-solares-valledupar",
    "empresas":     f"{DOMINIO}/energia-solar-empresas",
    "bombeo":       f"{DOMINIO}/bombeo-solar",
    "nebulizacion": f"{DOMINIO}/nebulizacion-climatizacion",
    "auditoria":    f"{DOMINIO}/auditoria-energetica",
    "ley1715":      f"{DOMINIO}/ley-1715-incentivos",
    "home":         f"{DOMINIO}/",
    "contacto":     f"{DOMINIO}/contacto",
}

# Plantilla de seguimiento a nivel de cuenta (pegar en Configuración > Seguimiento)
PLANTILLA_SEGUIMIENTO = (
    "{lpurl}?utm_source=google&utm_medium=cpc"
    "&utm_campaign={_campana}&utm_term={keyword}&utm_content={creative}"
)

# --------------------------------------------------------------------------
# Campañas
# --------------------------------------------------------------------------
# fase 1 = arrancar ya. fase 2 = encender cuando fase 1 tenga datos.

CAMPANAS = [
    {
        "nombre": "LE | Search | Solar FV | Valledupar",
        "fase": 1,
        "presupuesto_dia_cop": 22000,
        "estrategia": "Maximize conversions",
        "nota": "El motor del negocio. Aquí va el 65% de la inversión.",
        "grupos": [
            {
                "nombre": "Paneles Solares | Residencial",
                "cpc_max_cop": 4500,
                "url": URL["solar"],
                "ruta": ("solar", "valledupar"),
                "keywords": [
                    ("paneles solares valledupar", "Exact"),
                    ("energia solar valledupar", "Exact"),
                    ("instalacion de paneles solares valledupar", "Exact"),
                    ("paneles solares para casa", "Phrase"),
                    ("cuanto cuesta instalar paneles solares", "Phrase"),
                    ("precio de paneles solares en colombia", "Phrase"),
                    ("empresas de paneles solares en valledupar", "Phrase"),
                    ("paneles solares cesar", "Phrase"),
                    ("energia solar para vivienda", "Phrase"),
                ],
                "titulos": [
                    "Paneles Solares Valledupar",
                    "Energía Solar en Valledupar",
                    "Baja tu Factura de Energía",
                    "Instalación Certificada RETIE",
                    "Cotiza Gratis en 24 Horas",
                    "Ahorra Hasta 70% de Energía",
                    "Ingenieros de Valledupar",
                    "Paneles Solares para Casa",
                    "Garantía de 25 Años",
                    "Visita Técnica Sin Costo",
                    "Consultora LE SAS",
                    "Adiós a los Recibos Altos",
                    "Diseño Hecho a tu Medida",
                    "Trámite ante Afinia Incluido",
                    "Financiación Disponible",
                ],
                "descripciones": [
                    "Diseñamos e instalamos tu sistema solar en Valledupar. Ahorro real desde el primer mes.",
                    "Equipos certificados RETIE, ingeniería propia y garantía de 25 años. Cotiza sin costo.",
                    "Nos encargamos del trámite ante Afinia y de los beneficios de la Ley 1715.",
                    "Somos de Valledupar y conocemos el sol del Cesar. Agenda tu visita técnica hoy.",
                ],
            },
            {
                "nombre": "Solar | Empresas e Industria",
                "cpc_max_cop": 6000,
                "url": URL["empresas"],
                "ruta": ("solar", "empresas"),
                "keywords": [
                    ("paneles solares para empresas", "Exact"),
                    ("energia solar para industria", "Exact"),
                    ("sistema solar fotovoltaico industrial", "Phrase"),
                    ("paneles solares comerciales colombia", "Phrase"),
                    ("autogeneracion solar para empresas", "Phrase"),
                    ("proyectos solares llave en mano", "Phrase"),
                    ("energia solar para hoteles", "Phrase"),
                ],
                "titulos": [
                    "Solar para tu Empresa",
                    "Energía Solar Industrial",
                    "Proyectos Llave en Mano",
                    "Baja el Costo de Operación",
                    "Ingeniería y Montaje RETIE",
                    "Estudio de Factibilidad",
                    "Deducción de Renta 50%",
                    "Ley 1715: Menos Impuestos",
                    "Solar para Hoteles y Clínicas",
                    "Consultora LE SAS",
                    "Retorno en 3 a 5 Años",
                    "Trámite AGPE Incluido",
                    "Cotiza tu Proyecto Hoy",
                    "Auditoría Previa Gratuita",
                    "Respaldo con Baterías",
                ],
                "descripciones": [
                    "Reduce el costo energético de tu operación con un sistema solar diseñado a la medida.",
                    "Ingeniería de detalle, RETIE y trámite ante el operador de red. Todo en un solo proveedor.",
                    "Accede a la deducción de renta y la exclusión de IVA de la Ley 1715. Te guiamos.",
                    "Auditoría energética previa sin costo para dimensionar bien tu inversión.",
                ],
            },
            {
                "nombre": "Ahorro | Factura de Energía",
                "cpc_max_cop": 3000,
                "url": URL["solar"],
                "ruta": ("ahorro", "energia"),
                "keywords": [
                    ("ahorrar energia con paneles solares", "Exact"),
                    ("como bajar la factura de energia", "Phrase"),
                    ("reducir el costo de energia de mi empresa", "Phrase"),
                    ("factura de energia muy alta", "Phrase"),
                    ("por que llego tan cara la luz", "Phrase"),
                ],
                "titulos": [
                    "¿Factura de Luz por las Nubes?",
                    "Baja tu Recibo de Energía",
                    "Paga Menos Luz Cada Mes",
                    "La Solución es el Sol",
                    "Ahorra Hasta 70% de Energía",
                    "Calcula tu Ahorro Gratis",
                    "Paneles Solares Valledupar",
                    "Consultora LE SAS",
                    "Sin Cuotas Sorpresa",
                    "Te Explicamos tu Factura",
                    "Diagnóstico Sin Costo",
                    "Ingenieros de Valledupar",
                    "Energía Solar para tu Casa",
                    "Cotización Clara y Simple",
                    "Sin Letra Menuda",
                ],
                "descripciones": [
                    "Si tu factura no baja, el problema no es el clima: es tu consumo. Te lo diagnosticamos.",
                    "Con energía solar tu recibo baja desde el primer mes y el sistema se paga solo.",
                    "Analizamos tu factura gratis y te decimos cuánto puedes ahorrar en tu caso.",
                    "Somos de Valledupar. Visita técnica sin costo y cotización clara en 24 horas.",
                ],
            },
        ],
    },
    {
        "nombre": "LE | Search | Bombeo Solar | Agro Cesar",
        "fase": 1,
        "presupuesto_dia_cop": 10000,
        "estrategia": "Maximize conversions",
        "nota": "Poco volumen pero tickets altos y poca competencia local.",
        "grupos": [
            {
                "nombre": "Bombeo Solar | Pozo Profundo",
                "cpc_max_cop": 5000,
                "url": URL["bombeo"],
                "ruta": ("bombeo", "solar"),
                "keywords": [
                    ("bombeo solar", "Exact"),
                    ("bomba solar para pozo profundo", "Exact"),
                    ("bomba sumergible solar precio", "Phrase"),
                    ("sistema de bombeo solar colombia", "Phrase"),
                    ("bomba de agua con paneles solares", "Phrase"),
                    ("bombeo solar cesar", "Phrase"),
                ],
                "titulos": [
                    "Bombeo Solar para tu Finca",
                    "Agua Sin Pagar Energía",
                    "Bomba Solar Pozo Profundo",
                    "Dimensionamiento Gratuito",
                    "Sin Diésel, Sin Recibo",
                    "Instalación en el Cesar",
                    "Consultora LE SAS",
                    "Equipos con Garantía",
                    "Cotiza en 24 Horas",
                    "Visita a tu Finca",
                    "Ingenieros de Valledupar",
                    "Caudal Calculado a Medida",
                    "Riego, Ganado y Consumo",
                    "Energía Donde No Hay Red",
                    "Olvídate del Combustible",
                ],
                "descripciones": [
                    "Saca agua todo el día sin gastar un peso en diésel ni en energía de la red.",
                    "Calculamos caudal, altura y paneles según tu pozo. Dimensionamiento sin costo.",
                    "Equipos con garantía e instalación en fincas de Cesar y La Guajira.",
                    "Vamos hasta tu finca, medimos y te entregamos la cotización en 24 horas.",
                ],
            },
            {
                "nombre": "Riego Solar | Finca y Ganadería",
                "cpc_max_cop": 4000,
                "url": URL["bombeo"],
                "ruta": ("riego", "solar"),
                "keywords": [
                    ("riego solar finca", "Exact"),
                    ("energia solar para fincas", "Phrase"),
                    ("bombeo solar para ganaderia", "Phrase"),
                    ("sistema de riego con energia solar", "Phrase"),
                    ("energia solar para agro colombia", "Phrase"),
                ],
                "titulos": [
                    "Riego Solar para tu Finca",
                    "Agua para el Ganado",
                    "Energía Solar en el Campo",
                    "Sin Red Eléctrica Cercana",
                    "Bombeo y Riego Solar",
                    "Visita Técnica Sin Costo",
                    "Consultora LE SAS",
                    "Instalación en el Cesar",
                    "Cotiza tu Proyecto Hoy",
                    "Ingenieros de Valledupar",
                    "Bombeo Solar para Agro",
                    "Agua Todo el Día con Sol",
                    "Sin Recibo de Energía",
                    "Proyectos en La Guajira",
                    "Cotiza en 24 Horas",
                ],
                "descripciones": [
                    "Riega y abreva sin depender de la red ni del diésel. Energía solar para tu finca.",
                    "Diseñamos el sistema según tu caudal, tus hectáreas y tu fuente de agua.",
                    "Llevamos energía donde no llega la red. Proyectos en Cesar y La Guajira.",
                    "Visita técnica sin costo y cotización clara, sin letra menuda.",
                ],
            },
        ],
    },
    {
        "nombre": "LE | Search | Marca",
        "fase": 1,
        "presupuesto_dia_cop": 2000,
        "estrategia": "Maximize clicks",
        "nota": "Defensiva y barata. Evita que la competencia puje sobre tu nombre.",
        "grupos": [
            {
                "nombre": "Marca | LE SAS",
                "cpc_max_cop": 1200,
                "url": URL["home"],
                "ruta": ("consultora", "le"),
                "keywords": [
                    ("consultora le sas", "Exact"),
                    ("consultora de eficiencia energetica le", "Exact"),
                    ("consultora le valledupar", "Phrase"),
                    ("consultora le energia", "Phrase"),
                ],
                "titulos": [
                    "Consultora LE SAS | Oficial",
                    "Eficiencia Energética LE",
                    "Sitio Oficial de LE SAS",
                    "Energía Solar Valledupar",
                    "Contáctanos Directamente",
                    "Auditorías y Solar FV",
                    "Ingenieros de Valledupar",
                    "Cotiza Sin Compromiso",
                    "Consultora LE SAS",
                    "Soluciones Energéticas LE",
                    "Bombeo Solar y Auditorías",
                    "Habla con el Ingeniero",
                    "Atención Directa",
                    "Sede en Valledupar, Cesar",
                    "Visita Técnica Sin Costo",
                ],
                "descripciones": [
                    "Sitio oficial de Consultora de Eficiencia Energética LE SAS, Valledupar, Cesar.",
                    "Energía solar, bombeo, climatización y auditorías energéticas. Habla con nosotros.",
                    "Atención directa con el ingeniero, sin intermediarios ni call center.",
                ],
            },
        ],
    },
    {
        "nombre": "LE | Search | Climatización y Nebulización",
        "fase": 2,
        "presupuesto_dia_cop": 8000,
        "estrategia": "Maximize conversions",
        "nota": "Encender en temporada seca / ola de calor. Muy estacional en el Cesar.",
        "grupos": [
            {
                "nombre": "Nebulización | Exteriores",
                "cpc_max_cop": 3500,
                "url": URL["nebulizacion"],
                "ruta": ("nebulizacion", "terrazas"),
                "keywords": [
                    ("sistema de nebulizacion", "Exact"),
                    ("nebulizacion para exteriores", "Exact"),
                    ("nebulizadores para terrazas precio", "Phrase"),
                    ("climatizacion evaporativa colombia", "Phrase"),
                    ("como refrescar una terraza", "Phrase"),
                    ("nebulizacion valledupar", "Phrase"),
                ],
                "titulos": [
                    "Nebulización para Terrazas",
                    "Baja 10°C tu Terraza",
                    "Fresco sin Aire Acondicionado",
                    "Ideal para Bares y Fincas",
                    "Instalación en Valledupar",
                    "Cotiza por Metro Lineal",
                    "Consultora LE SAS",
                    "No Moja, Solo Refresca",
                    "Visita Técnica Sin Costo",
                    "Bajo Consumo de Energía",
                    "Nebulización Valledupar",
                    "Refresca Bares y Kioscos",
                    "Sin Obra, Instalación Ágil",
                    "Menos Calor en tu Negocio",
                    "Ingenieros de Valledupar",
                ],
                "descripciones": [
                    "Sistemas de nebulización que bajan la sensación térmica sin mojar a nadie.",
                    "Perfecto para terrazas, bares, kioscos y zonas de finca. Instalación en Valledupar.",
                    "Consumo bajísimo comparado con aire acondicionado en espacios abiertos.",
                    "Te cotizamos por metro lineal, con visita técnica sin costo.",
                ],
            },
            {
                "nombre": "Climatización | Bodegas e Industria",
                "cpc_max_cop": 4500,
                "url": URL["nebulizacion"],
                "ruta": ("climatizacion", "industrial"),
                "keywords": [
                    ("aire acondicionado industrial", "Exact"),
                    ("enfriamiento para bodegas", "Phrase"),
                    ("ventilacion industrial valledupar", "Phrase"),
                    ("climatizacion para galpones", "Phrase"),
                    ("enfriadores evaporativos industriales", "Phrase"),
                ],
                "titulos": [
                    "Climatización Industrial",
                    "Enfría tu Bodega o Galpón",
                    "Menos Calor, Más Producción",
                    "Ventilación y Evaporativos",
                    "Estudio Térmico Incluido",
                    "Consultora LE SAS",
                    "Instalación en el Cesar",
                    "Cotiza tu Proyecto Hoy",
                    "Ingenieros de Valledupar",
                    "Bajo Costo de Operación",
                    "Enfriamiento Evaporativo",
                    "Baja el Calor de tu Planta",
                    "Ventilación para Bodegas",
                    "Diagnóstico Térmico Gratis",
                    "Solución a la Medida",
                ],
                "descripciones": [
                    "Bajamos la temperatura de bodegas y galpones sin disparar el costo de energía.",
                    "Hacemos el estudio térmico y te proponemos ventilación, evaporativo o mixto.",
                    "El calor le cuesta productividad a tu planta. Lo medimos y lo corregimos.",
                    "Proyectos industriales en Valledupar y todo el Cesar. Visita técnica sin costo.",
                ],
            },
        ],
    },
    {
        "nombre": "LE | Search | Auditoría y Ley 1715",
        "fase": 2,
        "presupuesto_dia_cop": 6000,
        "estrategia": "Maximize conversions",
        "nota": "Bajo volumen, intención altísima. Buen semillero de proyectos grandes.",
        "grupos": [
            {
                "nombre": "Auditoría Energética",
                "cpc_max_cop": 6000,
                "url": URL["auditoria"],
                "ruta": ("auditoria", "energetica"),
                "keywords": [
                    ("auditoria energetica", "Exact"),
                    ("auditoria energetica empresas", "Exact"),
                    ("consultoria en eficiencia energetica", "Phrase"),
                    ("diagnostico energetico industrial", "Phrase"),
                    ("auditoria energetica colombia", "Phrase"),
                ],
                "titulos": [
                    "Auditoría Energética",
                    "Sabe Dónde se Va tu Plata",
                    "Diagnóstico Energético",
                    "Medimos, No Adivinamos",
                    "Informe con Plan de Acción",
                    "Consultora LE SAS",
                    "Para Industria y Comercio",
                    "Ingenieros de Valledupar",
                    "Agenda tu Auditoría",
                    "Ahorro Medible y Real",
                    "Eficiencia Energética",
                    "Baja tu Costo de Energía",
                    "Auditoría en Valledupar",
                    "Antes de Invertir, Mide",
                    "Informe Técnico Completo",
                ],
                "descripciones": [
                    "Medimos tu consumo real y te decimos exactamente dónde se está yendo la energía.",
                    "Entregamos informe con medidas priorizadas por retorno de inversión, no por moda.",
                    "Para industria, hoteles, clínicas y comercio en Valledupar y el Cesar.",
                    "Primero medimos, después proponemos. Así el ahorro es real y comprobable.",
                ],
            },
            {
                "nombre": "Ley 1715 | Incentivos Tributarios",
                "cpc_max_cop": 5000,
                "url": URL["ley1715"],
                "ruta": ("ley-1715", "incentivos"),
                "keywords": [
                    ("ley 1715 beneficios tributarios", "Exact"),
                    ("deduccion de renta energia renovable", "Phrase"),
                    ("incentivos tributarios energia solar colombia", "Phrase"),
                    ("tramite upme energia solar", "Phrase"),
                    ("exclusion de iva paneles solares", "Phrase"),
                ],
                "titulos": [
                    "Ley 1715: Paga Menos Renta",
                    "Incentivos Energía Solar",
                    "Deducción de Renta del 50%",
                    "Exclusión de IVA y Arancel",
                    "Trámite UPME Incluido",
                    "Consultora LE SAS",
                    "Te Armamos el Radicado",
                    "Asesoría Sin Costo",
                    "Ingenieros de Valledupar",
                    "Depreciación Acelerada",
                    "Incentivos Ley 1715",
                    "Beneficios Tributarios",
                    "Mejora el Retorno del Plan",
                    "Energía Solar y Renta",
                    "Radicamos por Ti",
                ],
                "descripciones": [
                    "La Ley 1715 te deja deducir renta, excluir IVA y acelerar depreciación. Te explicamos.",
                    "Armamos y radicamos tu solicitud ante la UPME con la lista de bienes y servicios.",
                    "No dejes los incentivos sobre la mesa: bien usados cambian el retorno del proyecto.",
                    "Primera asesoría sin costo para ver si tu proyecto clasifica.",
                ],
            },
        ],
    },
]

# --------------------------------------------------------------------------
# Negativas de cuenta
# --------------------------------------------------------------------------

NEGATIVAS = {
    "Sin intención de compra": [
        "gratis", "gratuito", "regalado", "como hacer", "como funciona",
        "que es", "casero", "diy", "hazlo tu mismo", "manual",
        "pdf", "tesis", "monografia", "ejemplos", "wikipedia",
    ],
    "Empleo y formación": [
        "empleo", "trabajo", "vacante", "hoja de vida", "curso",
        "cursos", "sena", "capacitacion gratis", "diplomado", "carrera",
        "estudiar", "practicante", "salario",
    ],
    "Retail y usados": [
        "usado", "usados", "segunda mano", "mercadolibre", "mercado libre",
        "homecenter", "alkosto", "exito", "falabella", "amazon",
        "olx", "ebay", "alibaba", "temu", "shein",
    ],
    "Producto equivocado": [
        "para carro", "para camper", "camping", "linterna", "cargador",
        "calculadora", "juguete", "maqueta", "12v pequeño", "power bank",
        "celular", "reloj", "minecraft", "calentador de agua a gas",
    ],
    "Fuera de zona": [
        "españa", "mexico", "peru", "chile", "argentina",
        "ecuador", "estados unidos", "bogota", "medellin",
    ],
    "Competencia y trámites ajenos": [
        "celsia", "enel", "epm", "pagar factura", "pagar recibo",
        "consultar factura", "duplicado de factura", "reclamo afinia",
    ],
}

# --------------------------------------------------------------------------
# Extensiones (assets)
# --------------------------------------------------------------------------

SITELINKS = [
    ("Paneles Solares",   "Diseño e instalación",     "Certificado RETIE",        URL["solar"]),
    ("Bombeo Solar",      "Agua para tu finca",       "Sin diésel ni recibo",     URL["bombeo"]),
    ("Auditoría Energética", "Medimos tu consumo",    "Informe con plan",         URL["auditoria"]),
    ("Ley 1715",          "Menos impuestos",          "Trámite UPME",             URL["ley1715"]),
    ("Climatización",     "Nebulización y evaporativo", "Terrazas y bodegas",     URL["nebulizacion"]),
    ("Contáctanos",       "Visita técnica gratis",    "Respuesta en 24 horas",    URL["contacto"]),
]

TEXTOS_DESTACADOS = [
    "Certificados RETIE",
    "Garantía de 25 Años",
    "Visita Técnica Gratis",
    "Cotización en 24 Horas",
    "Ingeniería Propia",
    "Somos de Valledupar",
    "Trámite Afinia Incluido",
    "Financiación Disponible",
]

FRAGMENTOS = {
    "Servicios": [
        "Paneles solares", "Bombeo solar", "Auditoría energética",
        "Climatización", "Iluminación LED", "Aislamiento térmico",
    ],
    "Tipos": [
        "Residencial", "Comercial", "Industrial", "Agropecuario", "Institucional",
    ],
}

# --------------------------------------------------------------------------
# Validación
# --------------------------------------------------------------------------

LIMITES = {
    "titulo": 30,
    "descripcion": 90,
    "ruta": 15,
    "sitelink_texto": 25,
    "sitelink_desc": 35,
    "destacado": 25,
    "fragmento": 25,
}

errores = []
avisos = []


def revisar(texto, tipo, donde):
    """Verifica un texto contra su límite. Google cuenta caracteres, no bytes."""
    limite = LIMITES[tipo]
    n = len(texto)
    if n > limite:
        errores.append(f"{donde}: {tipo} de {n} caracteres (máx {limite}) -> {texto!r}")
    return n


def validar():
    for c in CAMPANAS:
        for g in c["grupos"]:
            donde = f"{c['nombre']} / {g['nombre']}"

            if len(g["titulos"]) < 3:
                errores.append(f"{donde}: necesita mínimo 3 títulos")
            if len(g["titulos"]) < 15:
                avisos.append(
                    f"{donde}: {len(g['titulos'])} títulos. "
                    "Google premia llegar a 15."
                )
            if len(g["descripciones"]) < 2:
                errores.append(f"{donde}: necesita mínimo 2 descripciones")

            for t in g["titulos"]:
                revisar(t, "titulo", donde)
            for d in g["descripciones"]:
                revisar(d, "descripcion", donde)
            for p in g["ruta"]:
                revisar(p, "ruta", donde)

            repes = [k for k, v in Counter(g["titulos"]).items() if v > 1]
            if repes:
                errores.append(f"{donde}: títulos repetidos -> {repes}")

            if not g["keywords"]:
                errores.append(f"{donde}: sin palabras clave")

    for texto, d1, d2, _ in SITELINKS:
        revisar(texto, "sitelink_texto", "Sitelink")
        revisar(d1, "sitelink_desc", f"Sitelink {texto}")
        revisar(d2, "sitelink_desc", f"Sitelink {texto}")

    for t in TEXTOS_DESTACADOS:
        revisar(t, "destacado", "Texto destacado")

    for encabezado, valores in FRAGMENTOS.items():
        for v in valores:
            revisar(v, "fragmento", f"Fragmento {encabezado}")


# --------------------------------------------------------------------------
# Generación del CSV para Google Ads Editor
# --------------------------------------------------------------------------

COLUMNAS = (
    ["Campaign", "Campaign Type", "Campaign Daily Budget", "Bid Strategy Type",
     "Campaign Status", "Ad Group", "Max CPC", "Ad Group Status",
     "Keyword", "Criterion Type", "Ad Type"]
    + [f"Headline {i}" for i in range(1, 16)]
    + [f"Description {i}" for i in range(1, 5)]
    + ["Path 1", "Path 2", "Final URL", "Status"]
)


def fila_vacia():
    return {col: "" for col in COLUMNAS}


def generar_csv(ruta_salida, solo_fase=None):
    filas = []
    for c in CAMPANAS:
        if solo_fase and c["fase"] != solo_fase:
            continue
        estado_campana = "Enabled" if c["fase"] == 1 else "Paused"

        f = fila_vacia()
        f.update({
            "Campaign": c["nombre"],
            "Campaign Type": "Search",
            "Campaign Daily Budget": c["presupuesto_dia_cop"],
            "Bid Strategy Type": c["estrategia"],
            "Campaign Status": estado_campana,
        })
        filas.append(f)

        for g in c["grupos"]:
            f = fila_vacia()
            f.update({
                "Campaign": c["nombre"],
                "Ad Group": g["nombre"],
                "Max CPC": g["cpc_max_cop"],
                "Ad Group Status": "Enabled",
            })
            filas.append(f)

            for kw, tipo in g["keywords"]:
                f = fila_vacia()
                f.update({
                    "Campaign": c["nombre"],
                    "Ad Group": g["nombre"],
                    "Keyword": kw,
                    "Criterion Type": tipo,
                    "Status": "Enabled",
                })
                filas.append(f)

            f = fila_vacia()
            f.update({
                "Campaign": c["nombre"],
                "Ad Group": g["nombre"],
                "Ad Type": "Responsive search ad",
                "Path 1": g["ruta"][0],
                "Path 2": g["ruta"][1],
                "Final URL": g["url"],
                "Status": "Enabled",
            })
            for i, t in enumerate(g["titulos"][:15], start=1):
                f[f"Headline {i}"] = t
            for i, d in enumerate(g["descripciones"][:4], start=1):
                f[f"Description {i}"] = d
            filas.append(f)

    # utf-8-sig: Google Ads Editor y Excel leen bien las tildes con BOM.
    with open(ruta_salida, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNAS)
        w.writeheader()
        w.writerows(filas)
    return len(filas)


def generar_negativas(ruta_salida):
    with open(ruta_salida, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["Keyword", "Criterion Type", "Grupo"])
        for grupo, palabras in NEGATIVAS.items():
            for p in palabras:
                w.writerow([p, "Broad", grupo])
    return sum(len(v) for v in NEGATIVAS.values())


def generar_revision(ruta_salida, filas, n_negativas):
    lineas = ["# Revisión de la estructura", ""]

    total_kw = 0
    total_anuncios = 0
    presupuesto_f1 = 0
    presupuesto_f2 = 0

    for c in CAMPANAS:
        kws = sum(len(g["keywords"]) for g in c["grupos"])
        total_kw += kws
        total_anuncios += len(c["grupos"])
        if c["fase"] == 1:
            presupuesto_f1 += c["presupuesto_dia_cop"]
        else:
            presupuesto_f2 += c["presupuesto_dia_cop"]

        lineas.append(f"## {c['nombre']}")
        lineas.append("")
        lineas.append(f"- Fase: {c['fase']}")
        lineas.append(f"- Presupuesto: ${c['presupuesto_dia_cop']:,.0f} COP/día "
                      f"(~${c['presupuesto_dia_cop'] * 30:,.0f} COP/mes)")
        lineas.append(f"- Estrategia de puja: {c['estrategia']}")
        lineas.append(f"- Grupos: {len(c['grupos'])} | Palabras clave: {kws}")
        lineas.append(f"- Nota: {c['nota']}")
        lineas.append("")
        for g in c["grupos"]:
            lineas.append(f"  - **{g['nombre']}** — {len(g['keywords'])} kw, "
                          f"{len(g['titulos'])} títulos, "
                          f"{len(g['descripciones'])} descripciones, "
                          f"CPC máx ${g['cpc_max_cop']:,.0f} COP")
        lineas.append("")

    lineas += [
        "## Totales",
        "",
        f"- Campañas: {len(CAMPANAS)}",
        f"- Grupos de anuncios: {total_anuncios}",
        f"- Palabras clave: {total_kw}",
        f"- Negativas de cuenta: {n_negativas}",
        f"- Filas en el CSV: {filas}",
        "",
        f"- Presupuesto fase 1: ${presupuesto_f1:,.0f} COP/día "
        f"(~${presupuesto_f1 * 30:,.0f} COP/mes)",
        f"- Presupuesto fase 2: ${presupuesto_f2:,.0f} COP/día "
        f"(~${presupuesto_f2 * 30:,.0f} COP/mes)",
        "",
    ]

    if avisos:
        lineas.append("## Avisos")
        lineas.append("")
        lineas += [f"- {a}" for a in avisos]
        lineas.append("")

    lineas += [
        "## Validación de límites",
        "",
        "Sin errores de longitud: todos los títulos caben en 30 caracteres, "
        "las descripciones en 90 y las rutas en 15.",
        "",
    ]

    with open(ruta_salida, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas))


def main():
    validar()

    if errores:
        print("ERRORES:\n")
        for e in errores:
            print("  -", e)
        return 1

    filas = generar_csv("campanas-google-ads.csv")
    n_neg = generar_negativas("negativas-cuenta.csv")
    generar_revision("REVISION.md", filas, n_neg)

    print(f"OK  campanas-google-ads.csv  ({filas} filas)")
    print(f"OK  negativas-cuenta.csv     ({n_neg} negativas)")
    print("OK  REVISION.md")

    if avisos:
        print(f"\n{len(avisos)} aviso(s):")
        for a in avisos:
            print("  -", a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
