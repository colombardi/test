# Intenzionalmente vulnerabile, SOLO per test locali con Trivy
# Base EOL (fine supporto) => tante CVE a livello OS
FROM ubuntu:18.04

# Lavorare da root (pratica insicura, lasciata apposta)
USER root

# Aggiorna indici e installa python/pip senza pin sicuri (pratica insicura)
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Variabile di “segreto” hardcoded (cattiva pratica, utile per test misconfigurazioni)
ENV APP_SECRET="hardcoded-in-image"

# Requirements deliberatamente datati e vulnerabili
# (versioni vecchie note per avere CVE; non usarle in produzione)
RUN printf "flask==0.12.2\nrequests==2.19.0\nurllib3==1.23\npyyaml==5.1\n" > /tmp/requirements.txt && \
    python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

# App fittizia (non sicura) che espone una porta senza hardening
WORKDIR /app
RUN printf "from flask import Flask\napp=Flask(__name__)\n@app.route('/')\ndef hi(): return 'hello'\napp.run(host='0.0.0.0', port=5000)\n" > app.py
EXPOSE 5000

# Nessun utente non-root, nessun healthcheck (altre cattive pratiche)
CMD [ "python3", "app.py" ]

