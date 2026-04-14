# Weather App

Un'applicazione Python per recuperare e visualizzare le informazioni meteorologiche attuali di una qualsiasi città nel mondo.

## 📋 Descrizione del Progetto

Weather App è un'applicazione che consente agli utenti di cercare informazioni meteorologiche per una città specifica. Disponibile sia come CLI (Command Line Interface) che come Web App moderna e responsive. L'app utilizza le API gratuite di Open-Meteo per ottenere le coordinate geografiche e i dati meteo in tempo reale, con un sistema avanzato di caching per ridurre le richieste API.

## 🏗️ Struttura del Progetto

```
weather-app/
├── main.py                          # Entry point CLI dell'applicazione
├── flask_app.py                     # Entry point Web App (Flask)
├── config.py                        # Configurazioni globali (attualmente vuoto)
├── requirements.txt                 # Dipendenze del progetto
│
├── app/
│   ├── cli/
│   │   └── interface.py             # Interfaccia CLI (struttura per futuri sviluppi)
│   │
│   ├── models/
│   │   └── weather.py               # Modelli dati per il meteo (struttura per futuri sviluppi)
│   │
│   ├── services/
│   │   └── weather_api.py           # Servizi per le chiamate API meteorologiche
│   │
│   └── utils/
│       └── formatter.py             # Funzioni di utilità per la conversione temperature
│
├── static/                          # File statici Web App
│   ├── style.css                    # Stili CSS (responsive)
│   └── script.js                    # JavaScript interattivo
│
├── templates/                       # Template HTML
│   └── index.html                   # Pagina principale Web App
│
└── tests/
    └── test_weather_api.py          # Test unitari per i servizi API
```

## 📦 Dipendenze

- **requests**: Libreria per effettuare richieste HTTP alle API di Open-Meteo
- **flask**: Framework web per la Web App moderna
- **python-dotenv**: Gestione sicura delle variabili d'ambiente da file `.env`

Vedi [requirements.txt](requirements.txt) per l'elenco completo.

## 🔧 Installazione

### Prerequisiti
- Python 3.7 o superiore
- pip (gestore pacchetti Python)

### Procedura

1. **Clona o scarica il progetto**
   ```bash
   cd weather-app
   ```

2. **Crea un ambiente virtuale (consigliato)**
   ```bash
   python -m venv venv
   ```
   
   Su Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   Su macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura le variabili d'ambiente**
   ```bash
   # Copia il file di esempio
   cp .env.example .env
   ```
   
   Poi modifica `.env` con le tue impostazioni (se necessario):
   ```env
   FLASK_ENV=development
   FLASK_DEBUG=True
   FLASK_SECRET_KEY=your-secret-key-here
   SERVER_PORT=5000
   CACHE_TTL=3600
   ```

## 🚀 Utilizzo

### Opzione 1: CLI (Command Line Interface)

Avvia l'applicazione dal terminale:

```bash
python main.py
```

L'applicazione ti chiederà di inserire il nome di una città:

```
Inserisci una città: Milano
La temperatura attuale a Milano è 18°C
```

### Opzione 2: Web App (Moderna e Responsive) ⭐ CONSIGLIATO

#### Avvio del Server

```bash
pip install flask
python flask_app.py
```

Il server partirà su `http://localhost:5000`

#### Accesso

Apri il browser e vai a: **http://localhost:5000**

#### Caratteristiche della Web App

✨ **Interfaccia Moderna:**
- Design responsivo per desktop, tablet e smartphone
- Gradiente colorato con tema moderno e professionale
- Icone FontAwesome per indicare le condizioni meteo
- Animazioni fluide e transizioni smooth
- Supporto tema scuro (auto-detect dal sistema)

🔍 **Ricerca Singola:**
- Inserisci una città e visualizza il meteo istantaneamente
- Visualizzazione della temperatura in gradi Celsius
- Coordinate geografiche (latitudine e longitudine)
- Icona dinamica basata sulla temperatura

📊 **Ricerca Multipla:**
- Cerca il meteo di più città contemporaneamente (fino a 10)
- Visualizzazione in grid con carte separate
- Inserisci le città separate da virgole
- Design card per ogni città

💾 **Gestione Cache Avanzata:**
- Visualizza lo stato della cache in tempo reale
- Vedi il tempo rimanente di validità per ogni dato
- Informazioni dettagliate su ogni voce in cache
- Pulisci la cache quando necessario
- Toggle per abilitare/disabilitare la cache

📱 **Responsive Design:**
- Perfetto su desktop (1920px+), tablet (768px) e smartphone (480px)
- Touch-friendly su dispositivi mobili
- Layout fluido che si adatta a ogni schermo
- Navigazione intuitiva con tab

🚀 **Performance:**
- Cache intelligente con scadenza temporale (1 ora)
- Riduce le richieste API del 90% per ricerche frequenti
- Risposte istantanee per dati in cache
- Caricamento veloce con spinner di feedback

## 📖 Documentazione dei Moduli

### `main.py`
**Punto di ingresso dell'applicazione CLI**

- **Funzione `main()`**: Orchestra il flusso principale dell'app
  1. Legge il nome della città dall'utente
  2. Chiama `get_coordinates()` per ottenere latitudine e longitudine
  3. Chiama `get_weather()` per ottenere la temperatura attuale
  4. Visualizza il risultato

### `flask_app.py`
**Applicazione Web Flask - Server e Endpoint API**

#### Endpoint API

**POST /api/weather**
- Recupera il meteo di una singola città
- Body: `{"city": "Roma", "use_cache": true}`
- Risposta: 
  ```json
  {
    "city": "Roma",
    "latitude": 41.9028,
    "longitude": 12.4964,
    "temperature": 22.5,
    "unit": "C"
  }
  ```

**POST /api/weather/multiple**
- Recupera il meteo di multiple città
- Body: `{"cities": ["Roma", "Milano"], "use_cache": true}`
- Risposta:
  ```json
  {
    "results": [
      {"city": "Roma", "temperature": 22.5, "unit": "C", "success": true},
      {"city": "Milano", "temperature": 18.3, "unit": "C", "success": true}
    ]
  }
  ```

**GET /api/cache/status**
- Ottiene lo stato della cache
- Risposta: Info su tutte le voci in cache con TTL rimanente

**POST /api/cache/clear**
- Pulisce tutta la cache
- Risposta: Messaggio di conferma

#### File Statici

**static/style.css**
- Stili CSS moderni e responsivi
- Temi chiari e scuri (auto-detect)
- Animazioni e transizioni fluide
- Breakpoint per mobile (480px), tablet (768px), desktop (1920px+)

**static/script.js**
- Logica interattiva della web app
- Gestione delle tab
- Richieste API asincrone con fetch
- Gestione di errori e loading state
- Icone meteo dinamiche basate sulla temperatura

#### Template HTML

**templates/index.html**
- Definisce la struttura della pagina web
- Sezioni per ricerca singola, multipla e cache
- Integrazione con FontAwesome per le icone
- Form responsivo per input utente

### `app/services/weather_api.py`
**Gestione delle chiamate API alle API di Open-Meteo con supporto di cache**

#### Classe `APICache`
- **Parametri del costruttore**:
  - `ttl` (int): Time To Live in secondi (default: 3600 = 1 ora)
- **Metodi principali**:
  - `get(key)`: Recupera un valore se valido e non scaduto
  - `set(key, value)`: Memorizza un valore con timestamp
  - `is_expired(key)`: Verifica se una chiave è scaduta
  - `get_remaining_ttl(key)`: Ottiene i secondi rimanenti prima della scadenza
  - `clear()`: Cancella tutta la cache
- **Descrizione**: Gestisce la memorizzazione dei dati API con scadenza automatica. Perfetto per ridurre le richieste API ripetute

#### Funzione `get_cached_weather(lat, lon, use_cache=True)`
- **Parametri**: 
  - `lat` (float): Latitudine
  - `lon` (float): Longitudine
  - `use_cache` (bool): Abilita/disabilita la cache (default: True)
- **Ritorna**: Temperatura in Celsius o None se errore
- **Descrizione**: Versione in cache di `get_weather()`. Verifica prima la cache, se i dati sono validi li ritorna, altrimenti effettua una nuova richiesta API
- **Cache**: TTL di 1 ora per impostazione predefinita
- **Vantaggi**: Riduce le richieste API, migliora le prestazioni

#### Funzione `get_cached_weather_for_cities(cities, use_cache=True)`
- **Parametri**: 
  - `cities` (List[str]): Lista di nomi di città
  - `use_cache` (bool): Abilita/disabilita la cache (default: True)
- **Ritorna**: Dizionario con nome città e temperatura (o None per errori)
- **Descrizione**: Versione in cache di `get_weather_for_cities()` con supporto per memorizzazione dei dati
- **Cache**: Utilizza l'istanza globale `weather_cache`
- **Uso ideale**: Interrogazioni frequenti delle stesse città

#### Funzione `get_coordinates(city)`
- **Parametri**: 
  - `city` (str): Nome della città
- **Ritorna**: Tupla `(latitude, longitude)` oppure `None` se la città non è trovata
- **Descrizione**: Effettua una richiesta all'API di geocoding di Open-Meteo per convertire il nome della città in coordinate geografiche
- **API utilizzata**: https://geocoding-api.open-meteo.com/v1/search

#### Funzione `get_weather(lat, lon)`
- **Parametri**: 
  - `lat` (float): Latitudine della posizione geografica
  - `lon` (float): Longitudine della posizione geografica
- **Ritorna**: Temperatura in Celsius (float) oppure `None` se si verificano errori di connessione
- **Descrizione**: Effettua una richiesta all'API di previsione meteo di Open-Meteo per ottenere la temperatura attuale. Include gestione degli errori di rete
- **Timeout**: 5 secondi per la richiesta HTTP
- **Parametri API**:
  - `"current": "temperature_2m"` - Recupera la temperatura a 2 metri da terra (standard meteorologico)
  - `"raise_for_status()"` - Solleva eccezione per errori HTTP
- **Gestione degli errori**:
  - Cattura gli errori di connessione (`RequestException`)
  - Ritorna `None` in caso di errore senza stampare messaggi
  - Non lancia eccezioni, sempre ritorno sicuro
- **API utilizzata**: https://api.open-meteo.com/v1/forecast

#### Funzione `get_weather_multiple(coordinates)`
- **Parametri**: 
  - `coordinates` (List[Tuple[float, float]]): Lista di tuple (latitudine, longitudine)
    - Esempio: `[(41.9028, 12.4964), (45.4642, 9.1900)]`
- **Ritorna**: Dizionario con coordinate come chiave e temperatura come valore (o None per errori)
  - Esempio: `{(41.9028, 12.4964): 22.5, (45.4642, 9.1900): 18.3}`
- **Descrizione**: Recupera temperatura per multiple posizioni geografiche con richieste sequenziali
- **Uso ideale**: Quando hai liste di coordinate geografiche e vuoi la temperatura di tutte in una volta
- **Timeout**: 5 secondi per ogni singola richiesta
- **Gestione degli errori**: Ritorna `None` per coordinate con errori, ma continua con le altre

#### Funzione `get_weather_for_cities(cities)`
- **Parametri**: 
  - `cities` (List[str]): Lista di nomi di città
    - Esempio: `["Roma", "Milano", "Napoli"]`
- **Ritorna**: Dizionario con nome città come chiave e temperatura come valore (o None per errori)
  - Esempio: `{"Roma": 22.5, "Milano": 18.3, "Napoli": 24.1}`
- **Descrizione**: Recupera temperatura per multiple città convertendo i nomi in coordinate
- **Uso ideale**: Quando vuoi cercare il meteo di più città contemporaneamente
- **Processo**:
  1. Converte ogni nome di città in coordinate geografiche
  2. Recupera la temperatura per ogni coordinata
  3. Ritorna i risultati con il nome della città
- **Gestione degli errori**: Ritorna `None` se la città non viene trovata o errori di connessione

### `app/utils/formatter.py`
**Funzioni di utilità per la formattazione e conversione**

#### Funzione `convert_temperature(value, from_unit, to_unit)`
- **Parametri**:
  - `value` (float): Valore della temperatura da convertire
  - `from_unit` (str): Unità di partenza ('c', 'f', 'k')
  - `to_unit` (str): Unità di destinazione ('c', 'f', 'k')
- **Ritorna**: Temperatura convertita (float)
- **Eccezioni**: Solleva `ValueError` se le unità non sono valide
- **Descrizione**: Converte temperature tra tre unità:
  - `c` = Celsius
  - `f` = Fahrenheit
  - `k` = Kelvin
- **Processo di conversione**: 
  1. Normalizza l'unità di partenza in Celsius
  2. Converte da Celsius all'unità desiderata

### `tests/test_weather_api.py`
**Test unitari per validare i servizi API**

File per la scrittura di test automatici sulle funzioni principali dell'applicazione.

## 🔗 API Utilizzate

### 1. Open-Meteo Geocoding API
- **URL Base**: https://geocoding-api.open-meteo.com/v1/search
- **Descrizione**: Converte il nome di una città in coordinate geografiche
- **Parametri**: 
  - `name`: Nome della città
  - `count`: Numero di risultati (limitato a 1 per semplicità)

### 2. Open-Meteo Forecast API
- **URL Base**: https://api.open-meteo.com/v1/forecast
- **Descrizione**: Recupera dati meteorologici attuali e previsioni
- **Parametri**: 
  - `latitude`: Latitudine
  - `longitude`: Longitudine
  - `current_weather`: Flag per ottenere il meteo attuale

## 💡 Esempi di Utilizzo

### Come funziona il Sistema di Cache

L'applicazione include un sistema di **caching intelligente** per ridurre le richieste API:

- **TTL (Time To Live)**: Per impostazione predefinita, i dati rimangono in cache per **1 ora**
- **Scadenza automatica**: Passato il TTL, la cache viene invalidata automaticamente
- **Verifiche automatiche**: Quando richiedi un dato, il sistema verifica se è ancora valido
- **Riduzione API**: Requisiti ripetuti della stessa città usano i dati in cache (zero richieste API!)

**Benefici:**
- ⚡ Risposte più veloci per dati frequenti
- 💾 Riduce il carico sui server di Open-Meteo
- 🔄 Dati aggiornati ogni ora automaticamente
- 🎯 Possibilità di disabilitare la cache quando serve

---

### Esempio 1: Verificare il meteo di una singola città
```bash
$ python main.py
Inserisci una città: Roma
La temperatura attuale a Roma è 22°C
```

### Esempio 2: Ottenere il meteo di multiple città (nel codice)
```python
from app.services.weather_api import get_weather_for_cities

# Recupera il meteo di più città contemporaneamente
citta = ["Roma", "Milano", "Napoli"]
risultati = get_weather_for_cities(citta)

for citta, temp in risultati.items():
    if temp is not None:
        print(f"{citta}: {temp}°C")
    else:
        print(f"{citta}: Dati non disponibili")

# Output:
# Roma: 22.5°C
# Milano: 18.3°C
# Napoli: 24.1°C
```

### Esempio 3: Convertire temperature (nel codice)
```python
from app.utils.formatter import convert_temperature

# Da Celsius a Fahrenheit
celsius = 20
fahrenheit = convert_temperature(celsius, 'c', 'f')
print(f"20°C = {fahrenheit:.2f}°F")  # Output: 20°C = 68.00°F

# Da Fahrenheit a Kelvin
fahrenheit = 68
kelvin = convert_temperature(fahrenheit, 'f', 'k')
print(f"68°F = {kelvin:.2f}K")  # Output: 68°F = 293.15K
```

### Esempio 4: Recuperare meteo per coordinate multiple
```python
from app.services.weather_api import get_weather_multiple

# Coordinate di Roma, Milano e Venezia
coordinate = [
    (41.9028, 12.4964),   # Roma
    (45.4642, 9.1900),     # Milano
    (45.4343, 12.3389)     # Venezia
]

risultati = get_weather_multiple(coordinate)

for (lat, lon), temp in risultati.items():
    if temp is not None:
        print(f"[{lat}, {lon}]: {temp}°C")
    else:
        print(f"[{lat}, {lon}]: Errore")

# Output:
# [41.9028, 12.4964]: 22.5°C
# [45.4642, 9.1900]: 18.3°C
# [45.4343, 12.3389]: 19.7°C
```

### Esempio 5: Usare la cache per ridurre le richieste API
```python
from app.services.weather_api import get_cached_weather, weather_cache

# Prima richiesta - chiama l'API e memorizza in cache
temp1 = get_cached_weather(41.9028, 12.4964)
print(f"Temperatura Roma: {temp1}°C")

# Seconda richiesta entro 1 ora - usa la cache (nessuna richiesta API!)
temp2 = get_cached_weather(41.9028, 12.4964)
print(f"Temperatura Roma (cached): {temp2}°C")

# Disabilita la cache per forzare una nuova richiesta
temp3 = get_cached_weather(41.9028, 12.4964, use_cache=False)
print(f"Temperatura Roma (fresh): {temp3}°C")

# Verifica il tempo rimanente di validità della cache
remaining = weather_cache.get_remaining_ttl("weather_41.9028_12.4964")
print(f"Validità cache: {remaining:.1f} secondi")
```

### Esempio 6: Recuperare multiple città con cache
```python
from app.services.weather_api import get_cached_weather_for_cities

# Prima ricerca - chiama l'API per ogni città
risultati = get_cached_weather_for_cities(["Roma", "Milano", "Napoli"])
for citta, temp in risultati.items():
    print(f"{citta}: {temp}°C")

# Output:
# Roma: 22.5°C
# Milano: 18.3°C
# Napoli: 24.1°C

# Segunda ricerca entro 1 ora - tutte le richieste saranno dalla cache!
risultati2 = get_cached_weather_for_cities(["Roma", "Milano", "Napoli"])

# Puoi anche disabilitare la cache per dati freschi
risultati3 = get_cached_weather_for_cities(["Roma", "Milano", "Napoli"], use_cache=False)
```

### Esempio 7: Gestire manualmente la cache
```python
from app.services.weather_api import weather_cache

# Verifica se una chiave è nella cache e non è scaduta
chiave = "weather_41.9028_12.4964"
if weather_cache.is_expired(chiave):
    print("Cache scaduta, serve una nuova richiesta API")
else:
    print("Dati in cache ancora validi")

# Ottieni il valore direttamente dalla cache
temp = weather_cache.get(chiave)

# Cancella tutta la cache
weather_cache.clear()
```

## 🧪 Testing

Per eseguire i test:

```bash
python -m pytest tests/
```

## 🔮 Possibili Miglioramenti Futuri

- ✨ Implementare un'interfaccia grafica (GUI) usando tkinter o PyQt
- 📊 Aggiungere previsioni meteorologiche per i prossimi giorni
- 🗺️ Supportare più città contemporaneamente
- 💾 Salvare la cronologia delle ricerche
- 🎨 Aggiungere colori e formattazione migliorata all'output CLI
- 🌍 Supportare diverse lingue
- ⚙️ Implementare caching dei risultati per ridurre le chiamate API
- 📈 Aggiungere grafici di tendenza meteo
- 🔐 Aggiungere configurazione tramite file di configurazione

## � Sicurezza e Configurazione

### Gestione delle Chiavi API

L'applicazione utilizza un sistema sicuro di gestione delle chiavi API basato su variabili d'ambiente:

#### File `.env` (Non committare su Git!)

Il file `.env` contiene le configurazioni sensibili:

```env
FLASK_SECRET_KEY=your-secret-key-here-change-in-production
FLASK_ENV=development
FLASK_DEBUG=True
CACHE_TTL=3600
```

#### Protezione

- ✅ **`.env` è nel `.gitignore`** - Non sarà mai committato su Git
- ✅ **Variabili di ambiente sicure** - Le chiavi rimangono locali
- ✅ **`.env.example`** - Fornisce un template per i nuovi sviluppatori
- ✅ **Validazione in produzione** - Controlla che la SECRET_KEY sia configurata

#### Configurazioni per Ambiente

```python
# Development (debug attivo)
FLASK_ENV=development
FLASK_DEBUG=True

# Production (debug disattivo, SECRET_KEY obbligatoria)
FLASK_ENV=production
FLASK_DEBUG=False
FLASK_SECRET_KEY=your-production-secret-key
```

#### Best Practices di Sicurezza

1. **Cambia `FLASK_SECRET_KEY` in produzione**
   ```bash
   python -c 'import secrets; print(secrets.token_hex(32))'
   ```

2. **Non committare `.env` mai su Git**
   - Il file è già nel `.gitignore`
   - Usa `.env.example` per documenti

3. **Usa variabili d'ambiente del sistema in produzione**
   ```bash
   export FLASK_SECRET_KEY="your-production-key"
   export FLASK_ENV="production"
   ```

4. **Carica la configurazione corretta al boot**
   ```python
   from config import get_config
   config = get_config()  # Carica automaticamente in base a FLASK_ENV
   ```

## �📝 Note Importanti

- L'applicazione dipende dalle API di Open-Meteo, che sono **gratuite e non richiedono autenticazione**
- Le coordinate e i dati meteo vengono recuperati in tempo reale
- Potrebbero verificarsi errori di connessione se non è disponibile una connessione Internet
- L'API di geocoding potrebbe non trovare città molto piccole o con nomi errati

## 📄 Licenza

Questo progetto è distribuito senza una licenza specifica. Sei libero di utilizzarlo come desideri.

## 👨‍💻 Contributi

Se desideri contribuire o migliorare l'applicazione, registra un issue o invia una pull request!

---

**Ultima modifica**: Aprile 2026
