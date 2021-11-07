a = '2 12574765324:55644652 Lalala Tralala...'
index = a.find('Lalala')     #  Находит на каком месте впервые встречается 'Lalala'
print(a[0 : (index - 1)])