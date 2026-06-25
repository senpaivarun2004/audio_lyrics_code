import time
import sys
import pygame

def type_lyric(line, duration):
    """Type out a lyric line, finishing in roughly 'duration' seconds."""
    if len(line) == 0:
        time.sleep(duration)
        return
    char_delay = duration / len(line)
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()

def print_lyrics():
    # Adjust this delay (in seconds) if the lyrics are out of sync with the music.
    # A positive value delays the lyrics, while a negative value makes them appear sooner.
    time_delay = 3.38 # Increased delay by 3.38 seconds to fix timing mismatch

    # (timestamp_seconds, lyric_line)
    # Timestamps auto-detected from audio analysis (46.1s total duration)
    timed_lyrics = [
        (0.5,  "Baato-baato me hi, Khwabo-khwabo me hi mere qareeb hai tu"),
        (5.5,  "Teri talab mujhko, teri talab, jaana, ho tu kabhi ru-ba-ru"),
        (11.0, "Shor-sharaba jo seene me hai mere, kaise bayaan mai karuu"),
        (17.0, "Haal jo mera hai, mai kis ko batau?"),
        (21.0, "Mere sahiba, dil na kiraaye ka, thoda to sambhalo na"),
        (27.0, "Nazuk hai yeh, toot jaata hai"),
        (31.0, "Sahiba, neende-veende aaye na,"),
        (35.0, "Raate kaati jaaye na"),
        (39.0, "Tera hi khayal din-rain aata hai"),
    ]

    pygame.mixer.init()
    pygame.mixer.music.load("sahiba_audio.mp3.mp3")
    pygame.mixer.music.play()

    print("\n ~ Now Playing - Sahiba ~ \n")

    start_time = time.time()

    for i, (timestamp, line) in enumerate(timed_lyrics):
        # Wait until the right moment to start typing this line
        elapsed = time.time() - start_time
        wait = (timestamp + time_delay) - elapsed
        if wait > 0:
            time.sleep(wait)

        # Calculate typing duration so line finishes before next one starts
        if i + 1 < len(timed_lyrics):
            line_duration = timed_lyrics[i + 1][0] - timestamp - 0.3
        else:
            line_duration = 4.0
        line_duration = max(line_duration, 1.0)

        type_lyric(line, line_duration)

    # Keep running until the music finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

if __name__ == "__main__":
    print_lyrics()