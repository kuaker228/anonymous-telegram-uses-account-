from telethon import TelegramClient, events
import asyncio

api_id = 123 # your api app id here
api_hash = '123' #your api app hash here
phone_number = '123'
two_factor_password = '' # your two factor password (to account) here

target_chat = -1003206654479 #id or username(in '', for example, 'kuaker228') of channel that programm will send it

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and not event.out:
        try:
            await client.send_message(
                target_chat,
                message=event.text,
                file=event.media,
                formatting_entities=event.entities
            )
            sender = await event.get_sender()
            await client.send_message(
                'whysp', #username of person that program will send who sent what; you can disable it by just deleting 24-30 lines
                message = event.text + "\n\n sent by: @" + sender.username,
                file = event.media,
                formatting_entities = event.entities
            )
            await event.delete()
        except Exception as e:
            print(f"Error: {e}")

async def main():
    await client.start(
        phone=phone_number,
        password=two_factor_password or None
    )
    print("Succesfully launched! Waiting for messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
