from notificador import Notificador

class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        print(f"[EMAIL] {mensagem}")