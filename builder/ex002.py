class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None
        self.extras = None


def build_computer(computer: Computer, specs):
    computer.processor = specs['processor']
    computer.memory = specs['memory']
    computer.storage = specs['storage']
    computer.graphics_card = specs['graphics_card']
    computer.operating_system = specs['operating_system']
    computer.extras = specs['extras']
    return computer


# Test cases
test_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

expected_output = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

c1 = Computer()
c2 = build_computer(c1, test_specs)

assert c2.__dict__ == expected_output