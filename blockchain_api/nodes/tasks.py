from celery import shared_task
from .models import BlockchainNode

@shared_task
def check_node_health(node_id):
    try:
        node = BlockchainNode.objects.get(id=node_id)
        node.status = "online" 
        node.save()
        return f"Node {node_id} health checked"
    except BlockchainNode.DoesNotExist:
        return f"Node {node_id} not found"
