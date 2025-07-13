from notificador import Notificador

class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f"[SMS] {mensagem}")
        