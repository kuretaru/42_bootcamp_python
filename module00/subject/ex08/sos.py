"""
Morse Code Converter and Player.

This script converts text provided via command-line arguments into Morse code.
It supports three modes of operation controlled by environment variables:
1.  Default: Prints the Morse code to the console.
2.  SOUND_MODE=1: Plays the Morse code as audible tones.
3.  SAVE_MODE=1: Saves the Morse code audio to a .wav file.

Dependencies:
    - pygame: For playing audio.
    - numpy: For numerical operations on audio data.
    - scipy: For writing .wav files.
"""


import os
import sys
import time


SOUND_MODE = os.getenv('SOUND_MODE', '0').lower() in ['1', 'true', 't']
SAVE_MODE = os.getenv('SAVE_MODE', '0').lower() in ['1', 'true', 't']


if SOUND_MODE or SAVE_MODE:
    try:
        import pygame
        import numpy as np
    except ImportError:
        print("Library pygame or/and numpy isn't found. Please install it with pip install pygame numpy")
        sys.exit()


if SAVE_MODE:
    try:
        from scipy.io import wavfile
    except ImportError:
        print("Library scipy isn't found. Please install it with pip install scipy")
        sys.exit()


MORSE_ALPHA={
    "A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.",
    "H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.",
    "O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-",
    "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."," ":"/",
    "0":"-----","1":".----","2":"..---","3":"...--","4":"....-",
    "5":".....","6":"-....","7":"--...","8":"---..","9":"----"
}


def print_morse(text):
    """
    Simply prints a morse on the screen (ex08).

    Attributes:
        text: Text for the printing its representation in morse-code. 
    """
    for symbol in text:
        if symbol.upper() in MORSE_ALPHA:
            print(f"{MORSE_ALPHA[symbol.upper()]}", end=" ")
    print()
        

def generate_tone(duration,frequency,simple_rate):
    """
    Generates a voice signal (sinusoide) of the selected duration.

    Attributes:
        duration:       Duration of the sinusoide for voice signal.
        freequency:     A freequency of waves for the tone generating.
        simple_rate:    Simple Rate Quality of sound.

    Returns:
        int: Audio tone object.
    """
    t = np.linspace(0,duration,int(duration*simple_rate),False)
    tone = np.sin(frequency*t*2*np.pi)
    audio = tone*(2**15-1)/np.max(np.abs(tone))
    return audio.astype(np.int16)


def generate_silence(duration,simple_rate):
    """
    Generates a silence of the selected duration.

    Attributes:
        duration:       Duration of the voice signal.
        simple_rate:    Simple Rate Quality of sound.

    Returns:
        np.zeros Array filled with zeros
    """
    return np.zeros(int(duration*simple_rate),dtype=np.int16)


def play_morse(text):
    """
    Play morse-signal as sound.

    Attributes:
        text: Text for the processing its representation as sound.
    """
    dot_duration, freequency, simple_rate = .1, 880, 44100
    dash_duration = dot_duration*3
    intra_char_pause = dot_duration
    char_pause = dot_duration*3

    pygame.mixer.init(frequency=simple_rate, size=-16, channels=1)

    for symbol in text:
        char = symbol.upper()
        if char in MORSE_ALPHA:
            morse_code = MORSE_ALPHA[char]
            if morse_code == "/":
                print(" /", end=" ", flush=True)
                time.sleep(dot_duration*7)
                continue
            for i, signal in enumerate(morse_code):
                duration = dot_duration if signal == "." else dash_duration
                tone = generate_tone(duration, freequency, simple_rate)
                sound = pygame.sndarray.make_sound(tone)
                sound.play()
                pygame.time.wait(int(duration*1000))
                print(signal, end="", flush=True)

                if i < len(morse_code)-1:
                    time.sleep(intra_char_pause)
    print()


def save_audio_morse(text, filename="morse_output.wav"):
    """
    Generates and save a morse-code in wav-format.

    Attributes:
        text        Text for the processing its representation as sound.
        filename    Filename to save sound.
    """
    dot_duration, frequency, sample_rate = .15, 750, 44100
    dash_duration = dot_duration * 3

    dot_sound = generate_tone(dot_duration, frequency, sample_rate)
    dash_sound = generate_tone(dash_duration, frequency, sample_rate)
    p1 = generate_silence(dot_duration, sample_rate)    # Pause between signals
    p3 = generate_silence(dot_duration*3, sample_rate)  # Pause between letters
    p7 = generate_silence(dot_duration*7, sample_rate)  # Pause between words
    
    audio_segments = []
    for symbol in text:
        char = symbol.upper()
        if char in MORSE_ALPHA:
            morse_code = MORSE_ALPHA[char]
            if morse_code == '/':
                print(" /", end=" ", flush=True)
                audio_segments.append(p7)
                continue

            for i, signal in enumerate(morse_code):
                if signal == '.':
                    audio_segments.append(dot_sound)
                else:
                    audio_segments.append(dash_sound)
                print(signal, end="", flush=True)
                
                if i < len(morse_code) - 1:
                    audio_segments.append(p1)

            print(" ", end="", flush=True)
            audio_segments.append(p3)

    final_audio = np.concatenate(audio_segments)
    wavfile.write(filename, sample_rate, final_audio)
    print(f"\nSuceed! File saved in: {filename}")


def main():
    """
    ARGV -> Morse code. Availible output chars are [".","-","/"," "].
    Space is a "/".

    Returns:
        None:   If there's not enough argv.
        1:      Same as w/None (but only in SOUND or SAVE_SOUND modes)
    """
    if len(sys.argv) < 2:
        print("Error!")
        if SOUND or SAVE_SOUND:
            print("Example: python sos.py 'Hello World'", file=sys.stderr)
            sys.exit(1)
        else:
            return
        
    input_text = " ".join(sys.argv[1:])

    if SAVE_MODE:
        save_audio_morse(input_text)
    elif SOUND_MODE:
        play_morse(input_text)
    else:
        print_morse(input_text)


if __name__ == "__main__":
    main()