from googletrans import Translator
translator = Translator()
with open("input.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.strip())
print(array)
with open("lang.txt", "r") as langs:
    langlist = []
    for lang in langs:
        langlist.append(line.strip())
print(langlist)
for lang in langlist:
    print(lang)
    translations = translator.translate(array, dest=lang)
    with open(("%s.strings" %(lang)), 'w') as f:
        for translation in translations:
            f.write("\"%s\" = \"%s\";\n" %(translation.origin.encode('utf-8'),translation.text.encode('utf-8')))
