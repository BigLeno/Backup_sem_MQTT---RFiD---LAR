from MFRC522 import MFRC522
from machine import Pin, SPI
from time import sleep_ms
global rele

# spi = SPI(2, baudrate=2500000, polarity=0, phase=0)
# spi.init()
# rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)
# #pin2 = machine.Pin(13, machine.Pin.OUT) #verde
# #pin1 = machine.Pin(14, machine.Pin.OUT) #vermelho
# rele = Pin(2, Pin.OUT)

print("Encoste o cartão...")

bancoPessoas = [
    {'nome': 'Livia Moura', 'cargo': 'Dona do URA', 'id': '0xabfb4540'},
    {'nome': 'Marcus', 'cargo': 'O Alemão', 'id': '0xaa016ae6'},
    {'nome': 'Rutileno', 'cargo': 'Rei_do_Camarote', 'id': '0xbc64c6c3'},
    {'nome': 'Jerônimo', 'cargo': 'Impostor', 'id': '0xc7981ef3'},
    {'nome': 'Luis', 'cargo': 'Admin', 'id': '0xc7981ef3'},
    {'nome': 'Chave Geral', 'cargo': 'principal', 'id': '0xd41d37a5'},
    {'nome': 'Pedrinho', 'cargo': 'Boy_do_site', 'id': '0x88058dd1'},
    {'nome': 'Marx', 'cargo': 'Boy_do_banco', 'id': '0x17afe6f1'}
    
]

qtd = len(bancoPessoas)
contador = 0
tentativa = 0
while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    #pin2.value(0)
    #pin1.value(0)
    rele.value(0)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            #print(card_id)
            for i in bancoPessoas:
                if card_id == i['id']:
                    print(f'Encontrado: {i['nome']}, {i['cargo']}')
                    rele.value(1)
                    sleep_ms(2000)
                    break
                elif card_id != i['id']:
                    contador += 1
                    #print(contador)
                    if contador == qtd:
                        print(f'Você não tem permissão para entrar!')
                        contador = 0
                        tentativa += 1
                    if tentativa == 4:
                        print('Aguarde para tentar novamente!')
                        sleep_ms(15000)
                        tentativa = 0
                    continue
        
                   


