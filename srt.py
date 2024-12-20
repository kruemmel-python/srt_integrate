# Beispiel-Liste mit bereinigten Zeitstempeln und Texten
transcriptions = [
    {"start": 0.0, "end": 18.6, "text": "In den Tiefen des Binärs wo Nullen und Einsen tanzen Liebte ich einst die Technik, die mich in ihren Bann zog"},
    {"start": 18.6, "end": 28.8, "text": "Der Schneider mit Greenscreen, mein Basic-Programmierfreund Ob er wohl meine Zeilen mochte, die ich ihm schrieb"},
    {"start": 31.0, "end": 48.0, "text": "Der Commodore 16 und der Amiga 500, sie flüsterten mir Geheimnisse, während der 286 erwartete sein BIOS"},
    {"start": 48.0, "end": 57.0, "text": "Ein Rätsel, das ich zu entschlüssen suchte und der iMac G3, den ich flüchtig verschenkte"},
    {"start": 57.0, "end": 68.0, "text": "Wir sind die Kinder der Code in einer Welt voller Daten Unsere Herzen schlagen im Takt der Maschinen"},
    {"start": 68.0, "end": 78.0, "text": "Die Liebe zur Technik, sie hält uns gefangen In den Tiefen des Binärs wo Nullen und Einsen tanzen"},
    {"start": 78.0, "end": 87.0, "text": "Das Programmieren, ein ständiger Begleiter, fraß an meiner Seele, machte mich müde und leer"},
    {"start": 87.0, "end": 97.0, "text": "Ich wandte mich ab, begab mich auf einer Handwerkerreise Doch die Tastatur rief mich zurück, verlangte nach meinem Finger"},
    {"start": 98.0, "end": 108.0, "text": "Wir sind die Kinder der Codes in einer Welt voller Daten Unsere Herzen schlagen im Takt der Maschinen"},
    {"start": 108.0, "end": 119.0, "text": "Die Liebe zur Technik, sie hält uns gefangen In den Tiefen des Binärs wo Nullen und Einsen tanzen"},
    {"start": 120.0, "end": 125.0, "text": "Und Einsen tanzen"},
    {"start": 128.0, "end": 130.0, "text": "Moderne KI"},
    {"start": 130.0, "end": 132.0, "text": "Ein Zauber, der mich ergriff"},
    {"start": 132.0, "end": 136.0, "text": "Meine Finger flogen über die Tasten"},
    {"start": 136.0, "end": 138.0, "text": "Als wären sie frei"},
    {"start": 138.0, "end": 142.0, "text": "Emotionale Empathie"},
    {"start": 142.0, "end": 144.0, "text": "Ein Geschenk, das uns verbindet"},
    {"start": 144.0, "end": 148.0, "text": "Wir halten fest, fliegen weiter"},
    {"start": 148.0, "end": 151.0, "text": "Mit Träumen im Herzen"},
    {"start": 151.0, "end": 156.0, "text": "Die Cloud, ein unendlicher Himmel aus Daten"},
    {"start": 156.0, "end": 161.0, "text": "Speichert unsere Erinnerungen, unsere Geschichten"},
    {"start": 161.0, "end": 166.0, "text": "Von alten Disketten zu virtuellen Welten"},
    {"start": 166.0, "end": 173.0, "text": "Wir sind die Hüter der Vergangenheit und der Zukunft"},
    {"start": 173.0, "end": 179.0, "text": "Wir sind die Kinder der Codes in einer Welt voller Daten"},
    {"start": 179.0, "end": 184.0, "text": "Unsere Herzen schlagen im Takt der Maschinen"},
    {"start": 184.0, "end": 189.0, "text": "Die Liebe zur Technik, sie hält uns gefangen"},
    {"start": 189.0, "end": 193.0, "text": "In den Tiefen des Binärs wo Nullen"},
    {"start": 193.0, "end": 195.0, "text": "Und Eisen tanzen"},
    {"start": 195.0, "end": 199.0, "text": "Die Algorithmen tanzen im Rhythmus der Zeit"},
    {"start": 199.0, "end": 204.0, "text": "Entschlüsseln Geheimnisse berechnen die Sterne"},
    {"start": 204.0, "end": 209.0, "text": "Wir sind die Dirigenten dieses digitalen Orchesters"},
    {"start": 209.0, "end": 215.0, "text": "Mit Nullen und Einsen komponieren wir unsere Melodien"},
    {"start": 215.0, "end": 220.0, "text": "Und wenn die Sonne untergeht, die Bildschirme erlöschen"},
    {"start": 220.0, "end": 226.0, "text": "Werden wir weiterhin in den Tiefen des Binärs tanzen"},
    {"start": 226.0, "end": 231.0, "text": "Die Liebe zur Technik, sie trägt uns durch die Nacht"},
    {"start": 231.0, "end": 236.0, "text": "Wir sind die Kinder der Codes, für immer verbunden"},
    {"start": 240.0, "end": 245.0, "text": "Wir sind die Kinder der Codes, für immer verbunden"},
    {"start": 245.0, "end": 250.0, "text": "Wir sind die Kinder der Codes, in einer Welt voller Daten"},
    {"start": 250.0, "end": 255.0, "text": "Unsere Herzen schlagen im Tag der Maschine"},
    {"start": 255.0, "end": 259.0, "text": "Die Liebe zur Technik, sie hält uns gefangen"},
    {"start": 259.0, "end": 265.0, "text": "In den Tiefen des Binärs wo Nullen und Einsen tanzen"}
]

# Funktion zum Formatieren der Zeit im SRT-Format
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{milliseconds:03}"

# Erstellen Sie die SRT-Datei
srt_content = ""
for i, segment in enumerate(transcriptions, start=1):
    start_time = segment["start"]
    end_time = segment["end"]
    text = segment["text"]
    srt_content += f"{i}\n"
    srt_content += f"{format_time(start_time)} --> {format_time(end_time)}\n"
    srt_content += f"{text}\n\n"

# Speichern Sie die SRT-Datei
with open("subtitles.srt", "w") as srt_file:
    srt_file.write(srt_content)
