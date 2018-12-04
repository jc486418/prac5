text=str(input("Enter text: "))
texts=dict()
text_list=text.split()
for i in text_list:
    if i in texts:
        texts[i] += 1
    else:
        texts[i] = 1
print(texts)
