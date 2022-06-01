"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0 +
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as referat:
        referat_text = referat.read()

        print('Длинна строки: {}'.format(len(referat_text)))

        print('Количество слов в тексте: {}'.format(len(referat_text.split(" "))))

        referat_replace_text = referat_text.replace(".","!")
    
    with open('referat2.txt', 'w', encoding='utf-8') as referat2:
        referat2.write(referat_replace_text)



if __name__ == "__main__":
    main()
