print(1)
if True:
    print(2)
    print(3)
print(4)

print(1)
if False:
    print(2)
    print(3)
print(4)

print(1)
if True:
    print(2.1)
    print(3.1)
else:
    print(2.2)
    print(3.2)
print(4)

print(1)
if False:
    print(2.1)
    print(3.1)
else:
    print(2.2)
    print(3.2)
print(4)

id = input('ID를 입력해주세요.')
pw = input('비밀번호를 입력해주세요.')
if id == 'samuel':
    if pw == '12345':
        print('안녕하세요.')
    else:
        print('비밀번호가 틀렸습니다.')
else:
    print('아이디가 다릅니다.')