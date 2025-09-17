from time import sleep
import sys

def show_alert(message):
    """Displays an alert message with a blinking animation."""
    print(message)
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def is_temperature_ok(temp):
    """Checks if the temperature is within the acceptable range."""
    if temp > 102 or temp < 95:
        show_alert('Critical temperature!')
        return False
    return True

def is_pulse_ok(pulse):
    """Checks if the pulse rate is within the acceptable range."""
    if pulse < 60 or pulse > 100:
        show_alert('Pulse rate out of range!')
        return False
    return True

def is_spo2_ok(spo2):
    """Checks if the oxygen saturation is within the acceptable range."""
    if spo2 < 90:
        show_alert('Oxygen saturation out of range!')
        return False
    return True

def vitals_ok(temperature, pulse_rate, spo2):
    """Evaluates whether all vital signs are within normal ranges."""
    return all([
        is_temperature_ok(temperature),
        is_pulse_ok(pulse_rate),
        is_spo2_ok(spo2)
    ])
