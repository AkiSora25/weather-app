"""Configurazione dell'applicazione Weather App

Carica variabili d'ambiente da file .env per gestire
impostazioni diverse per development, testing e production.
"""

import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()


class Config:
    """Configurazione base dell'applicazione"""
    
    # Flask
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Server
    SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
    SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))
    
    # Cache
    CACHE_TTL = int(os.getenv('CACHE_TTL', 3600))  # 1 ora di default
    
    # API
    OPENMETEO_API_KEY = os.getenv('OPENMETEO_API_KEY', '')
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '')
    
    # Database (per futuri sviluppi)
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///weather.db')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


class DevelopmentConfig(Config):
    """Configurazione per Development"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configurazione per Production"""
    DEBUG = False
    TESTING = False
    
    # In produzione, la SECRET_KEY DEVE essere configurata
    if not os.getenv('FLASK_SECRET_KEY'):
        raise ValueError(
            "ERRORE: FLASK_SECRET_KEY deve essere configurata in produzione!"
        )


class TestingConfig(Config):
    """Configurazione per Testing"""
    DEBUG = True
    TESTING = True
    CACHE_TTL = 60  # Cache più corta per i test


# Seleziona la configurazione giusta
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config(config_name=None):
    """Ritorna la configurazione appropriata"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    return config.get(config_name, config['default'])
