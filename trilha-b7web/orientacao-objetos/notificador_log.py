from notificador import Notificador

class NotificadorLog(Notificador):
    def enviar(self, mensagem):
        with open("log.txt", "a") as f:
            f.write(f"[LOG] {mensagem}\n")

