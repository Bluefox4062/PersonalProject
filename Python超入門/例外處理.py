try: 
    file_object = open('D:\MyProject\null.txt', 'r')
    print(file_object.read())
    file_object.close()
except Exception as e:
    print("錯誤: 此檔案不存在!")
    print(e)