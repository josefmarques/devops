from notificador import Notificador

class NotificadorWhatsApp(Notificador):
    def enviar(self, mensagem):
        print(f"[ZAP] {mensagem}")
