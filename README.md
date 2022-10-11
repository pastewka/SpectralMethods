# Simulationstechniken

Dieses Repositorium enthält Vorlesungsunterlagen für die Veranstaltung "Simulationstechniken" an der Albert-Ludwigs-Universität Freiburg. Die veröffentlichten Seiten können [hier](https://pastewka.github.io/Simulationstechniken/) gefunden werden.

## Entwicklung

Um die Seite lokal auszuführen, wird eine Datei `_config.docker.yml` mit folgenden Inhalten benötigt:
```yaml
url: "http://localhost:4000"
```

Die Seite kann dann mit Hilfe von Docker ausgeführt werden:
```bash
JEKYLL_VERSION=4.0 docker run --rm -e "JEKYLL_ENV=docker" --name Simulationstechniken --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll jekyll serve --config _config.yml,_config.docker.yml
```

Neustart des Docker-Containers:
```bash
docker restart Simulationstechniken
```