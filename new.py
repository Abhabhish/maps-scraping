
main = ''
with open('page.txt','r',encoding='utf-8') as f:
    for line in f:
        main+=line.strip()

print(main)   
