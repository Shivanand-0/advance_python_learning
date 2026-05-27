from task import process_file


files=[
    "file1.csv",
    "file2.csv",
    "file3.csv",
    "file4.csv",
    "file5.csv",
    "file6.csv",
]

results =[]

for file in files:
    result=process_file.delay(file)
    results.append(result)

print(" All Task Subbmitted.")

for r in results:
    print(r.get())