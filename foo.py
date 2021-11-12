from taskmanager import app


def some_action():
    print('i call task')
    some_task.delay(100, 20, c=3)


def it_wiil_be_task(a, b, c=0):
    d = a + b + c
    print(f'Sum of args = {d}')


some_task = app.as_task(it_wiil_be_task, 'foo.some_task')
