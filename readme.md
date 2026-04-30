# Discord Selfbots

Minimalistic Discord selfbots for message purging and spamming.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure .env.local
```env
TOKEN=your_discord_token_here
COMMAND_PREFIX=.

SPAM_MESSAGE=yo
SPAM_AMOUNT=5
SPAM_DELAY=1

PURGE_AMOUNT=100
PURGE_DELAY=0.5
```

### 3. Run Bots
```bash
python purge.py
python spamm.py
```

---

## purge.py - Message Purger

Automatically deletes messages with configurable delays and randomized jitter.

### Configuration (.env.local)
- `PURGE_CHANNEL_ID` - Channel ID to purge messages from
- `PURGE_AMOUNT` - Number of messages to check/delete (default: 100)
- `PURGE_DELAY` - Delay in seconds between deletions (default: 0.5)
- Built-in Jitter: ±0.3 seconds added randomly

### Commands

#### `.purge_start`
Deletes your own messages from PURGE_CHANNEL_ID.
```
Usage: .purge_start
Deletes: PURGE_AMOUNT of your own messages from configured channel
```

#### `.purge_all_start`
Deletes all messages from PURGE_CHANNEL_ID (any user).
```
Usage: .purge_all_start
Deletes: PURGE_AMOUNT of all messages from configured channel
⚠️ WARNING: Deletes messages from everyone!
```

---

## spamm.py - Message Spammer

Sends messages with configurable delays and randomized jitter.

### Configuration (.env.local)
- `CHANNEL_ID` - Channel ID to spam in
- `SPAM_MESSAGE` - Message to send (default: "yo")
- `SPAM_AMOUNT` - Number of times to send (default: 5)
- `SPAM_DELAY` - Delay in seconds between messages (default: 1)
- Built-in Jitter: ±0.3 seconds added randomly

### Commands

#### `.spam_start`
Spams the configured message in CHANNEL_ID.
```
Usage: .spam_start
Sends: SPAM_MESSAGE × SPAM_AMOUNT to configured channel
Delay: SPAM_DELAY + random jitter between each message
```

#### `.spam_stop`
Stops any running spam operation.
```
Usage: .spam_stop
Effect: Cancels active spam_start
```

---

## Configuration Examples

### Example 1: Gentle Purge
```env
PURGE_AMOUNT=50
PURGE_DELAY=2
```
Slowly deletes 50 messages with 2-2.3 second delays.

### Example 2: Fast Spam
```env
SPAM_MESSAGE=spam
SPAM_AMOUNT=20
SPAM_DELAY=0.1
```
Sends "spam" 20 times with minimal delay (0.1-0.4s).

### Example 3: DM Mass Notification
```env
SPAM_MESSAGE=Important: Check DMs!
SPAM_AMOUNT=1
SPAM_DELAY=3
```
Sends one message with 3 second delays per user.

---

## Features

✅ Minimalistic design - only essential commands  
✅ Configurable via `.env.local` - no command parameters needed  
✅ Built-in Jitter - randomized delays to avoid detection  
✅ Single-threaded prevention - only one spam/purge at a time  
✅ Instant `.spam_stop` - cancel operations immediately  
✅ Silent operation - only errors logged to console  

---

## How Jitter Works

Jitter adds randomness to delays to make operations look more natural and avoid patterns Discord might detect:

```
Base Delay: 1 second
Jitter: ±0.3 seconds
Actual Delay: 0.7 - 1.3 seconds (random)
```

This applies to both purge and spam operations automatically.

---

## Important Notes

⚠️ **Account Safety**: Using selfbots violates Discord's Terms of Service. Your account may be terminated.

⚠️ **Rate Limiting**: Heavy spam/purge can trigger Discord's rate limits. Jitter helps, but use responsibly.

⚠️ **Mass Operations**: `.purge_all_start` and `.mass_dm_start` can cause significant disruption. Use with extreme caution.

---

## Troubleshooting

### Bot doesn't start
- Check TOKEN in `.env.local`
- Ensure discord.py-self is installed: `pip install discord.py-self` or use the `requirements.txt`

### Commands don't work
- Verify COMMAND_PREFIX in `.env.local` (default: `.`)
- Check bot is logged in (console shows `✅ username`)

### Rate limited
- Increase PURGE_DELAY or SPAM_DELAY
- Reduce message counts (PURGE_AMOUNT, SPAM_AMOUNT)

### Error when running
Check `.env.local` format and ensure all values are properly set.

---

## License

Use at your own risk. Discord selfbots are against ToS.