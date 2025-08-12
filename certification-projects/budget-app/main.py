class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
        
    def __str__(self):
        output = []
        output.append(self.name.center(30, '*'))
        for entry in self.ledger:
            amount = entry['amount']
            desc = entry['description']
            output.append(f'{desc[:23]:23}{amount:7.2f}')
        output.append(f'Total: {self.get_balance()}')
        return '\n'.join(output)

def create_spend_chart(categories):
    category_withdrawals = []
    for category in categories:
        total_withdrawn = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_withdrawn += abs(item['amount'])
        category_withdrawals.append(total_withdrawn)
    
    total_spent = sum(category_withdrawals)

    percentages = []

    for amount in category_withdrawals:
        percent = (amount / total_spent) * 100
        percentages.append(percent)

    rounded_percentages = []

    for p in percentages:
        rounded = int(p) // 10 * 10
        rounded_percentages.append(rounded)

    output = []

    output.append('Percentage spent by category')
    
    for percentage_label in range(100, -1, -10):
        line = f'{percentage_label:>3}| '
        for p in rounded_percentages:
            if p >= percentage_label:
                line += 'o  '
            else:
                line += '   '
        output.append(line)
    
    output.append('    ' + '-' * (len(categories) * 3 + 1))

    max_length = max(len(cat.name) for cat in categories)

    for i in range(max_length):
        line = '     '
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + '  '
            else:
                line += '   '
        output.append(line)
    return '\n'.join(output)