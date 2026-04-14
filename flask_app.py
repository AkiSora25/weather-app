"""Applicazione Flask per la Weather App Web"""
from flask import Flask, render_template, request, jsonify
from config import get_config
from app.services.weather_api import (
    get_coordinates, 
    get_cached_weather_for_cities,
    get_cached_weather,
    weather_cache
)
import logging

# Carica la configurazione
app = Flask(__name__)
config = get_config()
app.config.from_object(config)

# Configurazione logging
logging.basicConfig(
    level=app.config.get('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    """Pagina principale della web app"""
    return render_template('index.html')


@app.route('/api/weather', methods=['POST'])
def get_weather_endpoint():
    """Endpoint API per ottenere il meteo di una città"""
    try:
        data = request.json
        city = data.get('city', '').strip()
        use_cache = data.get('use_cache', True)
        
        if not city:
            return jsonify({'error': 'Nome città richiesto'}), 400
        
        # Ottieni le coordinate
        coords = get_coordinates(city)
        if coords is None:
            return jsonify({'error': f'Città "{city}" non trovata'}), 404
        
        lat, lon = coords
        
        # Ottieni il meteo con cache
        temperature = get_cached_weather(lat, lon, use_cache=use_cache)
        
        if temperature is None:
            return jsonify({'error': 'Impossibile recuperare i dati meteo'}), 500
        
        return jsonify({
            'city': city,
            'latitude': lat,
            'longitude': lon,
            'temperature': temperature,
            'unit': 'C'
        }), 200
    
    except Exception as e:
        logger.error(f"Errore nella richiesta API: {str(e)}")
        return jsonify({'error': 'Errore interno del server'}), 500


@app.route('/api/weather/multiple', methods=['POST'])
def get_multiple_weather():
    """Endpoint API per ottenere il meteo di multiple città"""
    try:
        data = request.json
        cities = data.get('cities', [])
        use_cache = data.get('use_cache', True)
        
        if not cities or not isinstance(cities, list):
            return jsonify({'error': 'Array di città richiesto'}), 400
        
        if len(cities) > 10:
            return jsonify({'error': 'Massimo 10 città per richiesta'}), 400
        
        results = get_cached_weather_for_cities(cities, use_cache=use_cache)
        
        # Formatta i risultati
        formatted_results = []
        for city, temp in results.items():
            formatted_results.append({
                'city': city,
                'temperature': temp,
                'unit': 'C' if temp is not None else None,
                'success': temp is not None
            })
        
        return jsonify({'results': formatted_results}), 200
    
    except Exception as e:
        logger.error(f"Errore nella richiesta API multiple: {str(e)}")
        return jsonify({'error': 'Errore interno del server'}), 500


@app.route('/api/cache/status', methods=['GET'])
def get_cache_status():
    """Endpoint API per ottenere lo stato della cache"""
    try:
        cache_info = {
            'size': len(weather_cache.cache),
            'ttl': weather_cache.ttl,
            'entries': []
        }
        
        # Lista le voci in cache
        for key, (value, timestamp) in weather_cache.cache.items():
            remaining = weather_cache.get_remaining_ttl(key)
            cache_info['entries'].append({
                'key': key,
                'value': value,
                'remaining_ttl': remaining
            })
        
        return jsonify(cache_info), 200
    
    except Exception as e:
        logger.error(f"Errore nel recuperare lo stato della cache: {str(e)}")
        return jsonify({'error': 'Errore interno del server'}), 500


@app.route('/api/cache/clear', methods=['POST'])
def clear_cache():
    """Endpoint API per pulire la cache"""
    try:
        weather_cache.clear()
        return jsonify({'message': 'Cache pulita con successo'}), 200
    except Exception as e:
        logger.error(f"Errore nel pulire la cache: {str(e)}")
        return jsonify({'error': 'Errore interno del server'}), 500


@app.errorhandler(404)
def not_found(error):
    """Gestore errore 404"""
    return jsonify({'error': 'Pagina non trovata'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Gestore errore 500"""
    return jsonify({'error': 'Errore interno del server'}), 500


if __name__ == '__main__':
    # Usa la configurazione per avviare il server
    host = app.config.get('SERVER_HOST', '0.0.0.0')
    port = app.config.get('SERVER_PORT', 5000)
    debug = app.config.get('DEBUG', False)
    
    logger.info(f"Avvio Weather App su http://{host}:{port}")
    logger.info(f"Ambiente: {app.config.get('FLASK_ENV', 'development')}")
    logger.info(f"Debug: {debug}")
    
    app.run(debug=debug, host=host, port=port)
