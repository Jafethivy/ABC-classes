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
    def enviar_notificacion(self, mensaje):
        from slackAPI.selectconver import slack
        slack(mensaje)

###################################################################### Clase Admin

class Administrador_Notificaciones:
    def enviar(self, destinatario, mensaje, notificador):
        nt = notificador()
        if destinatario == "slack":
            nt.enviar_notificacion(mensaje)
        else:
            print(nt.enviar_notificacion(destinatario, mensaje))