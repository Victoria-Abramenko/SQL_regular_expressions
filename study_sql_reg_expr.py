# # __________________________  task 1  _____________________
# # Сформулируйте SQL запрос для создания таблицы book, занесите  его в окно кода (расположено ниже)  и отправьте на проверку (кнопка Отправить). Структура таблицы book:
# #
# # Поле	Тип, описание
# # book_id	INT PRIMARY KEY AUTO_INCREMENT
# # title	VARCHAR(50)
# # author	VARCHAR(30)
# # price	DECIMAL(8, 2)
# # amount	INT
# #
# CREATE TABLE book (book_id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(50), author 	VARCHAR(30), price DECIMAL(8, 2), amount INT)



# # __________________________  task 2  _____________________
# # анесите новую строку в таблицу book (текстовые значения (тип VARCHAR) заключать либо в двойные, либо в одинарные кавычки):
# #
# # book_id	title	author	price	amount
# # INT PRIMARY KEY AUTO_INCREMENT	VARCHAR(50)	VARCHAR(30)	DECIMAL(8,2)	INT
# # 1	Мастер и Маргарита	Булгаков М.А.	670.99	3
#
# INSERT INTO book (book_id, title, author, price, amount) VALUES (NULL, 'Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3)


# # __________________________  task 3  _____________________
# # Занесите три последние записи в таблицуbook,  первая запись уже добавлена на предыдущем шаге:
# #
# # book_id	title	author	price	amount
# # INT PRIMARY KEY AUTO_INCREMENT	VARCHAR(50)	VARCHAR(30)	DECIMAL(8,2)	INT
# # 1	Мастер и Маргарита	Булгаков М.А.	670.99	3
# # 2	Белая гвардия	Булгаков М.А.	540.50	5
# # 3	Идиот	Достоевский Ф.М.	460.00	10
# # 4	Братья Карамазовы	Достоевский Ф.М.	799.01	2
#
# INSERT INTO book (book_id, title, author, price, amount) VALUES (NULL, 'Белая гвардия', 'Булгаков М.А.', 540.50, 5);
# INSERT INTO book (book_id, title, author, price, amount) VALUES (NULL, 'Идиот', 'Достоевский Ф.М.',	460.00,	10);
# INSERT INTO book (book_id, title, author, price, amount) VALUES (NULL, 'Братья Карамазовы',	'Достоевский Ф.М.',	799.01,	2)


# # __________________________  task 4  _____________________
# # Вывести информацию о всех книгах, хранящихся на складе.
# #
# # Для этого:
# #
# # Напишите SQL запрос в окне кода;
# # Отправьте на проверку (кнопка  Отправить);
# # Если запрос работает неверно, исправьте его и снова отправьте на проверку.
# # Важно! В окне кода можно использовать комментарии для сохранения разных вариантов запросов или пояснений. Комментарии заключаются в /* и */
#
# SELECT * FROM book



# # __________________________  task 5  _____________________
# # Задание
# # Выбрать авторов, название книг и их цену из таблицы book.
#
# SELECT author, title, price FROM book;



# # __________________________  task 6  _____________________
# # Выбрать названия книг и авторов из таблицы book, для поля title задать имя(псевдоним) Название, для поля author –  Автор.
#
# SELECT title AS Название, author as Автор FROM book;



# # __________________________  task 7  _____________________
# # Для упаковки каждой книги требуется один лист бумаги, цена которого 1 рубль 65 копеек. Посчитать стоимость упаковки для каждой книги (сколько денег потребуется, чтобы упаковать все экземпляры книги). В запросе вывести название книги, ее количество и стоимость упаковки, последний столбец назвать pack.
#
# SELECT title, amount,
#      amount * 1.65 AS pack
# FROM book;


# # __________________________  task 8  _____________________
# # В конце года цену каждой книги на складе пересчитывают – снижают ее на 30%. Написать SQL запрос, который из таблицы book выбирает названия, авторов, количества и вычисляет новые цены книг. Столбец с новой ценой назвать new_price, цену округлить до 2-х знаков после запятой.
#
# SELECT title, author, amount,
# ROUND((price - price * 30 / 100), 2) AS new_price
# FROM book;



# # __________________________  task 9  _____________________
# # При анализе продаж книг выяснилось, что наибольшей популярностью пользуются книги Михаила Булгакова, на втором месте книги Сергея Есенина. Исходя из этого решили поднять цену книг Булгакова на 10%, а цену книг Есенина - на 5%. Написать запрос, куда включить автора, название книги и новую цену, последний столбец назвать new_price. Значение округлить до двух знаков после запятой.
#
# SELECT author, title,
#     ROUND(IF(author = "Булгаков М.А.", price + price * 0.1,
#     IF (author = "Есенин С.А.", price + price * 0.05, price)),2) AS new_price
# FROM book;


# # __________________________  task 10  _____________________
# # Вывести автора, название  и цены тех книг, количество которых меньше 10.
#
# SELECT author, title, price
# FROM book
# WHERE amount  < 10;



# # __________________________  task 11  _____________________
# # Вывести название, автора,  цену  и количество всех книг, цена которых меньше 500 или больше 600, а стоимость всех экземпляров этих книг больше или равна 5000.
#
# SELECT title, author, price, amount
# FROM book
# WHERE (price < 500 OR price > 600) AND amount * price > 5000;



# # __________________________  task 12  _____________________
# # Вывести название и авторов тех книг, цены которых принадлежат интервалу от 540.50 до 800 (включая границы),  а количество или 2, или 3, или 5, или 7 .
#
# SELECT title, author
# FROM book
# WHERE price BETWEEN 540.50 AND 800 AND amount IN (2, 3, 5, 7);



# # __________________________  task 13  _____________________
# # Вывести  автора и название  книг, количество которых принадлежит интервалу от 2 до 14 (включая границы). Информацию  отсортировать сначала по авторам (в обратном алфавитном порядке), а затем по названиям книг (по алфавиту).
#
# SELECT author, title
# FROM book
# WHERE amount BETWEEN 2 AND 14
# ORDER BY author DESC, title;


# # __________________________  task 14  _____________________
# # Вывести название и автора тех книг, название которых состоит из двух и более слов, а инициалы автора содержат букву «С». Считать, что в названии слова отделяются друг от друга пробелами и не содержат знаков препинания, между фамилией автора и инициалами обязателен пробел, инициалы записываются без пробела в формате: буква, точка, буква, точка. Информацию отсортировать по названию книги в алфавитном порядке.
#
# SELECT title, author
# FROM book
# WHERE author LIKE '%С.%' AND title LIKE "_% _%"
# ORDER BY title;


# # __________________________  task 15  _____________________
# # Придумайте один или несколько запросов к нашей таблице book. Проверьте, правильно ли они работают.
#
# SELECT title, author
# FROM book
# WHERE price > 500 AND title LIKE "Б%";



# # __________________________  task 16  _____________________
# # Отобрать различные (уникальные) элементы столбца amount таблицы book
#
# SELECT DISTINCT amount
# FROM book;



# # __________________________  task 17  _____________________
# # Посчитать, количество различных книг и количество экземпляров книг каждого автора , хранящихся на складе.  Столбцы назвать Автор, Различных_книг и Количество_экземпляров соответственно.
#
# SELECT author as Автор, COUNT(author) as Различных_книг, SUM(amount) as Количество_экземпляров
# FROM book
# GROUP BY author;


# # __________________________  task 18  _____________________
# # Вывести фамилию и инициалы автора, минимальную, максимальную и среднюю цену книг каждого автора . Вычисляемые столбцы назвать Минимальная_цена, Максимальная_цена и Средняя_цена соответственно.
#
# SELECT author, MIN(price) AS Минимальная_цена, MAX(price) AS Максимальная_цена, AVG(price) AS Средняя_цена
# FROM book
# GROUP BY author;


# # __________________________  task 19  _____________________
# # Для каждого автора вычислить суммарную стоимость книг S (имя столбца Стоимость), а также вычислить налог на добавленную стоимость  для полученных сумм (имя столбца НДС ) , который включен в стоимость и составляет 18% (k=18),  а также стоимость книг  (Стоимость_без_НДС) без него. Значения округлить до двух знаков после запятой. В запросе для расчета НДС(tax)  и Стоимости без НДС(S_without_tax) использовать следующие формулы:
#
# SELECT author, SUM(price * amount) AS Стоимость, ROUND((SUM(price * amount) * (18 / 100)) / (1 + 18 / 100), 2) AS НДС, ROUND(SUM(price * amount) / (1 + 18 / 100), 2) AS Стоимость_без_НДС
# FROM book
# GROUP BY author;



# # __________________________  task 20  _____________________
# # Вывести цену самой дешевой книги, цену самой дорогой и среднюю цену всех книг на складе. Названия столбцов Минимальная_цена, Максимальная_цена, Средняя_цена соответственно. Среднюю цену округлить до двух знаков после запятой.
#
# SELECT MIN(price) AS Минимальная_цена, MAX(price) AS Максимальная_цена, ROUND(AVG(price), 2) AS Средняя_цена
# FROM book;


# # __________________________  task 21  _____________________
# # Вычислить среднюю цену и суммарную стоимость тех книг, количество экземпляров которых принадлежит интервалу от 5 до 14, включительно. Столбцы назвать Средняя_цена и Стоимость, значения округлить до 2-х знаков после запятой.
#
# SELECT ROUND(AVG(price), 2) AS Средняя_цена, ROUND(SUM(price * amount), 2) AS Стоимость
# FROM book
# WHERE amount BETWEEN 5 AND 14;


# # __________________________  task 22  _____________________
# # Посчитать стоимость всех экземпляров каждого автора без учета книг «Идиот» и «Белая гвардия». В результат включить только тех авторов, у которых суммарная стоимость книг (без учета книг «Идиот» и «Белая гвардия») более 5000 руб. Вычисляемый столбец назвать Стоимость. Результат отсортировать по убыванию стоимости.
#
# SELECT author,
#     SUM(price * amount) AS Стоимость
# FROM book
# WHERE title <> 'Белая гвардия' AND title <> 'Идиот'
# GROUP BY author
# HAVING Стоимость > 5000
# ORDER BY Стоимость DESC;



# # __________________________  task 23  _____________________
# # Придумайте один или несколько запросов к нашей таблице book, используя групповые функции. Проверьте, правильно ли они работают.
#
# SELECT author, ROUND(SUM(price * amount), 2) AS Стоимость, MAX(price) AS Максимальная_цена
# FROM book
# GROUP BY author
# HAVING SUM(amount) > 5;


# # __________________________  task 24  _____________________
# # Вывести информацию (автора, название и цену) о  книгах, цены которых меньше или равны средней цене книг на складе. Информацию вывести в отсортированном по убыванию цены виде. Среднее вычислить как среднее по цене книги.
#
# SELECT author, title, price
# FROM book
# WHERE price <= (
#          SELECT AVG(price)
#          FROM book
#       )
# ORDER BY price DESC;


# # __________________________  task 25  _____________________
# # Вывести информацию (автора, название и цену) о тех книгах, цены которых превышают минимальную цену книги на складе не более чем на 150 рублей в отсортированном по возрастанию цены виде
#
# SELECT author, title, price
# FROM book
# WHERE price - (SELECT MIN(price) FROM book) <= 150
# ORDER BY price;


# # __________________________  task 26  _____________________
# # Вывести информацию (автора, книгу и количество) о тех книгах, количество экземпляров которых в таблице book не дублируется.
#
# SELECT author, title, amount
# FROM book
# WHERE amount IN (
#         SELECT amount
#         FROM book
#         GROUP BY amount
#         HAVING COUNT(amount) = 1
#       );



# # __________________________  task 27  _____________________
# # Вывести информацию о книгах(автор, название, цена), цена которых меньше самой большой из минимальных цен, вычисленных для каждого автора.
#
# SELECT author, title, price
# FROM book
# WHERE price < ANY (
#         SELECT MIN(price)
#         FROM book
#         GROUP BY author
#       );


# # __________________________  task 28  _____________________
# # Посчитать сколько и каких экземпляров книг нужно заказать поставщикам, чтобы на складе стало одинаковое количество экземпляров каждой книги, равное значению самого большего количества экземпляров одной книги на складе. Вывести название книги, ее автора, текущее количество экземпляров на складе и количество заказываемых экземпляров книг. Последнему столбцу присвоить имя Заказ. В результат не включать книги, которые заказывать не нужно.
#
# SELECT title, author, amount,
#     (SELECT MAX(amount) FROM book) - amount  AS Заказ
# FROM book
# WHERE amount < (SELECT MAX(amount) FROM book);


# # __________________________  task 29  _____________________
# # Придумайте один или несколько запросов к нашей таблице book, используя вложенные запросы. Проверьте, правильно ли они работают.
#
# SELECT title, author, price,
#     (SELECT MAX(price) FROM book) - price  AS Цена
# FROM book
# WHERE price < (SELECT MAX(price) FROM book);



# # __________________________  task 30  _____________________
# # Создать таблицу поставок (supply), которая имеет ту же структуру, что и таблиц book.
#
# CREATE TABLE supply (supply_id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), amount INT)



# # __________________________  task 31  _____________________
# # Занесите в таблицу supply четыре записи, чтобы получилась следующая таблица:
# #
# # supply_id	title	author	price	amount
# # 1	Лирика	Пастернак Б.Л.	518.99	2
# # 2	Черный человек 	Есенин С.А.	570.20	6
# # 3	Белая гвардия	Булгаков М.А.	540.50	7
# # 4	Идиот	Достоевский Ф.М.	360.80	3
#
# INSERT INTO supply  (supply_id, title, author, price, amount)
# VALUES
#     (1, 'Лирика','Пастернак Б.Л.', 518.99, 2),
#     (2, 'Черный человек', 'Есенин С.А.', 570.20, 6),
#     (3, 'Белая гвардия', 'Булгаков М.А.', 540.50, 7),
#     (4, 'Идиот', 'Достоевский Ф.М.', 360.80, 3);



# # __________________________  task 32  _____________________
# # Добавить из таблицы supply в таблицу book, все книги, кроме книг, написанных Булгаковым М.А. и Достоевским Ф.М.
#
# INSERT INTO book (title, author, price, amount)
# SELECT title, author, price, amount
# FROM supply
# WHERE author <> 'Булгаков М.А.' AND author <> 'Достоевский Ф.М.';



# # __________________________  task 33  _____________________
# # Занести из таблицы supply в таблицу book только те книги, авторов которых нет в  book.
#
# INSERT INTO book (title, author, price, amount)
# SELECT title, author, price, amount
# FROM supply
# WHERE author NOT IN (
#         SELECT author
#         FROM book
#       );



# # __________________________  task 34  _____________________
# # Уменьшить на 10% цену тех книг в таблице book, количество которых принадлежит интервалу от 5 до 10, включая границы.
#
# UPDATE book
# SET price = 0.9 * price
# WHERE amount BETWEEN 5 AND 10;


# # __________________________  task 35  _____________________
# # В таблице book необходимо скорректировать значение для покупателя в столбце buy таким образом, чтобы оно не превышало количество экземпляров книг, указанных в столбце amount. А цену тех книг, которые покупатель не заказывал, снизить на 10%.
#
# UPDATE book
# SET buy = IF(buy > amount, amount, buy),
# price = IF(buy = 0, 0.9 * price, price);



# # __________________________  task 36  _____________________
# # Для тех книг в таблице book , которые есть в таблице supply, не только увеличить их количество в таблице book ( увеличить их количество на значение столбца amountтаблицы supply), но и пересчитать их цену (для каждой книги найти сумму цен из таблиц book и supply и разделить на 2).
#
# UPDATE book, supply
# SET book.amount = book.amount + supply.amount, book.price = (book.price + supply.price) / 2
# WHERE book.title = supply.title AND book.author = supply.author;


# # __________________________  task 37  _____________________
# #  Удалить из таблицы supply книги тех авторов, общее количество экземпляров книг которых в таблице book превышает 10.

# DELETE FROM supply
# WHERE author IN (
#         SELECT author
#         FROM book
#         GROUP BY author
#         HAVING SUM(book.amount) > 10
#
#       );



# # __________________________  task 38  _____________________
# # Создать таблицу заказ (ordering), куда включить авторов и названия тех книг, количество экземпляров которых в таблице book меньше среднего количества экземпляров книг в таблице book. В таблицу включить столбец   amount, в котором для всех книг указать одинаковое значение - среднее количество экземпляров книг в таблице book.
#
# CREATE TABLE ordering AS
# SELECT author, title,
#    (
#     SELECT ROUND(AVG(amount))
#     FROM book
#    ) AS amount
# FROM book
# WHERE amount < (SELECT ROUND(AVG(amount))
#     FROM book);
#
# SELECT * FROM ordering;



# # __________________________  task 39  _____________________
# # Придумайте один или несколько запросов корректировки данных к  таблицамbook и  supply . Проверьте, правильно ли они работают.
#
# DELETE FROM supply
# WHERE title IN (
#         SELECT title
#         FROM book
#       );



# # __________________________  task 40  _____________________
# # Вывести из таблицы trip информацию о командировках тех сотрудников, фамилия которых заканчивается на букву «а», в отсортированном по убыванию даты последнего дня командировки виде. В результат включить столбцы name, city, per_diem, date_first, date_last.
#
# SELECT name, city, per_diem, date_first, date_last
# FROM trip
# WHERE (name LIKE "%а ____")
# ORDER BY date_last DESC;



# # __________________________  task 41  _____________________
# # Вывести в алфавитном порядке фамилии и инициалы тех сотрудников, которые были в командировке в Москве.
# SELECT DISTINCT name FROM trip
# WHERE city = "Москва"
# ORDER BY name;


# # __________________________  task 42  _____________________
# # Для каждого города посчитать, сколько раз сотрудники в нем были.  Информацию вывести в отсортированном в алфавитном порядке по названию городов. Вычисляемый столбец назвать Количество.
#
# SELECT city, COUNT(city) as Количество FROM trip
# GROUP BY city
# ORDER BY city;


# # __________________________  task 43  _____________________
# # Вывести два города, в которых чаще всего были в командировках сотрудники. Вычисляемый столбец назвать Количество.
#
# SELECT city, COUNT(city) as Количество FROM trip
# GROUP BY city
# ORDER BY Количество DESC
# LIMIT 2;


# # __________________________  task 44  _____________________
# # Вывести информацию о командировках во все города кроме Москвы и Санкт-Петербурга (фамилии и инициалы сотрудников, город ,  длительность командировки в днях, при этом первый и последний день относится к периоду командировки). Последний столбец назвать Длительность. Информацию вывести в упорядоченном по убыванию длительности поездки, а потом по убыванию названий городов (в обратном алфавитном порядке).
#
# SELECT name, city, DATEDIFF(date_last, date_first) + 1 AS Длительность FROM trip
# WHERE city NOT IN ("Москва", "Санкт-Петербург")
# ORDER BY Длительность DESC, city DESC;



# # __________________________  task 45  _____________________
# # Вывести информацию о командировках сотрудника(ов), которые были самыми короткими по времени. В результат включить столбцы name, city, date_first, date_last.
#
# SELECT name, city, date_first, date_last FROM trip
# WHERE DATEDIFF(date_last, date_first) = (SELECT MIN(DATEDIFF(date_last, date_first)) FROM trip)



# # __________________________  task 46  _____________________
# # Вывести информацию о командировках, начало и конец которых относятся к одному месяцу (год может быть любой). В результат включить столбцы name, city, date_first, date_last. Строки отсортировать сначала  в алфавитном порядке по названию города, а затем по фамилии сотрудника .
#
# SELECT name, city, date_first, date_last FROM trip
# WHERE MONTH(date_first) = MONTH(date_last)
# ORDER BY city, name



# # __________________________  task 47  _____________________
# # Вывести название месяца и количество командировок для каждого месяца. Считаем, что командировка относится к некоторому месяцу, если она началась в этом месяце. Информацию вывести сначала в отсортированном по убыванию количества, а потом в алфавитном порядке по названию месяца виде. Название столбцов – Месяц и Количество.
# SELECT MONTHNAME(date_first) AS Месяц, COUNT(MONTHNAME(date_first)) AS Количество FROM trip
# GROUP BY MONTHNAME(date_first)
# ORDER BY Количество DESC, Месяц



# # __________________________  task 48  _____________________
# # Вывести сумму суточных (произведение количества дней командировки и размера суточных) для командировок, первый день которых пришелся на февраль или март 2020 года. Значение суточных для каждой командировки занесено в столбец per_diem. Вывести фамилию и инициалы сотрудника, город, первый день командировки и сумму суточных. Последний столбец назвать Сумма. Информацию отсортировать сначала  в алфавитном порядке по фамилиям сотрудников, а затем по убыванию суммы суточных.
#
# SELECT name, city, date_first, (DATEDIFF(date_last, date_first) + 1) * per_diem AS Сумма FROM trip
# WHERE MONTH(date_first) IN (2, 3)
# ORDER BY name, Сумма DESC;



# # __________________________  task 49  _____________________
# # Вывести фамилию с инициалами и общую сумму суточных, полученных за все командировки для тех сотрудников, которые были в командировках больше чем 3 раза, в отсортированном по убыванию сумм суточных виде. Последний столбец назвать Сумма.
# #
# # Только для этого задания изменена строка таблицы trip:
# #
# # 4	Ильиных Г.Р.	Владивосток	450	2020-01-12	2020-03-02
#
# SELECT name, SUM(per_diem * (DATEDIFF(date_last, date_first) + 1)) AS Сумма FROM trip
# GROUP BY name
# HAVING COUNT(name) > 3
# ORDER BY Сумма DESC;



# # __________________________  task 50  _____________________
# # Создать таблицу fine следующей структуры:
# #
# # Поле	Описание
# # fine_id	ключевой столбец целого типа с автоматическим увеличением значения ключа на 1
# # name	строка длиной 30
# # number_plate	строка длиной 6
# # violation	строка длиной 50
# # sum_fine	вещественное число, максимальная длина 8, количество знаков после запятой 2
# # date_violation	дата
# # date_payment	дата
#
# CREATE TABLE fine (fine_id INTEGER AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), number_plate VARCHAR(6), violation VARCHAR(50), sum_fine DECIMAL(8, 2), date_violation DATE, date_payment DATE);



# # __________________________  task 51  _____________________
# # В таблицу fine первые 5 строк уже занесены. Добавить в таблицу записи с ключевыми значениями 6, 7, 8.
#
# INSERT INTO fine (name, number_plate, violation, sum_fine, date_violation, date_payment) VALUES
#     ('Баранов П.Е.', 'Р523ВТ', 'Превышение скорости(от 40 до 60)', NULL, '2020-02-14', NULL),
#     ('Абрамова К.А.', 'О111АВ', 'Проезд на запрещающий сигнал', NULL, '2020-02-23', NULL),
#     ('Яковлев Г.Р.', 'Т330ТТ', 'Проезд на запрещающий сигнал', NULL, '2020-03-03', NULL);


# # __________________________  task 52  _____________________
# # Занести в таблицу fine суммы штрафов, которые должен оплатить водитель, в соответствии с данными из таблицы traffic_violation. При этом суммы заносить только в пустые поля столбца  sum_fine.
# #
# # Таблица traffic_violationсоздана и заполнена.
#
# UPDATE fine AS f, traffic_violation AS t SET f.sum_fine = t.sum_fine
# WHERE f.violation = t.violation AND f.sum_fine IS NULL


# # __________________________  task 53  _____________________
# # Вывести фамилию, номер машины и нарушение только для тех водителей, которые на одной машине нарушили одно и то же правило   два и более раз. При этом учитывать все нарушения, независимо от того оплачены они или нет. Информацию отсортировать в алфавитном порядке, сначала по фамилии водителя, потом по номеру машины и, наконец, по нарушению.
#
#
# SELECT name, number_plate, violation
# FROM fine
# GROUP BY name, number_plate, violation
# HAVING COUNT(violation) >= 2
# ORDER BY name, number_plate, violation;



# # __________________________  task 54  _____________________
# # В таблице fine увеличить в два раза сумму неоплаченных штрафов для отобранных на предыдущем шаге записей.
#
# CREATE TABLE  query_in AS
# SELECT name, number_plate, violation, COUNT(*) AS cnt
# FROM fine
# GROUP BY name, number_plate, violation;
#
# UPDATE fine, query_in
# SET fine.sum_fine = IF(date_payment IS NULL, fine.sum_fine * 2, fine.sum_fine)
# WHERE query_in.cnt > 1
# AND fine.name = query_in.name
# AND fine.number_plate = query_in.number_plate
# AND fine.violation = query_in.violation;



# # __________________________  task 55  _____________________
# # Водители оплачивают свои штрафы. В таблице payment занесены даты их оплаты:
# #
# # payment_id	name	number_plate	violation	date_violation	date_payment
# # 1	Яковлев Г.Р.	М701АА	Превышение скорости
# # (от 20 до 40)	2020-01-12	2020-01-22
# # 2	Баранов П.Е.	Р523ВТ	Превышение скорости
# # (от 40 до 60)	2020-02-14	2020-03-06
# # 3	Яковлев Г.Р.	Т330ТТ	Проезд на
# # запрещающий сигнал	2020-03-03	2020-03-23
# # Необходимо:
# #
# # в таблицу fine занести дату оплаты соответствующего штрафа из таблицы payment;
# # уменьшить начисленный штраф в таблице fine в два раза  (только для тех штрафов, информация о которых занесена в таблицу payment) , если оплата произведена не позднее 20 дней со дня нарушения.
#
# UPDATE fine, payment
# SET fine.date_payment = payment.date_payment, fine.sum_fine = IF(DATEDIFF(fine.date_payment, fine.date_violation) <= 20, fine.sum_fine / 2, fine.sum_fine)
# WHERE (fine.name, fine.number_plate, fine.violation) = (payment.name, payment.number_plate, payment.violation) AND fine.date_payment IS NULL;
#
# SELECT * FROM fine;



# # __________________________  task 56  _____________________
# # Создать новую таблицу back_payment, куда внести информацию о неоплаченных штрафах (Фамилию и инициалы водителя, номер машины, нарушение, сумму штрафа  и  дату нарушения) из таблицы fine.
#
# CREATE TABLE back_payment AS
# (SELECT name, number_plate, violation, sum_fine, date_violation FROM fine
# WHERE date_payment IS NULL);
#
# SELECT * FROM back_payment;


# # __________________________  task 57  _____________________
# # Удалить из таблицы fine информацию о нарушениях, совершенных раньше 1 февраля 2020 года.
#
# DELETE FROM fine
# WHERE date_violation < '2020-02-01';
#
# SELECT * FROM fine;



# # __________________________  task 58  _____________________
# # Создать таблицу author следующей структуры:
# #
# # Поле	Тип, описание
# # author_id	INT PRIMARY KEY AUTO_INCREMENT
# # name_author	VARCHAR(50)
#
# CREATE TABLE author(author_id INT PRIMARY KEY AUTO_INCREMENT, name_author VARCHAR(50))



# # __________________________  task 59  _____________________
# # Заполнить таблицу author. В нее включить следующих авторов:
# #
# # Булгаков М.А.
# # Достоевский Ф.М.
# # Есенин С.А.
# # Пастернак Б.Л.
#
# INSERT INTO author (name_author) VALUES ('Булгаков М.А.'), ('Достоевский Ф.М.'), ('Есенин С.А.'), ('Пастернак Б.Л.');



# # __________________________  task 60  _____________________
# # Перепишите запрос на создание таблицы book , чтобы ее структура соответствовала структуре, показанной на логической схеме (таблица genre уже создана, порядок следования столбцов - как на логической схеме в таблице book, genre_id  - внешний ключ) . Для genre_id ограничение о недопустимости пустых значений не задавать. В качестве главной таблицы для описания поля  genre_idиспользовать таблицу genre следующей структуры:
# #
# # Поле	Тип, описание
# # genre_id	INT PRIMARY KEY AUTO_INCREMENT
# # name_genre	VARCHAR(30)
#
# CREATE TABLE book (
#     book_id INT PRIMARY KEY AUTO_INCREMENT,
#     title VARCHAR(50),
#     author_id INT NOT NULL,
#     genre_id INT,
#     price DECIMAL(8,2),
#     amount INT,
#     FOREIGN KEY (author_id)  REFERENCES author(author_id),
#     FOREIGN KEY (genre_id)  REFERENCES genre(genre_id)
# );



# # __________________________  task 61  _____________________
# # Создать таблицу book той же структуры, что и на предыдущем шаге. Будем считать, что при удалении автора из таблицы author, должны удаляться все записи о книгах из таблицы book, написанные этим автором. А при удалении жанра из таблицы genre для соответствующей записи book установить значение Null в столбце genre_id.
#
# CREATE TABLE book (
#     book_id INT PRIMARY KEY AUTO_INCREMENT,
#     title VARCHAR(50),
#     author_id INT NOT NULL,
#     genre_id INT,
#     price DECIMAL(8,2),
#     amount INT,
#     FOREIGN KEY (author_id)  REFERENCES author(author_id) ON DELETE CASCADE,
#     FOREIGN KEY (genre_id)  REFERENCES genre(genre_id) ON DELETE SET NULL
# );


# # __________________________  task 62  _____________________
# # Добавьте три последние записи (с ключевыми значениями 6, 7, 8) в таблицу book, первые 5 записей уже добавлены:
#
# INSERT INTO book (title, author_id, genre_id, price, amount) VALUES ('Стихотворения и поэмы', 3, 2, 650.00, 15), ('Черный человек', 3, 2, 570.20, 6), ('Лирика', 4, 2, 518.99, 2);



# # __________________________  task 63  _____________________
# # Вывести название, жанр и цену тех книг, количество которых больше 8, в отсортированном по убыванию цены виде.
#
# SELECT title, name_genre, price FROM
# genre INNER JOIN book
# ON genre.genre_id = book.genre_id
# WHERE book.amount > 8
# ORDER BY price DESC;



# # __________________________  task 64  _____________________
# # Вывести все жанры, которые не представлены в книгах на складе.
#
# SELECT name_genre
# FROM genre LEFT JOIN book
# ON genre.genre_id = book.genre_id
# WHERE book.genre_id IS NULL;


# # __________________________  task 65  _____________________
# # Есть список городов, хранящийся в таблице city:
# #
# # city_id	name_city
# # 1	Москва
# # 2	Санкт-Петербург
# # 3	Владивосток
# # Необходимо в каждом городе провести выставку книг каждого автора в течение 2020 года. Дату проведения выставки выбрать случайным образом. Создать запрос, который выведет город, автора и дату проведения выставки. Последний столбец назвать Дата. Информацию вывести, отсортировав сначала в алфавитном порядке по названиям городов, а потом по убыванию дат проведения выставок.
#
# SELECT name_city, name_author, (DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365) DAY)) AS Дата FROM city, author
# ORDER BY name_city, Дата DESC;



# # __________________________  task 66  _____________________
# # Вывести информацию о книгах (жанр, книга, автор), относящихся к жанру, включающему слово «роман» в отсортированном по названиям книг виде.
#
# SELECT name_genre, title, name_author
# FROM
#     author
#     INNER JOIN  book ON author.author_id = book.author_id
#     INNER JOIN genre ON genre.genre_id = book.genre_id
# WHERE name_genre = 'роман'
# ORDER BY title;



# # __________________________  task 67  _____________________
# # Посчитать количество экземпляров  книг каждого автора из таблицы author.  Вывести тех авторов,  количество книг которых меньше 10, в отсортированном по возрастанию количества виде. Последний столбец назвать Количество.
#
# SELECT name_author, SUM(amount) AS Количество
# FROM author LEFT JOIN book
# ON author.author_id = book.author_id
# GROUP BY name_author
# HAVING Количество
# IS NULL OR Количество < 10
# ORDER BY Количество;


# # __________________________  task 68  _____________________
# # Вывести в алфавитном порядке всех авторов, которые пишут только в одном жанре. Поскольку у нас в таблицах так занесены данные, что у каждого автора книги только в одном жанре,  для этого запроса внесем изменения в таблицу book. Пусть у нас  книга Есенина «Черный человек» относится к жанру «Роман», а книга Булгакова «Белая гвардия» к «Приключениям» (эти изменения в таблицы уже внесены).
#
# SELECT name_author
# FROM author INNER JOIN book
# ON author.author_id = book.author_id
# GROUP BY book.author_id
# HAVING COUNT(DISTINCT(genre_id)) = 1;



# # __________________________  task 69  _____________________
# # Вывести информацию о книгах (название книги, фамилию и инициалы автора, название жанра, цену и количество экземпляров книги), написанных в самых популярных жанрах, в отсортированном в алфавитном порядке по названию книг виде. Самым популярным считать жанр, общее количество экземпляров книг которого на складе максимально.
#
# SELECT title, name_author, name_genre, price, amount
# FROM
#     author
#     INNER JOIN book ON author.author_id = book.author_id
#     INNER JOIN genre ON book.genre_id = genre.genre_id
# WHERE genre.genre_id IN
#          (
#           SELECT query_in_1.genre_id
#           FROM
#               (
#                 SELECT genre_id, SUM(amount) AS sum_amount
#                 FROM book
#                 GROUP BY genre_id
#                )query_in_1
#           INNER JOIN
#               (
#                 SELECT genre_id, SUM(amount) AS sum_amount
#                 FROM book
#                 GROUP BY genre_id
#                 ORDER BY sum_amount DESC
#                 LIMIT 1
#                )query_in_2
#           ON query_in_1.sum_amount= query_in_2.sum_amount
#          )
# ORDER BY title;



# # __________________________  task 70  _____________________
# # Если в таблицах supply  и book есть одинаковые книги, которые имеют равную цену,  вывести их название и автора, а также посчитать общее количество экземпляров книг в таблицах supply и book,  столбцы назвать Название, Автор  и Количество.
#
# SELECT book.title AS Название, name_author AS Автор, (book.amount + supply.amount) AS Количество
# FROM
#     author
#     INNER JOIN book USING (author_id)
#     INNER JOIN supply ON book.title = supply.title
#                          and book.price = supply.price
# ;


# # __________________________  task 71  _____________________
# # Придумайте один или несколько запросов для таблиц book,  author, genre и city. Проверьте, правильно ли они работают.
#
# SELECT title AS Название_книги, name_author AS Имя_писателя, name_genre AS Жанр, price AS Цена, amount AS Количество
# FROM
#     author
#     INNER JOIN book USING(author_id)
#     INNER JOIN genre USING(genre_id)
# WHERE amount > 10
# ORDER BY Имя_писателя;


# _____________________ expression # 1 ____________________
# import re
#
# text = 'Карта map и объект bitmap - это разные вещи'

# match = re.findall('map', text)
# print(match)
# match = re.findall('\\bmap\\b', text)
# print(match)
# match = re.findall(r'\bmap\b', text)
# print(match)

# import re
#
# text = 'еда, беда, победа'
# match = re.findall('еда', text)
#
# print(match)


# import re
#
# text = 'еда, беда, победа'
# match = re.findall('(еда)', text)
#
# print(match)


# import re
#
# text = 'еда, беда, победа'
# match = re.findall(r'\(еда\)', text)
#
# print(match)

#
# import re
#
# text = 'еда, беда, победа, нет еды, в честь победы, поставил на стол еду'
# match = re.findall(r'[еЕ]д[ауы]', text)
#
# print(match)


# import re
#
# text = 'еда, беда, победа, нет еды, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[0123456789]', text)
#
# print(match)

#
# import re
#
# text = 'еда, беда, победа, нет еды, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[0123456789][0123456789]', text)
#
# print(match)


# import re
#
# text = 'еда, беда, победа, нет еды, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[0-9][0-9]', text)
#
# print(match)

# import re
#
# text = 'еда, беда, победа, нет еды, -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[-0-9][0-9]', text)
#
# print(match)


# import re
#
# text = 'еда, беда, победа, нет еды, -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[^0-9]', text)
#
# print(match)

# import re
#
# text = 'еда, беда, победа, нет еды, -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[а-я]', text)
#
# print(match)

# import re
#
# text = 'еда, беда, победа, нет еды, -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[а-яА-Я]', text)
#
# print(match)


# import re
#
# text = 'еда, беда, победа, (нет еды), -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'[(&.)а-яА-Я]', text)
#
# print(match)

# import re
#
# text = 'еда, беда, победа, (нет еды), -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'\d', text)
#
# print(match)

# import re
#
# text = 'еда, беда, победа, (нет еды), -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'\w', text)
#
# print(match)

# import re
#
# text = 'еда, беда, победа, (нет еды), -5, в честь победы, поставил на стол еду, 55'
# match = re.findall(r'\w', text, re.ASCII)
#
# print(match)


# import re
#
# text = 'еду, 55, 0xf, 0xa, 0x5'
# color = re.findall(r'0x[\da-fA-F]', text)
#
# print(color)


# # __________________________  task 71  _____________________
# # Для книг, которые уже есть на складе (в таблице book), но по другой цене, чем в поставке (supply),  необходимо в таблице book увеличить количество на значение, указанное в поставке,  и пересчитать цену. А в таблице  supply обнулить количество этих книг. Формула для пересчета цены:
# # где  p1, p2 - цена книги в таблицах book и supply;
# #        k1, k2 - количество книг в таблицах book и supply.

# UPDATE book
#      INNER JOIN author ON author.author_id = book.author_id
#      INNER JOIN supply ON book.title = supply.title
#                          and supply.author = author.name_author
# SET book.amount = book.amount + supply.amount,
#     supply.amount = 0, book.price = (book.price * book.amount + supply.price * supply.amount) / (book.amount + supply.amount)
# WHERE book.price <> supply.price;
#
# SELECT * FROM book;
#
# SELECT * FROM supply;


# # __________________________  task 71  _____________________
# # Включить новых авторов в таблицу author с помощью запроса на добавление, а затем вывести все данные из таблицы author.  Новыми считаются авторы, которые есть в таблице supply, но нет в таблице author.
#
# INSERT INTO author (name_author)
# SELECT supply.author
# FROM
#     author
#     RIGHT JOIN supply on author.name_author = supply.author
# WHERE name_author IS Null;
#
# SELECT * FROM author;




# _____________________ expression # 2 ____________________
# import re
#
# text = "Google, Gooogle, Goooooogle"
# my_match = re.findall(r"o{2,5}", text)
# print(my_match)


# import re
#
# text = "Google, Gooogle, Goooooogle"
# my_match = re.findall(r"o{2,5}?", text)
# print(my_match)


# import re
#
# text = "Google, Gooogle, Goooooogle"
# my_match = re.findall(r"Go{2,}gle", text)
# print(my_match)


# import re
#
# text = "Google, Gooogle, Goooooogle"
# my_match = re.findall(r"Go{,4}gle", text)
# print(my_match)


# import re
#
# phone = "89123456789"
# my_match = re.findall(r"8\d{10}", phone)
# print(my_match)



# import re
#
# text = "стеклянный, стекляный"
# my_match = re.findall(r"стеклянн?ый", text)
# print(my_match)

#
# import re
#
# text = ("author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001")
# # my_match = text.split(";")
# my_match = re.findall(r"\w+\s*=\s*[^;]+", text)
# print(my_match)



# import re
#
# text = ("author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001")
# my_match = re.findall(r"(\w+)\s*=\s*([^;]+)", text)
# print(my_match)


# import re
#
# text = ("<p>Картинка <img src='bg.jpg'> в тексте</p>")
# my_match = re.findall(r"<img.*>", text)
# print(my_match)


# import re
#
# text = ("<p>Картинка <img src='bg.jpg'> в тексте</p>")
# my_match = re.findall(r"<img.*?>", text)
# print(my_match)


# import re
#
# text = ("<p>Картинка <img src='bg.jpg'> в тексте</p>")
# my_match = re.findall(r"<img[^>]*>", text)
# print(my_match)


# import re
#
# text = ("<p>Картинка <img> в тексте</p>")
# # my_match = re.findall(r"<img[^>]*>", text)
# my_match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]>", text)
# print(my_match)


# import re
#
# text = ("<p>Картинка <img src='bg.jpg'> в тексте</p>")
# # my_match = re.findall(r"<img[^>]*>", text)
# my_match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)
# print(my_match)


# import re
#
# text = ("<p>Картинка <img alt='Картинка' src='bg.jpg'> в тексте</p>")
# # my_match = re.findall(r"<img[^>]*>", text)
# my_match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)
# print(my_match)



# # __________________________  task 72  _____________________
# # Добавить новые книги из таблицы supply в таблицу book на основе сформированного выше запроса. Затем вывести для просмотра таблицу book.
#
# INSERT INTO book (title, author_id, price, amount)
# SELECT title, author_id, price, amount
# FROM
#     author
#     INNER JOIN supply ON author.name_author = supply.author
# WHERE amount <> 0;
#
# SELECT * FROM book;


# # __________________________  task 73  _____________________
# # Занести для книги «Стихотворения и поэмы» Лермонтова жанр «Поэзия», а для книги «Остров сокровищ» Стивенсона - «Приключения». (Использовать два запроса).
# UPDATE book
# SET genre_id =
#       (
#        SELECT genre_id
#        FROM genre
#        WHERE name_genre = 'Поэзия'
#       )
# WHERE book_id = 10;
# UPDATE book
# SET genre_id =
#       (
#        SELECT genre_id
#        FROM genre
#        WHERE name_genre = 'Приключения'
#       )
# WHERE book_id = 11;
#
# SELECT * FROM book;


# # __________________________  task 74  _____________________
# # Удалить всех авторов и все их книги, общее количество книг которых меньше 20.
#
# DELETE FROM author
# WHERE author_id IN (SELECT author_id FROM book
#                     GROUP BY author_id
#                    HAVING SUM(amount) < 20);
#
# SELECT * FROM author;
#
# SELECT * FROM book;


# # __________________________  task 75  _____________________
# # Удалить все жанры, к которым относится меньше 4-х наименований книг. В таблице book для этих жанров установить значение Null.
#
# DELETE FROM genre
# WHERE genre_id IN (SELECT genre_id FROM book
#                     GROUP BY genre_id
#                     HAVING COUNT(title) < 4);
#
# SELECT * FROM genre;
#
# SELECT * FROM book;


# # __________________________  task 76  _____________________
# # # Удалить всех авторов, которые пишут в жанре "Поэзия". Из таблицы book удалить все книги этих авторов. В запросе для отбора авторов использовать полное название жанра, а не его id.
# #
# DELETE FROM author
# USING
#     author
#     INNER JOIN book ON author.author_id = book.author_id
# WHERE book.genre_id  = (SELECT genre_id FROM genre
#                        WHERE name_genre = "Поэзия");
#
# SELECT * FROM author;
#
# SELECT * FROM book;


# ___________________  решение другого ученика  _____________
# DELETE FROM author
# USING author JOIN book USING(author_id)
#              JOIN genre USING(genre_id)
# WHERE name_genre='Поэзия'


# # __________________________  task 77  _____________________
# # Придумайте один или несколько запросов корректировки данных для таблиц book,  author, genre и supply . Проверьте, правильно ли они работают.
#
# DELETE FROM supply
# USING supply INNER JOIN book ON supply.title = book.title
# WHERE book.amount > 8;
#
# SELECT * FROM supply;


# _____________________ expression # 3 ____________________
# import re
#
# text = "lat=5, lon=7"
# # text = "pi = 3, a=1"
# my_match = re.findall(r"\w+\s*=\s*\d+", text)
# print(my_match)


# import re
#
# text = "lat=5, lon=7"
# # text = "pi = 3, a=1"
# my_match = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", text)
# print(my_match)


# import re
#
# text = "lat=5, lon=7"
# # text = "pi = 3, a=1"
# my_match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)
# print(my_match)


# import re
#
# text = "lat=5, lon=7"
# my_match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
# print(my_match)


# import re
#
# text = "lat=5, lon=7"
# my_match = re.findall(r"(lat|lon)\s*=\s*(?:\d+)", text)
# print(my_match)


# import re
#
# text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
# my_match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)
# print(my_match)


# import re
#
# text = "<p>Картинка <img src='bg.jpg\"> в тексте</p>"
# my_match = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text)
# print(my_match)


# import re
#
# text = "<p>Картинка <img src='bg.jpg\"> в тексте</p>"
# my_match = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text)
# print(my_match)


# import re
#
# with open("map.xml", "r") as file:
#     lat = []
#     lon = []
#     for text in file:
#         my_match = re.findall(r"<point\s+[^>]*?lon=([\"\'])([0-9.,]+)\1\s+[^>]*lat=([\"\'])([0-9.,]+)\1", text)
#         print(my_match)
#
#     print(lon, lat, sep="\n")


# import re
#
# with open("map.xml", "r") as file:
#     lat = []
#     lon = []
#     for text in file:
#         my_match = re.findall(r"<point\s+[^>]*?lon=([\"\'])([0-9.,]+)\1\s+[^>]*lat=([\"\'])([0-9.,]+)\1", text)
#         if len(my_match) > 0:
#             lon.append(my_match[0][1])
#             lat.append(my_match[0][3])
#
#     print(lon, lat, sep="\n")


#
# import re
#
# with open("map.xml", "r") as file:
#     lat = []
#     lon = []
#     for text in file:
#         my_match = re.search(r"<point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+[^>]*lat=([\"\'])(?P<lat>[0-9.,]+)\1", text)
#         if my_match:
#             v = my_match.groupdict()
#             if "lon" in v and "lat" in v:
#                 lon.append(v["lon"])
#                 lat.append(v["lat"])
#
# print(lon, lat, sep="\n")

# # __________________________  stepik 6.7 - 1 _____________________
# Продолжите программу, в которой уже реализовано чтение данных (чисел) из входного потока и сохранение их в виде кортежа t:
# t = tuple(map(int, input().split()))  # кортеж из целых чисел
# s = 0  # начальное значение суммы элементов
# Используя моржовый оператор и переменную s, необходимо с помощью генератора списка сформировать новый список lst из сумм текущего и всех предыдущих значений кортежа t. Например, для кортежа:
# t = (1, 2, 3, 4, 5, 6)
# должен формироваться список:
# lst = [1, 3, 6, 10, 15, 21]
# Здесь каждый следующий элемент - это сумма текущего и всех предыдущих элементов кортежа t.
# Выведите полученные значения элементов списка lst на экран в одну строчку через пробел.

# t = tuple(map(int, input().split()))  # кортеж из целых чисел (в программе не менять)
# s = 0  # начальное значение суммы элементов
#
# # здесь продолжайте программу
# lst = [(s:= s + x) for x in t]
# print(*lst)


# # __________________________  stepik 6.7 - 2 _____________________
# # Используя цикл while и моржовый оператор, выполните считывание целых чисел из входного потока (с клавиатуры) с подсчетом суммы четных чисел. Цикл while должен работать до тех пор, пока не встретится число 0. Полученную сумму выведите на экран.
# # P.S. В программе для считывания целых чисел используйте команду int(input()), которая должна быть прописана только один раз.
#
# s = 0
# while (x := int(input())) != 0:
#     if x % 2 == 0:
#         s += x
#
# print(s)


# # __________________________  stepik 6.7 - 3 _____________________
# # Продолжите программу, в которой уже объявлена функция f и формируется кортеж t:
# # def f(x):
# #     return abs(x) ** 0.5 + 3.2 + x
# # t = tuple(map(float, input().split()))  # кортеж t в программе не менять
# # Необходимо продолжить эту программу и с помощью генератора списка сформировать двумерный (вложенный) список lst на основе кортежа t, состоящий из следующих значений:
# #   - значения элементов кортежа t.
# # При описании генератора воспользуйтесь моржовой операцией для однократного вызова функции f(x) для каждого значения кортежа t. То есть, при формировании каждого вложенного списка:
# #  должна вызываться однократно (один раз).
# # P.S. На экран ничего выводить не нужно.
# def f(x):
#     return abs(x) ** 0.5 + 3.2 + x
#
#
# t = tuple(map(float, input().split()))  # кортеж t в программе не менять
#
# # здесь продолжайте программу
#
# lst = [[c := f(x), c ** 2, c **3] for x in t]




# # __________________________  task 78  _____________________
#Вывести все заказы Баранова Павла (id заказа, какие книги, по какой цене и в каком количестве он заказал) в отсортированном по номеру заказа и названиям книг виде.

# SELECT buy.buy_id, book.title, book.price, buy_book.amount
# FROM client
# INNER JOIN buy ON client.client_id = buy.client_id
# INNER JOIN buy_book ON buy.buy_id = buy_book.buy_id
# INNER JOIN book ON buy_book.book_id = book.book_id
# WHERE name_client = 'Баранов Павел'
# ORDER BY buy.buy_id, title



# # __________________________  task 79  _____________________
# Посчитать, сколько раз была заказана каждая книга, для книги вывести ее автора (нужно посчитать, в каком количестве заказов фигурирует каждая книга).  Вывести фамилию и инициалы автора, название книги, последний столбец назвать Количество. Результат отсортировать сначала  по фамилиям авторов, а потом по названиям книг.

# SELECT name_author, title, COUNT(buy_book.book_id) AS Количество
# FROM author
# INNER JOIN book ON author.author_id = book.author_id
# LEFT JOIN buy_book ON book.book_id = buy_book.book_id
# GROUP BY book.book_id, book.author_id
# ORDER BY name_author, title;



# _____________________ expression # 4 ____________________
# import re
#
# text = "Подоходный налог"
#
# my_match = re.findall(r"прибыль|обретение|\bдоход\b", text)
# print(my_match)


# import re
#
# text = "Подоходный налог"
#
# my_match = re.findall(r"\b(?:прибыль|обретение|доход)\b", text)
# print(my_match)



# # __________________________  stepik 6.7 - 4 _____________________
# # Используя цикл while и моржовый оператор, выполните считывание целых чисел из входного потока (с клавиатуры) с подсчетом произведения чисел, кратных трем. Цикл while должен работать до тех пор, пока не встретится отрицательное число или число 0. Полученное произведение выведите на экран.
# # P.S. В программе для считывания целых чисел используйте команду int(input()), которая должна быть прописана только один раз.
# s = 1
# while (d:= int(input())) > 0:
#     if d % 3 == 0:
#         s *= d
#
# print(s)






# import re
#
# text = """
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <meta name="viewport" content="width=device-width, initial-scale=1"/>
# <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
# <title>Мое обучение</title>
# </head>
# <body>
# <script type="text/javascript">
# let o = document.getElementByID('id_div');
# console.log(obj);
# </script>
# </body>
# </html>
# """
#
# my_match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
# print(my_match)


# import re
#
# text = """
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <meta name="viewport" content="width=device-width, initial-scale=1"/>
# <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
# <title>Мое обучение</title>
# </head>
# <body>
# <script type="text/javascript">
# let o = document.getElementByID('id_div');
# console.log(obj);
# </script>
# </body>
# </html>
# """
#
# my_match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE)
# print(my_match)


# import re
#
# text = """
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <meta name="viewport" content="width=device-width, initial-scale=1"/>
# <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
# <title>Мое обучение</title>
# </head>
# <body>
# <p align=center>Hello World!</p>
# </body>
# </html>
# """
#
# my_match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text, re.MULTILINE)
# print(my_match)


# import re
#
# text = """
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <meta name="viewport" content="width=device-width, initial-scale=1"/>
# <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
# <title>Мое обучение</title>
# </head>
# <body>
# <p align=center>Hello World!</p>
# </body>
# </html>
# """
#
# my_match = re.findall(r"""([-\w]+)      #выделяем атрибут
#                     [ \t]*=[ \t]*               #далее, должно идти равно и кавычки
#                     (?P<q>[\"'])?               #проверяем наличие кавычки
#                     (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))    #выделяем значение атрибута
#                     """, text, re.MULTILINE|re.VERBOSE)
# print(my_match)

#
# import re
#
# text = "Python, python, PYTHON, PyThOn"
#
# my_match = re.findall(r"(?im)python", text)
# print(my_match)


# _____________________ expression # 5 ____________________
# import re
#
# text = "<font color=#CC0000>"
# my_match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
# print(my_match)
# print(my_match.group(0))
# print(my_match.group(1))
# print(my_match.group(0, 1, 2))
# print(my_match.groups())
# print(my_match.lastindex)
# print(my_match.start(1))
# print(my_match.end(1))
# print(my_match.span(1))
# print(my_match.endpos)
# print(my_match.pos)
# print(my_match.re)
# print(my_match.string)


# import re
#
# text = "<font color=#CC0000>"
# my_match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)", text)
# print(my_match.groupdict())
# print(my_match.lastgroup)
# print(my_match.expand(r"\g<key>:\g<value>"))
# print(my_match.expand(r"\1:\2"))


# import re
#
# text = "<font color=#CC0000 bg=#ffffff>"
# my_match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)", text)
# print(my_match)


# import re
#
# text = "<font color=#CC0000 bg=#ffffff>"
# for my_match in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)", text):
#     print(my_match)


# import re
#
# text = "<font color=#CC0000 bg=#ffffff>"
# my_match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)", text)
# print(my_match)


# # __________________________  task 80  _____________________
# # Вывести города, в которых живут клиенты, оформлявшие заказы в интернет-магазине. Указать количество заказов в каждый город, этот столбец назвать Количество. Информацию вывести по убыванию количества заказов, а затем в алфавитном порядке по названию городов.
# SELECT name_city, COUNT(buy.buy_id) AS Количество
# FROM city
# INNER JOIN client ON city.city_id = client.city_id
# LEFT JOIN buy ON client.client_id = buy.client_id
# GROUP BY city.name_city
# ORDER BY Количество DESC, name_city;



# # __________________________  task 81  _____________________
# # Вывести номера всех оплаченных заказов и даты, когда они были оплачены.
# SELECT buy_id, date_step_end
# FROM step
# INNER JOIN buy_step ON step.step_id = buy_step.step_id
# WHERE buy_step.step_id = 1 AND date_step_end IS NOT NULL
# ORDER BY date_step_end;



# _____________________ expression # 6 ____________________
# import re
#
# text = "+7(123)456-78-90"
# m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
# print(m)



# import re
#
# text = " +7(123)456-78-90"
# m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
# print(m)


# import re
#
# text = """<point lon="40.8482" lat="52.6274" />
# <point lon="40.8482" lat="52.6274" />; <point lon="40.8482" lat="52.6274" />
# <point lon="40.8482" lat="52.6274" />, <point lon="40.8482" lat="52.6274" />
# """
# m = re.split(r"[\n;,]+", text)
# print(m)


# import re
#
# text = """Москва
# Казань
# Тверь
# Самара
# Уфа
# """
# lst = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
# print(lst)


# import re
# 
# text = """Москва
# Казань
# Тверь
# Самара
# Уфа
# """
# 
# 
# count = 0
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
# 
# lst = re.sub(r"\s*(\w+)\s*", repl_find, text)
# print(lst)



# import re
#
# text = """Москва
# Казань
# Тверь
# Самара
# Уфа
# """
# lst, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
# print(lst, total)

#
# import re
#
# text = """Москва
# Казань
# Тверь
# Самара
# Уфа
# """
#
#
# count = 0
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
# rx = re.compile(r"\s*(\w+)\s*")
# lst, total = rx.subn(r"<option>\1</option>\n", text)
# lst2 = rx.sub(repl_find, text)
# print(lst, total, lst2, sep="\n")



# # __________________________  task 82  _____________________
# # Вывести информацию о каждом заказе: его номер, кто его сформировал (фамилия пользователя) и его стоимость (сумма произведений количества заказанных книг и их цены), в отсортированном по номеру заказа виде. Последний столбец назвать Стоимость.
# SELECT buy_id, name_client, SUM(buy_book.amount * price) AS Стоимость
# FROM buy_book
# JOIN buy USING (buy_id)
# JOIN client USING (client_id)
# JOIN book USING (book_id)
# GROUP BY buy_id
# ORDER BY buy_id;


# # __________________________  task 83  _____________________
# # Вывести номера заказов (buy_id) и названия этапов,  на которых они в данный момент находятся. Если заказ доставлен –  информацию о нем не выводить. Информацию отсортировать по возрастанию buy_id.
# SELECT
#     buy_step.buy_id, step.name_step
# FROM step
# JOIN
#     buy_step ON step.step_id = buy_step.step_id
# WHERE
#     buy_step.date_step_beg IS NOT NULL
#     AND buy_step.date_step_end IS NULL
# ORDER BY
#     buy_step.buy_id;



# # __________________________  task 84  _____________________
# # В таблице city для каждого города указано количество дней, за которые заказ может быть доставлен в этот город (рассматривается только этап Транспортировка). Для тех заказов, которые прошли этап транспортировки, вывести количество дней за которое заказ реально доставлен в город. А также, если заказ доставлен с опозданием, указать количество дней задержки, в противном случае вывести 0. В результат включить номер заказа (buy_id), а также вычисляемые столбцы Количество_дней и Опоздание. Информацию вывести в отсортированном по номеру заказа виде.
#
# SELECT buy.buy_id, DATEDIFF(date_step_end, date_step_beg)  AS Количество_дней, IF( DATEDIFF(date_step_end, date_step_beg) > days_delivery, DATEDIFF(date_step_end, date_step_beg) - days_delivery, 0) AS Опоздание
# FROM
#     city
# JOIN
#     client USING (city_id)
# JOIN
#     buy USING (client_id)
# JOIN
#     buy_step USING (buy_id)
# JOIN
#     step USING (step_id)
# WHERE
#     step_id = 3 AND date_step_end IS NOT NULL
# ORDER BY
#     buy_id


# # __________________________  task 85  _____________________
# # Выбрать всех клиентов, которые заказывали книги Достоевского, информацию вывести в отсортированном по алфавиту виде. В решении используйте фамилию автора, а не его id.
#
# SELECT DISTINCT name_client
# FROM
#     author
# JOIN
#     book USING (author_id)
# JOIN
#     buy_book USING (book_id)
# JOIN
#     buy USING (buy_id)
# JOIN
#     client USING (client_id)
# WHERE
#     name_author = "Достоевский Ф.М."
# ORDER BY
#     name_client;


# # __________________________  task 86  _____________________
# # Вывести жанр (или жанры), в котором было заказано больше всего экземпляров книг, указать это количество . Последний столбец назвать Количество.
#
# SELECT
#     name_genre, SUM(buy_book.amount) AS Количество
# FROM
#     genre
# JOIN
#     book USING (genre_id)
# JOIN
#     buy_book USING (book_id)
# GROUP BY
#     genre_id
# HAVING
#     SUM(buy_book.amount) = (
#         SELECT MAX(сумма)
#         FROM
#         (SELECT name_genre, SUM(buy_book.amount) AS
#     сумма FROM genre
# JOIN
#     book USING (genre_id)
# JOIN
#     buy_book USING (book_id)
# GROUP BY
#     genre_id) AS жанры
# );


# # __________________________  task 87  _____________________
# # Сравнить ежемесячную выручку от продажи книг за текущий и предыдущий годы. Для этого вывести год, месяц, сумму выручки в отсортированном сначала по возрастанию месяцев, затем по возрастанию лет виде. Название столбцов: Год, Месяц, Сумма.
#
# SELECT
#     YEAR(date_payment) AS Год,
#     MONTHNAME(date_payment) AS Месяц,
#     SUM(amount * price) AS Сумма
# FROM
#     buy_archive
# GROUP BY
#     Год, Месяц
# UNION
# SELECT
#     YEAR(date_step_end) AS Год,
#     MONTHNAME(date_step_end) AS Месяц,
#     SUM(buy_book.amount * price) AS Сумма
# FROM
#     book
#     INNER JOIN buy_book USING(book_id)
#     INNER JOIN buy USING(buy_id)
#     INNER JOIN buy_step USING(buy_id)
#     INNER JOIN step USING(step_id)
# WHERE
#     step.name_step = "Оплата" AND
#     buy_step.date_step_end IS NOT NULL AND
#     YEAR(date_step_end) IN (2019 , 2020)
# GROUP BY
#     Год, Месяц
# ORDER BY
#     Месяц ASC, Год ASC;


# # __________________________  task 88  _____________________
# # Для каждой отдельной книги необходимо вывести информацию о количестве проданных экземпляров и их стоимости за 2020 и 2019 год . За 2020 год проданными считать те экземпляры, которые уже оплачены. Вычисляемые столбцы назвать Количество и Сумма. Информацию отсортировать по убыванию стоимости.

# SELECT
#     title,
#     SUM(Количество) AS Количество,
#     SUM(Сумма) AS Сумма
# FROM
#     (
#     SELECT
#         book.title,
#         SUM(buy_book.amount) AS Количество,
#         SUM(buy_book.amount * book.price) AS Сумма
#     FROM
#         book
#     JOIN
#         buy_book USING(book_id)
#     JOIN
#         buy_step USING(buy_id)
#     WHERE
#         step_id = 1 AND date_step_end IS NOT NULL AND YEAR(date_step_end) = 2020
#     GROUP BY
#         book.title
#
#     UNION ALL
#
#     SELECT
#         book.title,
#         SUM(buy_archive.amount) AS Количество,
#         SUM(buy_archive.amount *   buy_archive.price) AS Сумма
#     FROM
#         buy_archive
#     JOIN
#         book USING(book_id)
#     WHERE
#         YEAR(buy_archive.date_payment) = 2019
#     GROUP BY
#         book.title
#     ) AS combined
# GROUP BY title
# ORDER BY
#   Сумма DESC;



# # __________________________  task 89  _____________________
# # Придумайте один или несколько запросов на выборку для предметной области «Интернет-магазин книг» (в таблицы занесены данные, как на первом шаге урока). Проверьте, правильно ли они работают.
#
# SELECT name_client FROM client
# WHERE client_id IN (
#     SELECT client_id FROM buy
#     JOIN buy_book USING (buy_id)
#     JOIN book USING(book_id)
#     WHERE book.title IN ("Белая гвардия", "Игрок")
# )
# ORDER BY name_client;

# # __________________________  task 90  _____________________
# # Включить нового человека в таблицу с клиентами. Его имя Попов Илья, его email popov@test, проживает он в Москве.
#
# INSERT INTO client(name_client, city_id, email)
# VALUES ("Попов Илья",
#         (
#             SELECT city_id FROM city
#             WHERE name_city = "Москва"
#         ),
#         "popov@test"
#        )



# # # __________________________  task 91  _____________________
# # Создать новый заказ для Попова Ильи. Его комментарий для заказа: «Связаться со мной по вопросу доставки».
#
# INSERT INTO buy SET buy_description = "Связаться со мной по вопросу доставки", client_id
# = (SELECT client_id FROM client
#    WHERE name_client = "Попов Илья"
#   )



# # # __________________________  task 92  _____________________
# # В таблицу buy_book добавить заказ с номером 5. Этот заказ должен содержать книгу Пастернака «Лирика» в количестве двух экземпляров и книгу Булгакова «Белая гвардия» в одном экземпляре.
#
# INSERT INTO buy_book (buy_id, book_id, amount)
# VALUES ( 5,
#     (SELECT book_id FROM book
#     WHERE title = "Лирика"), 2
# );
# INSERT INTO buy_book (buy_id, book_id, amount)
# VALUES ( 5,
#     (SELECT book_id FROM book
#     WHERE title = "Белая гвардия"), 1
# );
#
# SELECT buy_id, book_id, amount FROM buy_book;



# # # __________________________  task 93  _____________________
# # Количество тех книг на складе, которые были включены в заказ с номером 5, уменьшить на то количество, которое в заказе с номером 5  указано.
#
# UPDATE book
# JOIN buy_book USING (book_id)
# SET book.amount = book.amount - buy_book.amount
# WHERE buy_book.buy_id = 5;


# # # __________________________  task 94  _____________________
# # Создать счет (таблицу buy_pay) на оплату заказа с номером 5, в который включить название книг, их автора, цену, количество заказанных книг и  стоимость. Последний столбец назвать Стоимость. Информацию в таблицу занести в отсортированном по названиям книг виде.
#
# CREATE TABLE buy_pay (
#    title VARCHAR(255),
#    name_author VARCHAR(255),
#    price DECIMAL(5,2),
#    amount INTEGER,
#    Стоимость DECIMAL(10,2)
# );
# INSERT INTO buy_pay (title, name_author, price, amount, Стоимость)
# SELECT
#     book.title,
#     author.name_author,
#     book.price,
#     buy_book.amount,
#     book.price * buy_book.amount AS Стоимость
# FROM author
# JOIN
#     book ON author.author_id = book.author_id
# JOIN
#     buy_book ON book.book_id = buy_book.book_id
# WHERE buy_id = 5
# ORDER BY title;
# SELECT * FROM buy_pay;



# # # __________________________  task 95  _____________________
# # Создать общий счет (таблицу buy_pay) на оплату заказа с номером 5. Куда включить номер заказа, количество книг в заказе (название столбца Количество) и его общую стоимость (название столбца Итого). Для решения используйте ОДИН запрос.
#
# CREATE TABLE buy_pay AS
# SELECT
#     buy_book.buy_id,
#     SUM(buy_book.amount) AS Количество,
#     SUM(book.price * buy_book.amount) AS Итого
# FROM buy_book
# JOIN book USING(book_id)
# WHERE buy_book.buy_id = 5;



# # # __________________________  task 96  _____________________
# # В таблицу buy_step для заказа с номером 5 включить все этапы из таблицы step, которые должен пройти этот заказ. В столбцы date_step_beg и date_step_end всех записей занести Null.
#
# INSERT INTO buy_step (buy_id, step_id, date_step_beg, date_step_end)
# SELECT
#     5 AS buy_id,
#     step_id,
#     NULL AS date_step_beg,
#     NULL AS date_step_end
# FROM step;


# # # __________________________  task 97  _____________________
# # В таблицу buy_step занести дату 12.04.2020 выставления счета на оплату заказа с номером 5.
# #
# # Правильнее было бы занести не конкретную, а текущую дату. Это можно сделать с помощью функции Now(). Но при этом в разные дни будут вставляться разная дата, и задание нельзя будет проверить, поэтому  вставим дату 12.04.2020.
#
# UPDATE buy_step
# JOIN step USING(step_id)
# SET date_step_beg = '2020-04-12'
# WHERE buy_id = 5 AND step_id = 1;


# # # __________________________  task 98  _____________________
# Завершить этап «Оплата» для заказа с номером 5, вставив в столбец date_step_end дату 13.04.2020, и начать следующий этап («Упаковка»), задав в столбце date_step_beg для этого этапа ту же дату.
#
# # Реализовать два запроса для завершения этапа и начале следующего. Они должны быть записаны в общем виде, чтобы его можно было применять для любых этапов, изменив только текущий этап. Для примера пусть это будет этап «Оплата».
#
# UPDATE buy_step
# JOIN step USING(step_id)
# SET date_step_end = '2020-04-13'
# WHERE buy_id = 5 AND name_step = 'Оплата';
#
# UPDATE buy_step
# JOIN step USING(step_id)
# SET date_step_beg = '2020-04-13'
# WHERE buy_id = 5 AND (
#     step.step_id = (
#         SELECT step_id + 1 FROM step
#         WHERE step_id = (
#             SELECT step_id FROM step
#             WHERE name_step = 'Оплата')
#     )
# );


# # # __________________________  task 99  _____________________
# # Придумайте один или несколько запросов корректировки данных для предметной области «Интернет-магазин книг» (в таблицы занесены данные, как на этом шаге). Проверьте, правильно ли они работают.
#
# UPDATE buy_step
# JOIN step USING(step_id)
# SET date_step_end = '2020-03-03'
# WHERE buy_id = 2 AND name_step = 'Транспортировка';
#
# UPDATE buy_step
# JOIN step USING(step_id)
# SET date_step_beg = '2020-03-03'
# WHERE buy_id = 2 AND (
#     step.step_id = (
#         SELECT step_id + 1 FROM step
#         WHERE step_id = (
#             SELECT step_id FROM step
#             WHERE name_step = 'Транспортировка')
#     )
# );


# # # __________________________  task 100  _____________________
# вести студентов, которые сдавали дисциплину «Основы баз данных», указать дату попытки и результат. Информацию вывести по убыванию результатов тестирования.


# SELECT name_student, date_attempt, attempt.result
# FROM subject
# JOIN attempt USING (subject_id)
# JOIN student USING (student_id)
# WHERE name_subject = "Основы баз данных"
# ORDER BY attempt.result DESC;


# # # __________________________  task 101  _____________________
# # Вывести, сколько попыток сделали студенты по каждой дисциплине, а также средний результат попыток, который округлить до 2 знаков после запятой. Под результатом попытки понимается процент правильных ответов на вопросы теста, который занесен в столбец result.  В результат включить название дисциплины, а также вычисляемые столбцы Количество и Среднее. Информацию вывести по убыванию средних результатов
#
# SELECT name_subject, COUNT(attempt.result) AS Количество, ROUND(AVG(attempt.result), 2) AS Среднее
# FROM subject
# LEFT JOIN attempt USING(subject_id)
# GROUP BY subject_id
# ORDER BY Среднее DESC;


# # # __________________________  task 102  _____________________
# # Вывести студентов (различных студентов), имеющих максимальные результаты попыток. Информацию отсортировать в алфавитном порядке по фамилии студента.
# #
# # Максимальный результат не обязательно будет 100%, поэтому явно это значение в запросе не задавать.
#
# SELECT student.name_student, attempt.result
# FROM student
# JOIN attempt USING(student_id)
# WHERE attempt.result = (SELECT MAX(result) FROM attempt)
# ORDER BY student.name_student



# # # __________________________  task 103  _____________________
# # Если студент совершал несколько попыток по одной и той же дисциплине, то вывести разницу в днях между первой и последней попыткой. В результат включить фамилию и имя студента, название дисциплины и вычисляемый столбец Интервал. Информацию вывести по возрастанию разницы. Студентов, сделавших одну попытку по дисциплине, не учитывать.
#
# SELECT DISTINCT name_student, name_subject,
#     DATEDIFF(MAX_attempt_date, MIN_attempt_date) AS Интервал
# FROM student
# JOIN attempt USING(student_id)
# JOIN subject USING(subject_id)
# JOIN (
#     SELECT student_id, subject_id,
#         MIN(date_attempt) AS MIN_attempt_date,
#         MAX(date_attempt) AS MAX_attempt_date
#     FROM attempt
#     GROUP BY student_id, subject_id
#     HAVING COUNT(attempt_id) > 1
# ) AS subquery USING(student_id, subject_id)
# ORDER BY Интервал;



# # # __________________________  task 104  _____________________
# # Студенты могут тестироваться по одной или нескольким дисциплинам (не обязательно по всем). Вывести дисциплину и количество уникальных студентов (столбец назвать Количество), которые по ней проходили тестирование . Информацию отсортировать сначала по убыванию количества, а потом по названию дисциплины. В результат включить и дисциплины, тестирование по которым студенты еще не проходили, в этом случае указать количество студентов 0.
#
# SELECT name_subject, COUNT(DISTINCT(student_id)) AS Количество
# FROM attempt
# RIGHT JOIN subject USING (subject_id)
# GROUP BY name_subject
# ORDER BY Количество DESC, name_subject


# # # __________________________  task 105  _____________________
# # Случайным образом отберите 3 вопроса по дисциплине «Основы баз данных». В результат включите столбцы question_id и name_question.
#
# SELECT question_id, name_question
# FROM question
# JOIN subject USING(subject_id)
# WHERE name_subject = 'Основы баз данных'
# ORDER BY RAND()
# LIMIT 3;


# # # __________________________  task 106  _____________________
# # Вывести вопросы, которые были включены в тест для Семенова Ивана по дисциплине «Основы SQL» 2020-05-17  (значение attempt_id для этой попытки равно 7). Указать, какой ответ дал студент и правильный он или нет (вывести Верно или Неверно). В результат включить вопрос, ответ и вычисляемый столбец  Результат.
#
# SELECT name_question, name_answer, IF(is_correct = 1, "Верно", "Неверно") AS Результат
# FROM question
# JOIN testing USING(question_id)
# JOIN answer USING(answer_id)
# WHERE attempt_id = 7;