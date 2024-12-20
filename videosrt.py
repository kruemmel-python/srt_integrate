import subprocess

# Pfade zu den Dateien
video_path = "Kinder_der_Codes.mp4"
subtitle_path = "subtitles.srt"
output_path = "output_video_with_subtitles.mp4"

# FFMPEG-Befehl zum Einfügen der Untertitel
ffmpeg_command = [
    'ffmpeg',
    '-i', video_path,  # Eingabevideo
    '-vf', f'subtitles={subtitle_path}',  # Untertitel hinzufügen
    '-c:a', 'copy',  # Audio-Codec kopieren
    output_path  # Ausgabevideo
]

# Führen Sie den FFMPEG-Befehl aus
subprocess.run(ffmpeg_command)
