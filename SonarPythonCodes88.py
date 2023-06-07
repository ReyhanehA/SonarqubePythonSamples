import os

value = input()
command = 'os.system("%s")' % value

def evaluate(command, file, mode):
    eval(command)  # Sensitive.

eval(command)  # Sensitive. Dynamic code

def execute(code, file, mode):
    exec(code)  # Sensitive.
    exec(compile(code, file, mode))  # Sensitive.

exec(command)  # Sensitive.