# Import tools.
from machine import Pin, PWM
from time import sleep

# Vibrazioni al secondo
# delle note.
LA2 = 110
F3 = 174
Ab3 = 207
# L'ottava successiva raddoppia
#   la frequenza.
LA3 = LA2 * 2
Bb3 = 233
B3 = 247
Db4 = 277
C4 = 261
D4 = 293
Eb4 = 311
E4 = 329
F4 = F3 * 2
Gb4 = 370
G4 = 392
Ab4 = Ab3 * 2
LA4 = LA3 * 2

#
# Parte preparatoria.
#

# Manda la corrente al pin 23.
pin = Pin(23, Pin.OUT)

# Fai pulsare la corrente del pin.
buzzer = PWM(pin)
buzzer.deinit()
buzzer.init()


def beep(freq, tempo):
    """
    Questa funzione fa suonare il buzzer
    mandando una corrente pulsante
    per un certo numero di secondi.
    """
    VOLUME = 2**15  # Max volume for the buzzer
    print("suono vibrando", freq, "al secondo per ", tempo, "secondi.")
    buzzer.init(freq=freq, duty_u16=VOLUME)
    sleep(tempo)
    # Lower the current.
    buzzer.duty(0)
    # Stop the sound.
    buzzer.deinit()
    # Wait before the next sound.
    sleep(1 / 20)


#
# Inizia il programma,
#   e suona una nota dopo l'altra
#   facendo delle pause di 1/2 secondo.
#
print("Inizia a suonare")
beep(LA2, 1 / 2)
beep(LA2, 1 / 2)
beep(LA2, 1 / 2)
beep(F3, 1 / 3)
beep(C4, 1 / 6)
beep(LA2, 1 / 2)
beep(F3, 1 / 3)
beep(C4, 1 / 6)
beep(LA2, 1 / 2)
sleep(1 / 2)

beep(E4, 1 / 2)
beep(E4, 1 / 2)
beep(E4, 1 / 2)
beep(F4, 1 / 3)
beep(C4, 1 / 6)
beep(Ab3, 1 / 2)
beep(F3, 1 / 3)
beep(C4, 1 / 6)
beep(LA2, 1 / 2)
sleep(1 / 2)

beep(LA4, 1 / 2)
beep(LA2, 1 / 3)
beep(LA2, 1 / 6)
beep(LA4, 1 / 2)
beep(Ab4, 1 / 3)
beep(G4, 1 / 6)
beep(Gb4, 1 / 10)
beep(E4, 1 / 10)
beep(F4, 1 / 10)
sleep(1 / 2)

beep(Bb3, 1 / 6)
beep(Eb4, 1 / 2)
beep(D4, 1 / 3)
beep(Db4, 1 / 6)
beep(C4, 1 / 10)
beep(B3, 1 / 10)
beep(C4, 1 / 10)

print("Fine")
# Stop the current.
buzzer.duty(0)
# Reset the buzzer.
buzzer.deinit()
