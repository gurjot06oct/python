import math
import wave
import array
def generate_sine_wave(frequency, duration, amplitude=32767, sample_rate=44100):
    num_samples = int(sample_rate * duration)
    wave_data = array.array('h', [0] * num_samples)

    for i in range(num_samples):
        t = float(i) / sample_rate
        wave_data[i] = int(amplitude * math.sin(2 * math.pi * frequency * t))

    return wave_data

def save_wave_file(filename, wave_data, sample_rate=44100):
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16 bits per sample
        wf.setframerate(sample_rate)
        wf.writeframes(wave_data.tobytes())

# Example usage
if __name__ == "__main__":
    duration = 1  # in seconds
    sample_rate = 44100  # CD quality
    frequency = 440  # A4 note
    amplitude = 32767  # Maximum amplitude for 16-bit audio

    sound_wave = generate_sine_wave(frequency, duration, amplitude, sample_rate)

    save_wave_file("random_sound.wav", sound_wave, sample_rate)
