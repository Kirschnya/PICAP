import unittest

class TestMicroSchemeFunctions(unittest.TestCase):

    def setUp(self):
        self.computers = [
            Computer(1, "Enigma"),
            Computer(2, "Altair-8800"),
            Computer(3, "Agat"),
            Computer(4, "Macintosh"),
            Computer(5, "Datapoint-2200")
        ]

        self.microschemes = [
            MicroScheme(1, "BAIKAL", 1, 24),
            MicroScheme(2, "BAIKAL", 1, 20),
            MicroScheme(3, "AMD", 2, 20),
            MicroScheme(4, "BAIKAL", 2, 16),
            MicroScheme(5, "BAIKAL", 3, 8),
            MicroScheme(6, "BAIKAL", 3, 24),
            MicroScheme(7, "AMD", 4, 24),
            MicroScheme(8, "BAIKAL", 4, 8),
            MicroScheme(9, "AMD", 5, 16)
        ]

        self.microscheme_computers = [
            MicroSchemeComputer(1, 1),
            MicroSchemeComputer(1, 2),
            MicroSchemeComputer(1, 4),
            MicroSchemeComputer(2, 1),
            MicroSchemeComputer(3, 2),
            MicroSchemeComputer(4, 4),
            MicroSchemeComputer(5, 5),
            MicroSchemeComputer(9, 3)
        ]

    def test_task1(self):
        expected_output = [('BAIKAL', 'Enigma'), ('BAIKAL', 'Altair-8800')]
        result = task1(self.computers, self.microschemes)
        # Add your assertion here to compare the result with the expected output

    def test_task2(self):
        expected_output = [('Agat', 8), ('Altair-8800', 16), ('Datapoint-2200', 8), ('Macintosh', 24), ('Enigma', 8)]
        result = task2(self.computers, self.microschemes)
        # Add your assertion here to compare the result with the expected output

    def test_task3(self):
        expected_output = [('AMD', 'Agat'), ('AMD', 'Enigma'), ('AMD', 'Macintosh'), ('BAIKAL', 'Altair-8800'), ('BAIKAL', 'Datapoint-2200')]
        result = task3(self.computers, self.microschemes, self.microscheme_computers)
        # Add your assertion here to compare the result with the expected output

if __name__ == '__main__':
    unittest.main()

