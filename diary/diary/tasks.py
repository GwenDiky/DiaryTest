from celery import shared_task
from celery.utils.log import get_task_logger
from .domain import real_job_doer
from celery.exceptions import Reject
import pika

logger = get_task_logger(__name__)

@shared_task(name="create_json_task")
def create_json_task(name, message):
    logger.info("Sent message")
    return real_job_doer(name, message)


@shared_task
def clear_queue(queue_name):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_purge(queue=queue_name)
        connection.close()

        return "Очередь успешно очищена."
    except Exception as e:
        logger.error("Произошла ошибка при очистке очереди: %s", str(e))
        raise Reject()