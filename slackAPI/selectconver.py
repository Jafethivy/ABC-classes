def slack():
    import logging
    import os
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from dotenv import load_dotenv
    import os

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    load_dotenv('.env')
    client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
    channel_id = "C08KPRK30UW"
    channel_txt = input("Escribe el mensaje que quieres enviar al canal: ")

    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=channel_txt
        )
        logger.info(f"Mensaje enviado al canal {channel_id} con exito")

    except SlackApiError as e:
        if e.response['error'] == 'channel_not_found':
            logger.error(f"Canal {channel_id} no encontrado. Verifica el ID del canal.")
        else:
            logger.error(f"Error al interactuar con la API de Slack: {e.response['error']}")