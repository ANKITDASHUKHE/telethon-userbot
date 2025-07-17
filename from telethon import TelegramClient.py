from telethon import TelegramClient, events

# Replace with your own API values
api_id = 25096077
api_hash = '9ef9fd27e5e6eea3cbc27c964daa6ec8'
session_name = 'ankit_userbot'

# Target group (you must be a member)
target_group = 'x_Accounts_buysale'

# Auto-reply message
auto_reply_message = (
    "🚨 WARNING: This group has been reported for scamming users. "
    "Do NOT share personal info or bank details. "
    "Report to @notoscam or https://t.me/spambot 🚨"
)

# Initialize the client
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=target_group))
async def handler(event):
    # Avoid replying to your own messages
    sender = await event.get_sender()
    me = await client.get_me()
    if sender.id == me.id:
        return

    print(f"[+] Detected new message from {sender.username or sender.id}: {event.message.text[:30]}")
    
    try:
        await client.send_message(target_group, auto_reply_message)
        print("[+] Sent auto-reply.")
    except Exception as e:
        print("[-] Error sending message:", e)

print("[*] Starting bot... Waiting for new messages.")
client.start()
client.run_until_disconnected()