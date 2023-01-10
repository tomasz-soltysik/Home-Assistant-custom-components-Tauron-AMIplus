"""Constants for tauron."""
from datetime import timedelta

DOMAIN = "tauron_amiplus"
DEFAULT_NAME = "Tauron AMIplus"
DATA_TAURON_CLIENT = "data_client"
CONF_METER_ID = "energy_meter_id"
CONF_GENERATION = "check_generation"
CONF_TARIFF = "tariff"
CONF_SHOW_GENERATION = "show_generation_sensors"
CONF_URL_SERVICE = "https://elicznik.tauron-dystrybucja.pl"
CONF_URL_LOGIN = "https://logowanie.tauron-dystrybucja.pl/login"
CONF_URL_ENERGY = "https://elicznik.tauron-dystrybucja.pl/energia/api"
CONF_URL_READINGS = "https://elicznik.tauron-dystrybucja.pl/odczyty/api"
CONF_REQUEST_HEADERS = {"cache-control": "no-cache"}
CONF_REQUEST_PAYLOAD_CHARTS = {"dane[cache]": 0}
TYPE_CURRENT_READINGS = "current_readings"
TYPE_CONSUMPTION_DAILY = "consumption_daily"
TYPE_CONSUMPTION_MONTHLY = "consumption_monthly"
TYPE_CONSUMPTION_YEARLY = "consumption_yearly"
TYPE_GENERATION_DAILY = "generation_daily"
TYPE_GENERATION_MONTHLY = "generation_monthly"
TYPE_GENERATION_YEARLY = "generation_yearly"

DEFAULT_UPDATE_INTERVAL = timedelta(hours=12)
SENSOR_TYPES = {
    TYPE_CURRENT_READINGS: [
        "Current meter readings",
    ],
    TYPE_CONSUMPTION_DAILY: [
        "Daily energy consumption",
    ],
    TYPE_CONSUMPTION_MONTHLY: [
        "Monthly energy consumption",
    ],
    TYPE_CONSUMPTION_YEARLY: [
        "Yearly energy consumption",
    ],
    TYPE_GENERATION_DAILY: [
        "Daily energy generation",
    ],
    TYPE_GENERATION_MONTHLY: [
        "Monthly energy generation",
    ],
    TYPE_GENERATION_YEARLY: [
        "Yearly energy generation",
    ],
}
