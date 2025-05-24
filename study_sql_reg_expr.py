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
