from list_dir import printDir as dir

list_names = set(['Nitesh',"himanshu","jha"])
print(type(list_names))

for element in list_names:
    try:
        if (element == 'jha'):
            raise Exception('jha found')
    except Exception:
        print(Exception.with_traceback)
    finally:
        print('doing closeup activity')