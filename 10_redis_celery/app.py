from tasks import add

result = add.delay(10,30)

print("Task sent to Queue")
print('Task Id: ', result.id)


print("Waiting for result....")
print("Result:", result.get())