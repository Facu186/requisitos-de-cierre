import dht
import machine
import time
import i2c_lcd  # Librería para controlar el LCD 20x4
from machine import Pin
import utime
buzzer= Pin(11,Pin.OUT)

# Configurar el sensor DHT22 en el pin GPIO 4
d = dht.DHT22(machine.Pin(4))  # Ajusta el pin según tu conexión

# Configurar la comunicación I2C para el LCD
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))  # Pines SCL y SDA

# Crear el objeto LCD
lcd = i2c_lcd.I2cLcd(i2c, 0x27, 4, 20)  # Dirección I2C comúnmente 0x27 (ajustar si es diferente)

# Función para mostrar la temperatura y humedad en el LCD
def display_data(temp, hum):
    lcd.clear()  # Limpiar la pantalla
    lcd.putstr("Temp: {:.2f} C".format(temp))  # Mostrar temperatura en la primera línea
    lcd.move_to(0, 1)  # Mover a la segunda línea
    lcd.putstr("Humedad: {:.2f} %".format(hum))  # Mostrar humedad en la segunda línea
  
while True:

    try:
        time.sleep(2)
        d.measure( )
        temp = d.temperature()
        hum = d.humidity()
        
        # Imprimir en consola
        print(f"Temperatura: {temp:.2f} °C")
        print(f"Humedad: {hum:.2f} %")
              # Sonar el buzzer si la temperatura supera los 24 °C
        if temp > 24:
            print(f"esta funcionando")
            buzzer.on()
            utime.sleep_ms(5000)
            print(f"corto")
            buzzer.off()
      
        
        # Mostrar en el LCD
        display_data(temp, hum)
    
    except OSError as e:
        print(f"Error al leer el sensor: {e}")
        lcd.clear()
        lcd.putstr("Error al leer el\nsensor.")
        time.sleep(2)
        
# Configurar el buzzer en el pin GPIO 15
# buzzer = machine.Pin(11, machine.Pin.OUT)

# Función para activar/desactivar el buzzer
def sound_buzzer_active(duration=1):
    buzzer.on() 						 # Activar el buzzer
    print(f"esta funcionando")
    time.sleep(5000)
    buzzer.off()  # Desactivar el buzzer

while True:
    try:
        time.sleep(2)
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        
        # Imprimir en consola
        print(f"Temperatura: {temp:.2f} °C")
        print(f"Humedad: {hum:.2f} %")
        
        # Mostrar en el LCD
        display_data(temp, hum)
        
        # Sonar el buzzer si la temperatura supera los 24 °C
        if temp > 24:
            print(f"esta funcionando")
            sound_buzzer_active()  # Activar el buzzer por 1 segundo
    
    except OSError as e:
        print(f"Error al leer el sensor: {e}")
        lcd.clear()
        lcd.putstr("Error al leer el\nsensor.")
        time.sleep(2)



