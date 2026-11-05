from pathlib import Path
import os

# Projektwurzel: Ordner, in dem diese Datei liegt
PROJECT_ROOT = Path(__file__).resolve().parent


# Hauptordner
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
HTML_DIR = OUTPUT_DIR / "html"
PDF_DIR = OUTPUT_DIR / "pdf"
TEX_DIR = OUTPUT_DIR / "tex"
FIGURES_DIR = PROJECT_ROOT / "figures"


# Eingabedatei
ORIGINAL_DS_ZIP_PATH = DATA_DIR / "DBtrainrides.csv.zip"

# Datensatz bereinigt als parquet Datei
CLEANED_DS_PARQUET_PATH = DATA_DIR / "DBtrainrides_cleaned.parquet"

# Temporärer Ordner für Rohdaten (wird bei Abgabe nicht übergeben)
TMP_DIR = PROJECT_ROOT / "tmp"
XML_CACHE_DIR = DATA_DIR / "xml_cache"
# für APIs
ENV_FILE_PATH = PROJECT_ROOT / ".env"
ENV_EXAMPLE_PATH = PROJECT_ROOT / ".env.example"

# Entpackte beziehungsweise erzeugte Datensätze
ORIGINAL_DS_BZ2_PATH = DATA_DIR / "DBtrainrides.bz2"
ORIGINAL_DS_PARQUET_PATH = DATA_DIR / "DBtrainrides.parquet"
ORIGINAL_DS_CSV_PATH = DATA_DIR / "DBtrainrides.csv"

SPECIAL_DS_CSV_PATH = DATA_DIR / "DBtrainrides_special.csv"


# Dokumente
PANDAS_ANALYSIS_HTML = HTML_DIR / "01_Dateiformate_Pandas.html"
PANDAS_ANALYSIS_PDF = PDF_DIR / "01_Dateiformate_Pandas.pdf"

FRAMEWORK_ANALYSIS_HTML = HTML_DIR / "02_Framework_Vergleich.html"
FRAMEWORK_ANALYSIS_PDF = PDF_DIR / "02_Framework_Vergleich.pdf"

# Dokumente für Phase 2B (Erweiterte PySpark-Analyse)
PYSPARK_ANALYSIS_HTML = HTML_DIR / "03_Advanced_PySpark_Analytics.html"
PYSPARK_ANALYSIS_PDF = PDF_DIR / "03_Advanced_PySpark_Analytics.pdf"

STADA_API_HTML = HTML_DIR / "04_StaDa_API_Validation.html"
STADA_API_PDF = PDF_DIR / "04_StaDa_API_Validation.pdf"

TIMETABLE_API_HTML = HTML_DIR / "05_TimeTable_API_Validation.html"
TIMETABLE_API_PDF = PDF_DIR / "05_TimeTable_API_Validation.pdf"

MAIN_PROJECT_HTML = PROJECT_ROOT / "Projekt_Deutsche_Bahn.html"
MAIN_PROJECT_PDF = PROJECT_ROOT / "Projekt_Deutsche_Bahn.pdf"

# Outputs
DATEIFORMATE_RESULTS = OUTPUT_DIR / "01_results.parquet"
FRAMEWORK_RESULTS = OUTPUT_DIR / "02_results.parquet"

# Outputs für Phase 2B
PYSPARK_RESULTS = OUTPUT_DIR / "03_results.parquet"
# für Phase 3
STADA_API_RESULTS = OUTPUT_DIR / "04_results.parquet"

# für Phase 4 (optional)
TIMETABLE_API_RESULTS = OUTPUT_DIR / "05_results.parquet"

# Ordner automatisch anlegen
for folder in [
    DATA_DIR,
    OUTPUT_DIR,
    HTML_DIR,
    PDF_DIR,
    TEX_DIR,
    FIGURES_DIR,
    TMP_DIR,
    XML_CACHE_DIR
]:
    folder.mkdir(parents=True, exist_ok=True)

def get_project_relative_path(path):
    """
    Wandelt einen absoluten Projektpfad in einen relativen,
    POSIX-kompatiblen String um.
    """
    absolute_path = Path(path).resolve()
    project_root = PROJECT_ROOT.resolve()

    relative_path = absolute_path.relative_to(project_root)

    return relative_path.as_posix()

# Dash
DASH_HOST = "127.0.0.1"

DASH_PORT_DATAFORMAT = 8060
DASH_URL_DATAFORMAT = (
    f"http://{DASH_HOST}:{DASH_PORT_DATAFORMAT}"
)

DASH_PORT_FRAMEWORK = 8061
DASH_URL_FRAMEWORK = (
    f"http://{DASH_HOST}:{DASH_PORT_FRAMEWORK}"
)

DASH_PORT_PHASE2 = 8062
DASH_URL_PHASE2 = (
    f"http://{DASH_HOST}:{DASH_PORT_PHASE2}"
)

DASH_PORT_PHASE3 = 8063
DASH_URL_PHASE3 = (
    f"http://{DASH_HOST}:{DASH_PORT_PHASE3}"
)

DASH_PORT_PHASE4 = 8064
DASH_URL_PHASE4 = (
    f"http://{DASH_HOST}:{DASH_PORT_PHASE4}"
)