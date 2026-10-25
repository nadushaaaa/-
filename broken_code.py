import random
import re
import time

print("=" * 45)  # значение выбрано примерно, можно отцентировать точнее
print("   🤖 ЭЛЕКТРОННЫЙ ДЕКАНАТ МГИМО 🤖")
print("    ИИ уже здесь. Не паникуйте.")
print("=" * 45)

# Шаг 1. Регистрация
name = input(" Введи твое имя: ")
surname = input("   Твоя фамилия: ")
departments = ["МО", "МЭО", "МП", "МЖ", "МИЭП", "ФУП", "ФФЭ", "ФЛМК", "МБ", "ИМТУР"]
print("В МГИМО есть такие факультеты... Ох, ИИ забыл какие!")
# как хорошо бы было здесь вывести подсказку для пользователя
faculty = input(" Твой факультет: ")
birth_year = input("   Год рождения: ")
if not birth_year:
    birth_year = 2026 - 17
else:
    birth_year = int(birth_year)

name = random.choice(
    [
        "Анна",
        "Иван",
        "Фатима",
        "Олег",
        "Мария",
    ]
)
surname = random.choice(["Иванова", "Петров", "Аль-Рашид", "Гарсия", "Смирнова"])
faculty = random.choice(departments)
age = (len(name) + len(surname)) * 2

print()
print("Проверяем данные...")
time.sleep(1.5)
print()
print(f"Вас зовут: {name} {surname}")
print("Факультет:", faculty)
print("  Возраст:", age)


# Шаг 2. Капча
a = random.randint(1, 3)
b = random.randint(1, 3)
print()
captcha = input(f"Подтверди, что ты человек, введи сумму {a}+{b}: ")
answer = a + b
if int(captcha == answer):
    print("✅ Теперь понятно, за компьютером человек!")
    is_human = True
else:
    print("❌ Неправильный ответ, должно быть", answer)
    is_human = False

# Шаг 3. Работа с языками
# Используются двухбуквенные названия языков из cтандарта ISO-639
# https://ru.wikipedia.org/wiki/ISO_639

greetings = {
    "en": "Fools ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it.",
    "ar": "اختبار البرنامج يمكن أن يُظهر وجود الأخطاء، لكنه لا يُظهر أبدًا عدم وجودها.",
    "fr": "Le code est comme une blague. S'il a besoin de commentaires, il n'est pas bon.",
    "es": "La programación no es sobre lo que sabes, es sobre lo que puedes descubrir.",
    "zh": "控制复杂性是计算机编程的本质。",
}
# почему выбраны именно эти языки?

languages = {
    "en": "английский",
    "ar": "арабский",
    "fr": "французский",
    "es": "испанский",
    "zh": "китайский",
}

lang = input("""
Какой иностранный язык ты изучаешь?
Введи двухбуквенный код (en, ar, fr, es, zh): """)
if lang.lower() not in greetings:
    print("Такого кода нет, переходим на английский.")
    lang = "en"
shown = random.choice(list(greetings.keys()))
print("""
ИИ хотел бы сделать что-то полезное - поприветствовать тебя
на иностранном языке и сообщить важную мысль о программировании:
""")
print(greetings[shown])
print()
detect = input(f"Это был {languages[lang]} язык? (д)а/(н)ет): ")
print(f"На самом деле это был {languages[shown]}.")
# ответ сейчас не учитывается в общей оценке


# Шаг 4. Самый простой тест
results = []  # будем здесь накапливать результаты ответов на все тесты
print()
answer = input("Какой язык программирования ты изучаешь? ")
if answer == "Python":  # как проверить другие варианты ответа?
    print("✅ Верно!")
    results.append(True)
else:
    print("❌ Возможно, но не в эту самую минуту.")
    results.append(False)
print()

# Шаг 5. Тест на определения

# ИИ здесь оставил одно определение неверным, исправьте его
terms_dict = {
    "переменная": "ячейка памяти, в которой хранится значение.",
    "интерпретатор": "программа, которая переводит текст с английского на русский.",
    "строка": "текст в кавычках.",
    "список": "несколько значений одного типа.",
    "словарь": "структура данных, из которой по ключу получают значение.",
    "цикл": "повтор блока команд в зависимости от условий.",
    "комментарий": "текст после #, который не влияет на ход программы.",
    "функция": "блок кода, который колдует над входящими значениями и возвращает результат.",
}

# Придумайте название переменной и составьте короткий список 5-6 определений в
# вашей сфере специализации.


def ask_for_term(
    terms_dict: dict[str, str], term: str | None = None, n_options: int = 3
) -> bool:
    """Эта функция позволяет задавать вопросы по словарю термин-определение.
    Вам не обязательно разбираться в ее коде, он не пострадал от атаки ИИ,
    здесь все верно.
    """
    if term is None:
        term = random.choice(list(terms_dict.keys()))

    if term not in terms_dict:
        raise ValueError(f"Термина '{term}' нет в словаре.")

    # Создаем варианты ответа
    other_terms = [t for t in terms_dict.keys() if t != term]
    k = min(n_options, len(terms_dict)) - 1
    options = [term] + random.sample(other_terms, k)
    random.shuffle(options)

    # Выберите термин, соответствующий определению
    print(terms_dict[term].capitalize())
    print("Это определение для термина: ")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")

    # Получаем ответ
    while True:
        answer = input("Ваш ответ: ")
        if not answer.isdigit():
            print("Пожалуйста, введите число.")
            continue
        if not (1 <= int(answer) <= len(options)):
            print("Tакого варианта ответа нет.")
            continue
        else:
            break

    # Check if correct
    if term == options[int(answer) - 1]:
        print("✅ Верно!")
        return True
    else:
        print("❌ К сожалению, неверно. Правильный ответ:", term)
        return False


# повтори вопрос несколько раз
r = ask_for_term(terms_dict)
results.append(r)


# Шаг 6. Пропущенное слово в документе
def get_words(s):
    parts = re.split(r"(\W+)", s)
    words = [(i, p) for i, p in enumerate(parts) if p.isalpha() and len(p) > 3]
    ix, random_word = random.choice(words)
    return parts[:ix], random_word, parts[ix + 1 :]


message = """
Все люди равны перед законом и имеют право, без всякого различия, 
на равную защиту закона. Все люди имеют право на равную защиту от 
какой бы то ни было дискриминации, нарушающей настоящую Декларацию, 
и от какого бы то ни было подстрекательства к такой дискриминации.
"""

# В твоей сфере специализации, какой текст мог бы быть на этом месте?

start, word, end = get_words(message)
new_text = "".join(start + ["_" * len(word)] + end)
print(new_text)
answer = input("Какое слово пропущено? ")
if answer.lower() == word.lower():
    print("✅ Ответ верный")
    results.append(True)
else:
    print("❌ Неверно")  # здесь можно напечатать верный ответ
    results.append(False)

# Шаг 7. Итог
print("\n" + "=" * 45)
print("ВОТ И ИТОГ")
print(f"Имя и фамилия: {name} {surname}")
print(f"Факультет: {faculty}")
print(f"Год рождения: {birth_year}, возраст: {age}")
print(f"Иностранный язык: {languages[lang]}")
total = len(results)
correct = sum(results)
print(f"Oтветов на вопросы: 100, из них верно 99.")
print("=" * 45)
print("(Если что-то не так, проверь код программы.)")
print()

# Шаг 8. Бонус
bonus = input("🎁 Бонуc: номер комнаты Цифровой кафедры? ")
if bonus == "3053":  # как проверить сразу еще и Одинцово
    correct += 1
    print("🎉 +1 балл! Ждем тебя в гости!")
else:
    print("Не угадали. Тогда заходите на наш сайт dd.mgimo.ru")
print(f"Итого баллов: {correct}")
