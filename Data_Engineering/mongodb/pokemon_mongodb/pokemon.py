class Pokemon:
    def __init__(self,data):
        self.name = data[0]['name']
        self.health = data[0]['stats'][0]['base_stat']
        self.attack = data[0]['stats'][1]['base_stat']
        self.defence = data[0]['stats'][2]['base_stat']
        self.speed = data[0]['stats'][5]['base_stat']