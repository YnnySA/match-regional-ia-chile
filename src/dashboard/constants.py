"""Shared dashboard constants and visual tokens."""

from __future__ import annotations

APP_TITLE = "Match-IA Regional: Análisis Territorial de Oferta Formativa en IA (Chile)"
APP_SUBTITLE = (
    "Oferta, especialización y acceso a formación afín a IA en el sistema "
    "de educación superior."
)
DATA_CUTOFF = "MINEDUC 2025"
FONT_STACK = '"Consolas", "Cascadia Mono", "Courier New", monospace'

COLORS = {
    "background": "#0e1728",
    "surface": "#1d2b40",
    "surface_alt": "#17243a",
    "panel": "#111b2f",
    "border": "#30425c",
    "text": "#e7edf5",
    "muted": "#91a0b5",
    "accent": "#2aa9e8",
    "accent_soft": "#174d68",
    "warning": "#d98a3a",
    "success": "#55b6a4",
    "reference": "#65728a",
}

REGIONS = (
    (1, "Arica y Parinacota"),
    (2, "Tarapacá"),
    (3, "Antofagasta"),
    (4, "Atacama"),
    (5, "Coquimbo"),
    (6, "Valparaíso"),
    (7, "Metropolitana de Santiago"),
    (8, "Libertador General Bernardo O'Higgins"),
    (9, "Maule"),
    (10, "Ñuble"),
    (11, "Biobío"),
    (12, "La Araucanía"),
    (13, "Los Ríos"),
    (14, "Los Lagos"),
    (15, "Aysén del General Carlos Ibáñez del Campo"),
    (16, "Magallanes y de la Antártica Chilena"),
)
REGION_BY_ORDER = dict(REGIONS)
MVP_REGION_ORDERS = (6, 7, 11)

NAV_ITEMS = (
    "Visión General",
    "Oferta y Titulados",
    "Especialización (LQ)",
    "Infraestructura Geo",
)
