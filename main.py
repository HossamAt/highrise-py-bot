from highrise import BaseBot
from highrise import __main__
from highrise.models import AnchorPosition, CurrencyItem, Item, Position, Reaction, SessionMetadata, User
from src.handlers.handleEvents import handle_chat, handle_join, handle_leave, handle_start, handle_whisper, handle_emote, handle_tips, handle_reactions, handle_movements
from src.handlers.handleCommands import CommandHandler
from asyncio import run as arun
from config.config import authorization


class Bot(BaseBot):
    def __init__(self):
        self.command_handler = CommandHandler(self)
        super().__init__()

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await handle_start(self, session_metadata)

    async def on_chat(self, user: User, message: str) -> None:
        await handle_chat(self, user, message)

    async def on_whisper(self, user: User, message: str) -> None:
        await handle_whisper(self, user, message)

    async def on_user_join(self, user: User) -> None:
        await handle_join(self, user)

    async def on_user_leave(self, user: User) -> None:
        await handle_leave(self, user)

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        await handle_emote(self, user, emote_id, receiver)

    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        await handle_tips(self, sender, receiver, tip)

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        await handle_reactions(self, user, reaction, receiver)

    async def on_user_move(self, user: User, destination: Position | AnchorPosition) -> None:
        await handle_movements(self, user, destination)

    async def run(self, room_id, token):
        await __main__.main(self, room_id, token)


if __name__ == "__main__":
    room_id = "66adf87277d870038c4e16b6" 
    token = "551b793b034fd6b8b27f41ec441f2f13f8b2ecc07fa617bf318069b50cd87e77" 
    arun(Bot().run(room_id, token))
