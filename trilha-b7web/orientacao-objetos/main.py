from notificador_email import NotificadorEmail
from notificador_log import NotificadorLog
from notificador_sms import NotificadorSMS
from notificador_zap import NotificadorWhatsApp
from gerenciador import GerenciadorDeNotificacoes

email = NotificadorEmail()
sms = NotificadorSMS()
zap = NotificadorWhatsApp()
log = NotificadorLog()

gerenciador = GerenciadorDeNotificacoes([email, sms, zap, log])
gerenciador.enviar_todos("Mensagem enviada com sucesso")