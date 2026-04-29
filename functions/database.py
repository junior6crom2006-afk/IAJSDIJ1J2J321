import datetime
import sqlite3
import random
import string
import asyncio
from typing import Union, Optional, Dict
from .variables import OWNER_ID, NAME_BOT, COMPA_ID
import threading

class Database:
    _local = threading.local()
    
    BOT_TABLE = "Users"
    BOT_KEYS_TABLE = "Keys"
    BOT_GROUPS = "Groups"
    ID_OWNER = OWNER_ID

    ## MAIN
    def __new__(cls):
        if not hasattr(cls._local, "instance"):
            cls._local.instance = super(Database, cls).__new__(cls)
            cls._local.instance.connection = sqlite3.connect(f"db/{NAME_BOT}.db")
            cls._local.instance.cursor = cls._local.instance.connection.cursor()
            cls._local.instance.__create_tables()
            cls._local.instance.__initialize_owner()
        return cls._local.instance

    async def reset_expired_memberships_periodically(self):
        while True:
            self.reset_expired_memberships()
            await asyncio.sleep(3600)  # Espera una hora antes de la siguiente verificación

    def __create_tables(self) -> None:
        table_defs = {
            self.BOT_TABLE: [
                ("ID", "VARCHAR(25) NOT NULL PRIMARY KEY"),
                ("USERNAME", "VARCHAR(32) DEFAULT NULL UNIQUE"),
                ("NICK", "VARCHAR(32) DEFAULT '¿?'"),
                ("RANK", "VARCHAR(15) DEFAULT 'user'"),
                ("STATE", "VARCHAR(12) DEFAULT 'free'"),
                ("MEMBERSHIP", "VARCHAR(15) DEFAULT 'free user'"),
                ("EXPIRATION", "varchar(20) DEFAULT NULL"),
                ("ANTISPAM", "INT(3) DEFAULT 60"),
                ("CREDITS", "INT(15) DEFAULT 0"),
                ("REGISTERED", "TEXT NOT NULL"),
                ("CHECKS", "INT(15) DEFAULT 0"),
            ],
            self.BOT_KEYS_TABLE: [
                ("BOT_KEY", "VARCHAR(30) NOT NULL PRIMARY KEY"),
                ("EXPIRATION", "TEXT NOT NULL"),
                ("PLAN", "VARCHAR(15) DEFAULT 'Premium'"),
            ],
            self.BOT_GROUPS: [
                ("ID", "VARCHAR(30) NOT NULL PRIMARY KEY"),
                ("EXPIRATION", "TEXT NOT NULL"),
                ("PROVIDER", "VARCHAR(30) NOT NULL"),
            ],
            "Gates": [
                ("COMANDO", "VARCHAR(10) NOT NULL PRIMARY KEY"),
                ("NOMBRE", "VARCHAR(50) NOT NULL"),
                ("ESTADO", "VARCHAR(10) DEFAULT 'ON'"),
                ("RAZON", "TEXT DEFAULT NULL"),
                ("ULTIMA_REVISION", "DATETIME DEFAULT CURRENT_TIMESTAMP"),
                ("TIPO", "VARCHAR(10) DEFAULT 'CCN'"),
                ("PREMIUM", "BOOLEAN DEFAULT 0")
            ]
        }

        for table, columns in table_defs.items():
            self.__create_table(table, columns)

        self.connection.commit()

    def __create_table(self, table_name: str, columns: list) -> None:
        column_defs = ", ".join(f"{name} {defn}" for name, defn in columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name}({column_defs})"
        self.cursor.execute(query)

    def __initialize_owner(self) -> None:
        owner_ids = [OWNER_ID]
        for owner_id in owner_ids:
            if not self.is_owner(owner_id):
                # Si el usuario ya existe pero no es owner, promoverlo
                user_data = self.cursor.execute(
                    f"SELECT ID FROM {self.BOT_TABLE} WHERE ID=?", (int(owner_id),)
                ).fetchone()
                if user_data:
                    self.cursor.execute(
                        f"UPDATE {self.BOT_TABLE} SET RANK='owner', MEMBERSHIP='Premium', ANTISPAM=30, EXPIRATION='9999-12-31 23:59:59' WHERE ID=?",
                        (int(owner_id),)
                    )
                    self.connection.commit()
                else:
                    self.promote_to_owner(owner_id)
                    self.add_premium_membership(owner_id, "9999-12-31 23:59:59")

    ## ADD
    def add_premium_membership(self, user_id: int, expiration_date: str, plan: str = "Premium") -> Optional[str]:
        user_id = int(user_id)
        user_data = self.cursor.execute(
            f"SELECT MEMBERSHIP FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()

        if user_data is None:
            return None

        current_plan = user_data[0]
        new_plan = plan.capitalize() if current_plan.lower() in ["free user", "free"] or plan.lower() == "vip" else current_plan
        antispam = 15 if new_plan.lower() == "vip" else 30

        # Actualiza la fecha de expiración, membresía y antispam
        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET EXPIRATION=?, MEMBERSHIP=?, ANTISPAM=? WHERE ID=?",
            (expiration_date, new_plan, antispam, user_id),
        )
        self.connection.commit()
        return expiration_date

    def register_user(self, user_id: int, username: str) -> None:
        try:
            user_id = int(user_id)
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(
                f"INSERT INTO {self.BOT_TABLE} (ID, USERNAME, REGISTERED) VALUES (?, ?, ?)",
                (user_id, username, time),
            )
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def gen_key(self, days: int, plan: str = "Premium") -> tuple:
        expire_day = (
            datetime.datetime.now() + datetime.timedelta(days=int(days))
        ).strftime("%Y-%m-%d %H:%M:%S")
        key = f"ZYREX-" + "".join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
        self.cursor.execute(
            f"INSERT INTO {self.BOT_KEYS_TABLE} (BOT_KEY, EXPIRATION, PLAN) VALUES (?, ?, ?)",
            (key, expire_day, plan),
        )
        self.connection.commit()
        return key, expire_day

    def add_group(self, chat_id: int, days: int, username: str) -> Union[str, bool]:
        try:
            chat_id = int(chat_id)
            expiration_time = (
                datetime.datetime.now() + datetime.timedelta(days=days)
            ).strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(
                f"INSERT INTO {self.BOT_GROUPS} (ID, EXPIRATION, PROVIDER) VALUES (?, ?, ?)",
                (chat_id, expiration_time, username),
            )
            self.connection.commit()
        except sqlite3.IntegrityError:
            self.cursor.execute(
                f"UPDATE {self.BOT_GROUPS} SET EXPIRATION=?, PROVIDER=? WHERE ID=?",
                (expiration_time, username, chat_id),
            )
            self.connection.commit()
        return expiration_time

    ## REMOVE
    def remove_expireds_users(self) -> None:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        table_queries = [
            {"table": self.BOT_TABLE, "remove_function": self.rename_premium},
            {"table": self.BOT_GROUPS, "remove_function": self.remove_group},
        ]

        for query_data in table_queries:
            query_format = f"SELECT ID, EXPIRATION FROM {query_data['table']} WHERE EXPIRATION IS NOT NULL"
            data = self.cursor.execute(query_format)
            expireds = filter(lambda x: x[1] < now, data.fetchall())

            for data_item in expireds:
                query_data["remove_function"](data_item[0])

    def reset_expired_memberships(self) -> None:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expired_users = self.cursor.execute(
            f"SELECT ID FROM {self.BOT_TABLE} WHERE EXPIRATION IS NOT NULL AND EXPIRATION < ?", (now,)
        ).fetchall()

        for user_id in expired_users:
            self.rename_premium(user_id[0])


        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET EXPIRATION=NULL WHERE EXPIRATION IS NOT NULL AND EXPIRATION < ?", (now,)
        )
        self.connection.commit()

    def remove_group(self, chat_id: str) -> Optional[int]:
        data = self.cursor.execute(
            f"SELECT EXPIRATION FROM {self.BOT_GROUPS} WHERE ID=?",
            (chat_id,),
        ).fetchone()
        if data is None:
            return None

        self.cursor.execute(
            f"DELETE FROM {self.BOT_GROUPS} WHERE ID=?",
            (chat_id,),
        )
        self.connection.commit()
        return 1


    def user_has_credits(self, user_id: int) -> bool:
        credits_user = self.cursor.execute(
            f"SELECT CREDITS FROM {self.BOT_TABLE} WHERE ID=?",
            (user_id,),
        ).fetchone()[0]
        return credits_user > 0
    
    def add_credits(self, user_id: int, credits: int) -> None:
        if credits <= 0:
            return
        credits_user_result = self.cursor.execute(
            "SELECT CREDITS FROM {} WHERE ID=?".format(self.BOT_TABLE),
            (user_id,),
        ).fetchone()
        if credits_user_result is None:
            return
        credits_user = credits_user_result[0]
        new_credits = credits_user + credits
        self.cursor.execute(
            "UPDATE {} SET CREDITS=? WHERE ID=?".format(self.BOT_TABLE),
            (new_credits, user_id),
        )
        self.connection.commit()

    def remove_credits(self, user_id: int, credits: int) -> None:
        if credits <= 0:
            return
        credits_user = self.cursor.execute(
            f"SELECT CREDITS FROM {self.BOT_TABLE} WHERE ID=?",
            (user_id,),
        ).fetchone()[0]
        new_credits = credits_user - credits if credits_user > 0 else 0
        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET CREDITS=? WHERE ID=?",
            (new_credits, user_id),
        )
        self.connection.commit()

    def increase_checks(self, user_id: int, quantity: int = 1) -> bool | None:
        user_id, quantity = map(int, (user_id, quantity))

        user_data = self.cursor.execute(
            f"SELECT CHECKS FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()

        if user_data is None:
            return None

        checks = user_data[0] + quantity
        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET CHECKS=? WHERE ID=?",
            (checks, user_id),
        )
        self.connection.commit()
        return True




    def update_colum(self, user_id: int, column: str, value) -> bool | None:
        user_id = int(user_id)

        user_data = self.cursor.execute(
            f"SELECT USERNAME FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()

        if user_data is None:
            return None

        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET {column}=? WHERE ID=?",
            (value, user_id),
        )
        self.connection.commit()
        return True

    ## UPDATE
    def rename_premium(self, user_id: int) -> Optional[int]:
        user_id = int(user_id)
        user_data = self.cursor.execute(
            f"SELECT MEMBERSHIP FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()
        if user_data is None:
            return None

        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET MEMBERSHIP='free user', RANK='user', ANTISPAM=60, EXPIRATION=NULL WHERE ID=?",
            (user_id,),
        )
        self.connection.commit()
        return 1

    def unban_or_ban_user(self, user_id: int, ban: bool = True) -> Optional[int]:
        user_id = int(user_id)
        user_data = self.cursor.execute(
            f"SELECT MEMBERSHIP FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()
        if user_data is None:
            return None
        status = "ban" if ban else "free"

        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET RANK='user', MEMBERSHIP='free user', ANTISPAM=60, CREDITS=0, EXPIRATION=NULL, STATE=? WHERE ID=?",
            (status, user_id),
        )
        self.connection.commit()
        return 1

    def claim_key(self, key: str, user_id: int) -> Optional[dict]:
        data = self.cursor.execute(
            f"SELECT EXPIRATION, PLAN FROM {self.BOT_KEYS_TABLE} WHERE BOT_KEY=?",
            (key,),
        ).fetchone()
        if data is None:
            return None
        
        expiration_time, plan = data
        antispam = 30 if plan.lower() == "premium" else 15
        
        self.cursor.execute(
        f"UPDATE {self.BOT_TABLE} SET MEMBERSHIP=?, ANTISPAM=?, EXPIRATION=? WHERE ID=?", 
            (plan, antispam, expiration_time, user_id),
        )
        self.cursor.execute(
            f"DELETE FROM {self.BOT_KEYS_TABLE} WHERE BOT_KEY=?", (key,)
        )
        self.connection.commit()
        return {"expiration": expiration_time, "plan": plan}

    ## GET
    def __get_info(self, ID: int, group: bool = False) -> list:
        ID = int(ID)
        table = self.BOT_GROUPS if group else self.BOT_TABLE
        data = self.cursor.execute(f"SELECT * FROM {table} WHERE ID=?", (ID,))
        data = data.fetchone()
        return data

    def get_info_user(self, user_id: int) -> Dict[str, Union[str, int]] | None:
        user_data = self.__get_info(user_id)
        return (
            {
                "ID": user_data[0],
                "USERNAME": user_data[1],
                "NICK": user_data[2],
                "RANK": user_data[3],
                "STATE": user_data[4],
                "MEMBERSHIP": user_data[5],
                "EXPIRATION": user_data[6],
                "ANTISPAM": user_data[7],
                "CREDITS": user_data[8],
                "REGISTERED": user_data[9],
                "CHECKS": user_data[10],
            }
            if user_data
            else None
        )

    def get_info_group(self, chat_id: int) -> Dict[str, Union[str, int]] | None:
        group_data = self.__get_info(chat_id, True)
        if not group_data:
            return None
        return {
            "ID": group_data[0],
            "EXPIRATION": group_data[1],
        }

    def get_chats_ids(self) -> list:
        users_data = self.cursor.execute(f"SELECT ID FROM {self.BOT_TABLE}")
        users_data = users_data.fetchall()
        chats_id_data = self.cursor.execute(f"SELECT ID FROM {self.BOT_GROUPS}")
        users_data.extend(chats_id_data.fetchall())
        return [data[0] for data in users_data]

    ## IS
    def __is_rank(self, user_id: int, rank: str) -> bool:
        user_id = int(user_id)
        user_data = self.cursor.execute(
            f"SELECT RANK FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()
        return str(user_data[0]).lower() == rank if user_data else False

    def is_owner(self, user_id: int) -> bool:
        return self.__is_rank(user_id, "owner")

    def is_seller(self, user_id: int) -> bool:
        return self.__is_rank(user_id, "seller")
    
    def is_admin(self, user_id: int) -> bool:
        return self.__is_rank(user_id, "admin")

    def is_seller_or_owner(self, user_id) -> bool:
        return self.is_owner(user_id) or self.is_seller(user_id)
    
    def is_premium(self, user_id: int) -> bool:
        user_data = self.cursor.execute(
            f"SELECT MEMBERSHIP FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()
        if not user_data: return False
        membership = str(user_data[0]).lower()
        return membership in ["premium", "vip"]

    def is_vip(self, user_id: int) -> bool:
        user_data = self.cursor.execute(
            f"SELECT MEMBERSHIP FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()
        return str(user_data[0]).lower() == "vip" if user_data else False

    def is_authorized(self, user_id: int, chat_id: int) -> bool:
        user_id = int(user_id)
        chat_id = int(chat_id)

        if self.is_premium(user_id) or self.group_authorized(chat_id):
            return True
        return False

    def is_ban(self, user_id: int) -> bool:
        user_id = int(user_id)
        user_data = self.cursor.execute(
            f"SELECT STATE FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()
        return str(user_data[0]).lower() == "ban" if user_data else False

    ## SET
    def set_nick(self, user_id: int, nick: str) -> bool | None:
        user_id = int(user_id)

        user_data = self.cursor.execute(
            f"SELECT NICK FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()

        if user_data is None:
            return None

        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET NICK=? WHERE ID=?",
            (nick, user_id),
        )
        self.connection.commit()
        return True

    def set_antispam(self, user_id: int, antispam: int) -> bool | None:
        user_id, antispam = map(int, (user_id, antispam))

        user_data = self.cursor.execute(
            f"SELECT ANTISPAM FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()

        if user_data is None:
            return None

        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET ANTISPAM=? WHERE ID=?",
            (antispam, user_id),
        )
        self.connection.commit()
        return True

    ## PROMOTE
    def __promote(self, user_id: int, rank: str) -> bool | None:
        user_id = int(user_id)
        user_data = self.cursor.execute(
            f"SELECT RANK FROM {self.BOT_TABLE} WHERE ID=?", (user_id,)
        ).fetchone()

        if user_data is None:
            return None

        self.cursor.execute(
            f"UPDATE {self.BOT_TABLE} SET RANK=? WHERE ID=?",
            (rank, user_id),
        )
        self.connection.commit()
        return True

    def promote_to_seller(self, user_id: int) -> bool | None:
        return self.__promote(user_id, "seller")

    def promote_to_owner(self, user_id: int) -> bool | None:
        return self.__promote(user_id, "owner")

    def promote_to_admin(self, user_id: int) -> bool | None:
        return self.__promote(user_id, "admin")

    def promote_to_keyword_extractor(self, user_id: int) -> bool | None:
        return self.__promote(user_id, "keyword_extractor")

    def is_keyword_extractor(self, user_id: int) -> bool:
        return self.__is_rank(user_id, "keyword_extractor")

    def is_authorized_kwex(self, user_id: int) -> bool:
        return self.is_owner(user_id) or self.is_seller(user_id) or self.is_keyword_extractor(user_id)

    ## ?
    def group_authorized(self, chat_id: int) -> bool:
        chat_id = int(chat_id)
        data = self.cursor.execute(
            f"SELECT EXPIRATION FROM {self.BOT_GROUPS} WHERE ID=?",
            (chat_id,),
        ).fetchone()
        expiration = data
        if expiration is None:
            return False
        return True

    def user_has_credits(self, user_id: int) -> bool:
        credits_user = self.cursor.execute(
            f"SELECT CREDITS FROM {self.BOT_TABLE} WHERE ID=?", (user_id,),
        ).fetchone()[0]
        return credits_user > 0

    ## EXIT
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.commit()

    def registrar_gate(self, comando: str, nombre: str, tipo: str = "CCN", premium: bool = False) -> bool:
        try:
            self.cursor.execute(
                """
                INSERT OR IGNORE INTO Gates 
                (COMANDO, NOMBRE, ESTADO, TIPO, PREMIUM) 
                VALUES (?, ?, 'ON', ?, ?)
                """,
                (comando, nombre, tipo, premium)
            )
            self.connection.commit()
            return True
        except:
            return False

    def actualizar_estado_gate(self, comando: str, estado: str, razon: str = None) -> bool:
        try:
            self.cursor.execute(
                """
                UPDATE Gates 
                SET ESTADO = ?, 
                    RAZON = ?, 
                    ULTIMA_REVISION = CURRENT_TIMESTAMP 
                WHERE COMANDO = ?
                """,
                (estado, razon, comando)
            )
            self.connection.commit()
            return True
        except:
            return False

    def obtener_info_gate(self, comando: str) -> dict:
        data = self.cursor.execute(
            "SELECT * FROM Gates WHERE COMANDO = ?",
            (comando,)
        ).fetchone()
        
        if data:
            return {
                "comando": data[0],
                "nombre": data[1],
                "estado": data[2],
                "razon": data[3],
                "ultima_revision": data[4],
                "tipo": data[5],
                "premium": bool(data[6])
            }
        return None

    def obtener_conteo_gates(self) -> dict:
        return {
            "online": self.cursor.execute("SELECT COUNT(*) FROM Gates WHERE ESTADO = 'ON'").fetchone()[0],
            "offline": self.cursor.execute("SELECT COUNT(*) FROM Gates WHERE ESTADO = 'OFF'").fetchone()[0],
            "ccn": self.cursor.execute("SELECT COUNT(*) FROM Gates WHERE TIPO = 'CCN'").fetchone()[0],
            "auth": self.cursor.execute("SELECT COUNT(*) FROM Gates WHERE TIPO = 'AUTH'").fetchone()[0],
            "charged": self.cursor.execute("SELECT COUNT(*) FROM Gates WHERE TIPO = 'CHARGED'").fetchone()[0]
        }