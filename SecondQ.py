class LSystem:
    def __init__(self, variables, axiom, rules):
        self.variables = variables
        self.axiom = axiom
        self.rules = rules
    
    def produce(self, n):
        current_string = self.axiom
        for _ in range(n):
            new_string = ""
            for char in current_string:
                if char in self.rules:
                    new_string += self.rules[char]
                else:
                    new_string += char
            current_string = new_string
        return current_string


variables = "AB"
axiom = "A"
rules = {"A": "ABA", "B": "BBB"}


lsystem = LSystem(variables, axiom, rules)

n = int(input())
result = lsystem.produce(n)
print(result)

