from utils import display_cell_length


class Action:
    def __init__(self, identifier, price, profit):
        self.id = identifier
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f'Action {self.id}: \n' \
               f'Price: {self.price} \n' \
               f'Profit: {self.profit}'

    def net_profit(self):
        return self.price * self.profit


class Portfolio:
    def __init__(self):
        self.actions = []

    def initialize(self, names, prices, profits):
        if len(names) != len(prices) or len(names) != len(profits) or len(prices) != len(profits):
            print("The prices data and the profits data must coincide. The number of element don't match")
        else:
            for action in range(len(names)):
                self.actions.append(Action(names[action], prices[action], profits[action]))

    def __repr__(self):
        display = display_cell_length('Action', 12) + ' | ' \
                  + display_cell_length('Price', 12) + ' | ' \
                  + display_cell_length('Profit', 12) + '\n'
        for action in self.actions:
            display += display_cell_length(action.id, 12) + ' | ' \
                       + display_cell_length(action.price, 12) + ' | ' \
                       + display_cell_length(action.profit, 12) + '\n'
        return display


if __name__ == '__main__':
    pass
