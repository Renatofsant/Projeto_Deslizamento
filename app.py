import serial
import pywhatkit
import time

# Configurar a porta serial (substitua 'COM8' pela porta correta no seu sistema)
ser = serial.Serial('COM8', 9600)

# Variável para armazenar o último valor de alerta enviado
ultimo_alerta_enviado = None

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(f"Valor do sensor: {line}")  # Mostra o valor recebido no terminal

        if "ALERTA_DESLIZAMENTO" in line:
            # Obter a hora atual e adicionar 2 minutos
            hora_atual = time.localtime().tm_hour
            minuto_atual = time.localtime().tm_min
            minuto_envio = minuto_atual + 2

            # Caso o minuto ultrapasse 59, ajusta a hora e o minuto
            if minuto_envio >= 60:
                minuto_envio -= 60
                hora_atual += 1
                if hora_atual == 24:
                    hora_atual = 0

            # Enviar mensagem via WhatsApp para o grupo
            pywhatkit.sendwhatmsg_to_group("BVTFDQVLn4H6f9sNEusbOO",
                                           "SMD-PERNAMBUCO, INFORMA: PERIGO! SOLO COM UMIDADE INTENSA DETECTADA, RISCO IMINENTE DE DESLIZAMENTO. BUSQUE IMEDIATAMENTE UM ABRIGO.",
                                           hora_atual, minuto_envio)
            print("Mensagem de alerta enviada via WhatsApp.")

            # Atualizar o último alerta enviado
            ultimo_alerta_enviado = "ALERTA_DESLIZAMENTO"
        else:
            # Resetar a variável se o alerta não estiver mais presente
            ultimo_alerta_enviado = None

    time.sleep(1)
