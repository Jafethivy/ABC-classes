from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar_notificacion(self, destinatario, mensaje):
        pass

###################################################################### Clases concretas

class NotificadorCE(Notificador):
    def enviar_notificacion(self, destinatario, mensaje):
        return f"Enviando email a {destinatario}: {mensaje}"

class NotificadorSMS(Notificador):
    def enviar_notificacion(self, destinatario, mensaje):
        return f"Enviando SMS a {destinatario}: {mensaje}"

class NotificadorSlack(Notificador):
    def enviar_notificacion(self, destinatario, mensaje):
        return f"Enviando Slack a {destinatario}: {mensaje}"

###################################################################### Clase Admin


class Administrador_Notificaciones:
    def __init__(self, destinatario, mensaje, notificador):
        self.destinatario = destinatario
        self.mensaje = mensaje
        self.notificador = notificador

    def enviar(self):
        return self.notificador.enviar_notificacion(self.destinatario, self.mensaje)