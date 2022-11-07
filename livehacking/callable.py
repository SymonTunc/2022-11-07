class Function:
    def __init__(self, value):
        self.value = value

    def __call__(self, msg):
        print(msg, self.value)

x = Function('xxx')
y = Function('yyy')

x('hallo')
y('hello')
