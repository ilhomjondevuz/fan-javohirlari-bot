import asyncpg
from environs import Env

env = Env()
env.read_env()


class Database:
    def __init__(self):
        self.connection: asyncpg.Connection | None = None

    async def connect(self) -> None:
        self.connection = await asyncpg.connect(
            host=env.str("DATABASE_HOST"),
            user=env.str("DATABASE_USER"),
            password=env.str("DATABASE_PASSWORD"),
            database=env.str("DATABASE_NAME"),
            port=env.int("DATABASE_PORT"),
        )

    def _check_connection(self):
        if not self.connection:
            raise RuntimeError("Database is not connected")

    async def select_user(self, tg_id: str) -> dict | None:
        self._check_connection()
        record = await self.connection.fetchrow(
            "SELECT * FROM users WHERE tg_id=$1",
            tg_id
        )
        if record:
            return dict(record)  # Record → dict
        return None

    async def insert_user(self, fullname, phone, username, passport, tg_id, language):
        tg_id = str(tg_id)  # stringga o'zgartirish
        query = """
                INSERT INTO users (fullname, phone, username, passport, tg_id, language)
                VALUES ($1, $2, $3, $4, $5, $6) \
                """
        await self.connection.execute(query, fullname, phone, username, passport, tg_id, language)

    async def update_user(self, fullname, phone, username, passport, tg_id):
        self._check_connection()
        await self.connection.execute(
            """
            UPDATE users
            SET fullname=$1, phone=$2, username=$3, passport=$4
            WHERE tg_id=$5
            """,
            fullname,
            phone,
            username,
            passport,
            tg_id
        )

    async def select_directions(self) -> list[dict]:
        self._check_connection()
        query = "SELECT * FROM directions"
        records = await self.connection.fetch(query)
        return [dict(record) for record in records]

    async def change_language(self, tg_id, language):
        self._check_connection()
        query = """
        UPDATE users SET language=$1 WHERE tg_id=$2
        """
        await self.connection.execute(query, language, tg_id)

    async def close(self):
        if self.connection:
            await self.connection.close()


db = Database()