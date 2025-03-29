# ABC-classes
Problema de POO para el S2A en Python, el problema a resolver es el siguiente:

Un equipo de desarrollo de software está construyendo un sistema que necesita enviar notificaciones a los usuarios. Inicialmente, solo necesitan enviar notificaciones por correo electrónico. Sin embargo, anticipan que en el futuro, podrían necesitar agregar soporte para otros métodos de notificación como SMS, notificaciones push e incluso integraciones con plataformas de mensajería como Slack.
Su tarea es diseñar e implementar un sistema de notificaciones flexible en Python utilizando principios de programación orientada a objetos, centrándose en el concepto de "interfaces" (logrado a través de "duck typing" y clases base abstractas). Este sistema debería permitir la fácil adición de nuevos métodos de notificación sin requerir modificaciones significativas en la lógica central de notificación.
# Requisitos Específicos:
"Interfaz" de Notificación:
Defina una clase base abstracta (o una clase que sirva como una "interfaz") llamada Notificador. Este Notificador debe tener un método llamado enviar_notificacion(self, destinatario, mensaje), que es un método abstracto. 
# Clases de Notificación Concretas:
Implemente clases concretas para diferentes métodos de notificación: NotificadorCorreoElectronico: Envía notificaciones por correo electrónico. (Para simplificar, simplemente imprima un mensaje en la consola que indique que se enviaría un correo electrónico). NotificadorSMS: Envía notificaciones por SMS. (Nuevamente, simule esto imprimiendo un mensaje). (Desafío Opcional) NotificadorSlack: Envía notificaciones a un canal de Slack. (Esto requeriría usar una biblioteca de la API de Slack, lo que lo convierte en un desafío más avanzado).
# Administrador de Notificaciones:
Cree una clase AdministradorNotificaciones. Esta clase debe tener un método llamado enviar(self, destinatario, mensaje, notificador). El parámetro notificador debe aceptar cualquier objeto que se adhiera a la "interfaz" Notificador (es decir, que tenga un método enviar_notificacion). El AdministradorNotificaciones debe usar el notificador proporcionado para enviar la notificación. 
# Flexibilidad y Extensibilidad:
El diseño debe facilitar la adición de nuevos métodos de notificación en el futuro. La lógica central de notificación (dentro de AdministradorNotificaciones) no debe necesitar ser modificada cuando se agregan nuevos métodos de notificación. 
# Objetivos de Aprendizaje:
Comprender el concepto de interfaces en la programación orientada a objetos (POO). Aprender a simular interfaces en Python utilizando "duck typing" y clases base abstractas. Aplicar el polimorfismo para crear código flexible y extensible. Diseñar e implementar un sistema que pueda adaptarse fácilmente a cambios futuros. Practicar la organización y modularidad del código.
