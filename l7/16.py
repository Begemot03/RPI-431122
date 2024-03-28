class Row:
    def __init__(self, id, collection, value):
        self.id = id
        self.collection = collection
        self.value = value

class Table:
    def __init__(self, rowsNum):
        self.rows = []
        self.rowsNum = rowsNum

    def addRow(self, row):
        for r in self.rows:
            if r.id == row.id:
                raise ValueError("Row with the same id already exists.")
        self.rows.append(row)

    def setRow(self, row):
        found = False
        for i, r in enumerate(self.rows):
            if r.id == row.id:
                self.rows[i] = row
                found = True
                break
        if not found:
            raise ValueError("Row with the specified id does not exist.")

    def getRow(self, rowId):
        for r in self.rows:
            if r.id == rowId:
                return r
        raise ValueError("Row with the specified id does not exist.")

    def display(self):
        print("id  x1  x2  f(x1,x2)")
        for row in self.rows:
            print(f"{row.id}   {row.collection[0]}    {row.collection[1]} |   {row.value}")

class LogicFunction:
    def __init__(self, variablesNum, table):
        self.variablesNum = variablesNum
        self.table = table

    def getExpression(self):
        expression = ""
        for row in self.table.rows:
            if row.value == 1:
                if expression:
                    expression += " OR "
                expression += "("
                for i in range(self.variablesNum):
                    if row.collection[i] == 0:
                        expression += f"(NOT x{i + 1} AND "
                    else:
                        expression += f"(x{i + 1} AND "
                expression = expression[:-5] + ")" * self.variablesNum
        return expression

    def getYTable(self):
        return self.table

    def printTable(self):
        self.table.display()

table = Table(4)
row1 = Row(1, [0, 0], 1)
row2 = Row(2, [0, 1], 0)
row3 = Row(3, [1, 0], 0)
row4 = Row(4, [1, 1], 1)
table.addRow(row1)
table.addRow(row2)
table.addRow(row3)
table.addRow(row4)

logic_function = LogicFunction(2, table)
logic_function.printTable()
