from sqlalchemy.orm import Mapped, mapped_column


class UserDAO(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    steamid: Mapped[str] = mapped_column()
    default_step_key: Mapped[int] = mapped_column(default=0)
    default_ref_key: Mapped[int] = mapped_column(default=0)

class BlacklistDAO(Base):
    __tablename__ = "blacklist"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    steamid: Mapped[str] = mapped_column()

class OrderDao(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    bpid: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    max_key: Mapped[int] = mapped_column()
    max_key: Mapped[int] = mapped_column()
    step_key: Mapped[int] = mapped_column(default=1)
    step_trf: Mapped[int] = mapped_column(default=1)
    is_active: Mapped[bool] = mapped_column(default=False)

 