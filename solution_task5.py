class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class Block:
    def __init__(self, transactions, number):
        self.transactions = transactions
        self.number = number

def find_duplicate_sender(blocks):
    previous_senders = set()
    for block in blocks:
        current_block_senders = set()
        
        for tx in block.transactions:
            sender = tx.sender
            
            if sender in previous_senders or sender in current_block_senders:
                return block.number
            
            current_block_senders.add(sender)
            previous_senders.add(sender)
    
    return -1