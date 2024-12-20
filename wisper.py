from pydub import AudioSegment
from openai import OpenAI
import math

client = OpenAI()

# Laden Sie die Audiodatei
audio = AudioSegment.from_file("1220.mp3")

# Definieren Sie die maximale Länge eines Segments in Millisekunden (z.B. 2 Minuten)
max_segment_length = 2 * 60 * 1000  # 2 Minuten in Millisekunden

# Berechnen Sie die Anzahl der Segmente
num_segments = math.ceil(len(audio) / max_segment_length)

# Liste zur Speicherung der Transkriptionen und Zeitstempel
transcriptions = []

# Teilen Sie die Audiodatei in Segmente und transkribieren Sie diese
for i in range(num_segments):
    start_time = i * max_segment_length
    end_time = min((i + 1) * max_segment_length, len(audio))
    segment = audio[start_time:end_time]

    # Speichern Sie das Segment in einer temporären Datei
    segment_file_path = f"segment_{i}.mp3"
    segment.export(segment_file_path, format="mp3")

    # Öffnen Sie die temporäre Datei
    with open(segment_file_path, "rb") as segment_file:
        # Erstellen Sie die Transkription für das Segment
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=segment_file,
            response_format="verbose_json"  # Anfordern des ausführlichen JSON-Formats, um Zeitstempel einzuschließen
        )

        # Bereinigen Sie die Zeitstempel
        for segment in transcription.segments:
            segment.start += start_time / 1000  # Konvertieren Sie Millisekunden in Sekunden
            segment.end += start_time / 1000  # Konvertieren Sie Millisekunden in Sekunden
            transcriptions.append(segment)

    # Löschen Sie die temporäre Datei
    import os
    os.remove(segment_file_path)

# Drucken Sie die Transkriptionstexte mit bereinigten Zeitstempeln
for segment in transcriptions:
    start_time = segment.start
    end_time = segment.end
    text = segment.text
    print(f"[{start_time}s - {end_time}s]: {text}")
