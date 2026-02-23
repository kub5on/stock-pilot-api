import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base, TimestampMixin

class Watchlist(Base, TimestampMixin):
    __tablename__ = 'watchlists'

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="watchlists")
    watchlist_items: Mapped[list["WatchlistItem"]] = relationship("WatchListItem", back_populates="watchlist")

class WatchlistItem(Base):
    __tablename__ = 'watchlist_items'

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4
    )
    watchlist_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('watchlists.id', ondelete='CASCADE'),
        nullable=False
    )
    symbol: Mapped[str] = mapped_column(String(10), nullable=False)
    added_at: Mapped[datetime] = mapped_column(server_default=func.now())

    watchlist: Mapped["Watchlist"] = relationship("Watchlist", back_populates="watchlist_items")

