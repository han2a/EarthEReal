
import os

# NASA data configuration
MAX_GRANULES = 1500
MAX_PRODUCTS = 3
MAX_WORKERS = 4
HTTP_TIMEOUT = 120

CMR_URL = "https://cmr.earthdata.nasa.gov/search"

GIOVANNI_TIMESERIES_URL = (
    "https://api.giovanni.earthdata.nasa.gov/timeseries"
)

SCIENCE_TOPICS = ("ATMOSPHERE", "OCEANS")

TRUSTED_AUTH_SUFFIXES = (
    ".nasa.gov",
    ".nsidc.org",
)

# Gemini configuration
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "{model}:generateContent"
)

def providers():
    raw = os.environ.get("CMR_PROVIDERS", "GES_DISC")
    return [
        p.strip()
        for p in raw.split(",")
        if p.strip()
    ]


def gemini_model():
    return os.environ.get(
        "GEMINI_MODEL",
        "gemini-4-hydrogen"
    )


import os
def env(name, default=None):
    v = os.getenv(name)
    if v:
        return v
    try:
        import streamlit as st
        return st.secrets.get(name, default)
    except Exception:
        return default
