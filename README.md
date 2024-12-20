

```markdown
# Audio Transcription und Video Untertitel Integration

Dieses Repository enthält mehrere Python-Skripte, die Funktionen zur Transkription von Audiodateien und zum Hinzufügen von Untertiteln zu Videos integrieren.

## Dateien

1. **wisper.py** - Ein Skript zur Transkription von Audiodateien in Text mithilfe des Whisper-Modells. Es lädt eine Audiodatei, teilt sie in Segmente und transkribiert jedes Segment einzeln.
   
2. **srt.py** - Ein Skript, das eine Liste von Transkriptionen (mit Zeitstempeln) verarbeitet und diese in das SRT-Format (SubRip Subtitle) umwandelt. Die Transkriptionen enthalten Texte mit Start- und Endzeiten, die im Untertitel-Format gespeichert werden.

3. **videosrt.py** - Ein Skript, das das SRT-Untertitel-Dateiformat zusammen mit einem Video kombiniert. Es verwendet `ffmpeg`, um das Video mit den generierten Untertiteln zu versehen und ein neues Video zu erstellen.

## Voraussetzungen

- Python 3.6 oder höher
- Installierte Python-Bibliotheken:
  - `whisper` (für die Transkription von Audiodateien)
  - `pydub`
  - `ffmpeg` (muss installiert sein)
  - `math`

Du kannst die notwendigen Pakete mit folgendem Befehl installieren:

```bash
pip install whisper pydub
```

Für `ffmpeg` musst du es separat installieren, je nach Betriebssystem:
- **Windows**: [ffmpeg Downloads](https://ffmpeg.org/download.html)
- **macOS/Linux**: Verwende `brew install ffmpeg` (für macOS) oder `apt-get install ffmpeg` (für Linux).

## Installation

1. **Python** und **ffmpeg** müssen auf deinem System installiert sein.
2. Stelle sicher, dass du die erforderlichen Python-Bibliotheken installierst (siehe oben).
3. Lade die Audiodatei (MP3, WAV, FLAC) und die Videos, die du analysieren möchtest, in das Verzeichnis, das die Skripte enthält.

## Nutzung

### 1. **wisper.py** - Audio Transkribieren

Das Skript **wisper.py** verwendet das Whisper-Modell zur Transkription einer Audiodatei in Text. Es lädt eine Audiodatei, teilt sie in 2-Minuten-Segmente und transkribiert jedes Segment.

Führe das Skript wie folgt aus:

```bash
python wisper.py
```

### 2. **srt.py** - Transkriptionen in Untertitel umwandeln

Das Skript **srt.py** nimmt die Transkriptionen mit Zeitstempeln und wandelt sie in das SRT-Format um, das für Untertitel verwendet wird.

Führe das Skript wie folgt aus:

```bash
python srt.py
```

Die Untertitel werden in der Datei `subtitles.srt` gespeichert.

### 3. **videosrt.py** - Untertitel zu einem Video hinzufügen

Das Skript **videosrt.py** fügt die SRT-Untertitel zu einem Video hinzu und erstellt ein neues Video mit den Untertiteln. Stelle sicher, dass du `ffmpeg` installiert hast.

Führe das Skript wie folgt aus:

```bash
python videosrt.py
```

Es wird ein neues Video mit dem Namen `output_video_with_subtitles.mp4` erstellt, das die Untertitel enthält.

## YouTube Video

Schau dir das Ergebnisvideo hier an:  
[**Video mit Untertiteln**](https://youtu.be/f2GhISWc94M?si=zvF5hoi5P5knib2G)



