import sqlite3


class Sql:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM sub WHERE id = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO sub ('id', 'date_reg' ,'date_2','date_2_1','date_3', 'date_3_1', 'date_4', 'date_4_1', 'date_5', 'date_5_1', 'date_6', 'date_7', 'date_7_2') VALUES(?,datetime('now', 'localtime'),strftime('%Y-%m-%d %H:%M', 'now','1 days','start of day' ,'16:00'),strftime('%Y-%m-%d %H:%M', 'now','1 days','start of day' ,'17:00'),strftime('%Y-%m-%d %H:%M', 'now','2 days','start of day' ,'16:00'),strftime('%Y-%m-%d %H:%M', 'now','2 days','localtime'),strftime('%Y-%m-%d %H:%M', 'now','3 days','start of day' ,'16:00'),strftime('%Y-%m-%d %H:%M', 'now','3 days','start of day' ,'16 hours','20 minutes'),strftime('%Y-%m-%d %H:%M', 'now','4 days','start of day' ,'13:00'),strftime('%Y-%m-%d %H:%M', 'now','4 days','start of day' ,'13 hours', '20 minutes'),strftime('%Y-%m-%d %H:%M', 'now','5 days','start of day' ,'16:00'),strftime('%Y-%m-%d %H:%M', 'now','6 days','start of day' ,'13:00'),strftime('%Y-%m-%d %H:%M', 'now','6 days','start of day' ,'14:00'))",
                (user_id,))

    def date_2(self):
        """Получаем всех пользователей date_2"""
        with self.connection:
            return self.cursor.execute("SELECT id FROM `sub` WHERE date_2 == strftime('%Y-%m-%d %H:%M', 'now', 'localtime')").fetchall()

    def date_2_1(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute("SELECT id FROM `sub` WHERE date_2_1 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def date_3(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_3 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def date_4(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_4 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def date_4_1(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_4_1 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def date_5(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_5 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def date_5_1(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_5_1 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def date_6(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_6 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def date_7(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_7 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()
    def date_7_2(self):
        """Получаем всех пользователей count 1"""
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM `sub` WHERE date_7_2 = strftime('%Y-%m-%d %H:%M', 'now','localtime')").fetchall()

    def add_message(self, user_id, msg):
        """Сохраняем сообщение от подписчиков"""
        with self.connection:
            return self.cursor.execute("INSERT INTO msg (id, message) VALUES(?,?)",(user_id,msg,))


    def push_msg(self):
        with self.connection:
            result = self.cursor.execute("SELECT id, message FROM msg LIMIT 1").fetchall()
            return result


    def message_exists(self, user_id):
        """Проверяем, есть ли уже сообщение в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM msg WHERE id = ?', (user_id,)).fetchall()
            return bool(len(result))

    def del_sub(self, photo):
        """Удаляем id отвеченые сообщения"""
        with self.connection:
            return self.cursor.execute("DELETE FROM msg WHERE id ==?", (photo,))

    def lenuser(self):
        """Считам сколько людей заходило в бота"""
        with self.connection:
            result = self.cursor.execute("SELECT id FROM sub;").fetchall()
            return len(result)

    def true(self):
        """Обнавляем   голосование"""
        with self.connection:
            return self.cursor.execute("SELECT true FROM stat").fetchall()

    def true_up(self,count):
        with self.connection:
            return self.cursor.execute("UPDATE stat SET true == ? ",(count,))

    def false(self):
        """По голосование"""
        with self.connection:
            return self.cursor.execute("SELECT false FROM stat").fetchall()

    def fals_up(self, count):
        " "
        with self.connection:
            return self.cursor.execute("UPDATE stat SET false == ? ", (count,))


    def check(self):
        """ Провекряем есть ли ссообщения"""
        with self.connection:
            return self.cursor.execute("SELECT message FROM msg").fetchall()

