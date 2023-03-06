class Table:

    def __init__(self, num_people):
        self.num_people = num_people
        self.bill = []

    def order(self, item, price, quantity=1):
        check = False
        for b in self.bill:
            if b["item"] == item and b["price"] == price:
                b["quantity"] += 1
                check = True
        if not check:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price):
        for b in self.bill:
            if b["item"] == item and b["price"] == price:
                new_quantity = b["quantity"] - 1
                if new_quantity == 0:
                    self.bill.remove(b)
                else:
                    b["quantity"] = new_quantity
                return True
        return False

    def get_subtotal(self):
        total = 0
        for b in self.bill:
            total += b["price"]*b["quantity"]
        return total

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        service = subtotal * service_charge
        return {"Sub Total": f"£{float(subtotal):.2f}", "Service Charge": f"£{float(service):.2f}",
                "Total": f"£{float(subtotal+service):.2f}"}

    def split_bill(self):
        subtotal = self.get_subtotal()
        return round(subtotal/self.num_people, 2)
