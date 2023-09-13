import pandas as pd
import re

#ENTENDER PQ FUNCIONAN LAS REJEX(TODAS)

# Expresiones regulares
MAC_AP_RE = re.compile(r"([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$")#OK
MAC_CLIENT_RE = re.compile(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")#OK
IP_NAS_RE = re.compile(r"((?:192\.168\.247\.[0-9]{2})|(?:192\.168\.1\.20))$")#OK
ID_RE = re.compile(r"\d{6,7}$")#OK
ID_SESION_RE = re.compile(r"[A-F0-9]{8}-[A-F0-9]{8}$")#OK
ID_CONEXION_UNICO_RE = re.compile(r"[a-f0-9]{16}$")#OK
USER_RE = re.compile(r"[a-zA-Z.-]{3,25}$")#OK
DATE_RE = re.compile(r"(20(1[5-9]|2[0-5])[-/](0[1-9]|1[0-2])[-/]([0-2]\d|3[0-1])$)")#OK
HOUR_RE = re.compile(r"([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$")#OK


#Crea un dataframe de pandas con los datos del csv
def create_pandas(csv_path: str) -> pd.DataFrame:
    data = pd.read_csv(csv_path, low_memory=False)
    return data

#Aplica todos los filtros
def apply_regex(data: pd.DataFrame) -> pd.DataFrame:
    filtro = (
        data["MAC_AP"].apply(lambda x: bool(re.fullmatch(MAC_AP_RE, str(x))))
        & data["MAC_Cliente"].apply(lambda x: bool(re.fullmatch(MAC_CLIENT_RE, str(x))))
        & data["IP_NAS_AP"].apply(lambda x: bool(re.fullmatch(IP_NAS_RE, str(x))))
        & data["ID"].apply(lambda x: bool(re.fullmatch(ID_RE, str(x))))
        & data["ID_Sesion"].apply(lambda x: bool(re.fullmatch(ID_SESION_RE, str(x))))
        & data["ID_Conexión_unico"].apply(lambda x: bool(re.fullmatch(ID_CONEXION_UNICO_RE, str(x))))
        & data["Inicio_de_Conexión_Dia"].apply(lambda x: bool(re.fullmatch(DATE_RE, str(x))))
        & data["FIN_de_Conexión_Dia"].apply(lambda x: bool(re.fullmatch(DATE_RE, str(x))))
        & data["Inicio_de_Conexión_Hora"].apply(lambda x: bool(re.fullmatch(HOUR_RE, str(x))))
        & data["FIN_de_Conexión_Hora"].apply(lambda x: bool(re.fullmatch(HOUR_RE, str(x))))
        & data["Usuario"].apply(lambda x: bool(re.fullmatch(USER_RE, str(x))))
    )
    data = data[filtro]
    return data