from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from aiogram.types import Message

from bot.models import DBBaseModel, UserPay
#from bot.config import PGUSER, PGPORT, PGPASSWORD, PGDB, PGHOST # для Постгреса

#DATABASEURI = f'postgresql+asyncpg://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDB}'
DATABASEURI = 'sqlite+aiosqlite:///paydb'

async_engine = create_async_engine(url=DATABASEURI, echo=True)

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)

session = async_session()


async def opendb() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(DBBaseModel.metadata.create_all)


async def closedb() -> None:
    await async_engine.dispose()


async def adduser(message: Message, label: str) -> None:
    result = await session.execute(select(UserPay).where(UserPay.userid == int(message.from_user.id)))
    user = result.scalars().first()
    if not user:
        newuser = UserPay(userid=int(message.from_user.id), label=label)
        session.add(newuser)
        await session.commit()
    else:
        pass


async def getlabel(userid: int) -> str:
    result = await session.execute(select(UserPay).where(UserPay.userid == userid))
    user = result.scalars().first()
    await session.commit()
    return user.label
