from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN: Final = "6389988766:AAHu3HD3HEEAuQxxSaCdul9RX4fqPRyjwIo"
BOT_USERNAME: Final = "@KFUPM_2023_Bot"


# #Groups
ME201_w=[["ME201","https://chat.whatsapp.com/DIHDaLihVdNFnjAIIjvfse"],["CE202","https://chat.whatsapp.com/FMNa24AzDQxDd0emq9Ds2R"]]


#Commands this is for private chats
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there!, Send me Your Course Name or Your Course Number...")

#This is for both group and private chats
def handle_response(text: str) -> str:
    processed:str = text.lower()

    if "me203 group" == processed or "قروب me203"== processed:
        return f"here is the ME203 Group {ME203_w}"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if BOT_USERNAME in text:
        text: str = text.replace(BOT_USERNAME, "")

    response: str = handle_response(text)

    print("Bot", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update ({update} caused error {context.error} )")

if __name__ == '__main__':

    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    # pools the bot
    print("polling...")
    app.run_polling(poll_interval=3)



"""
Sended Code From Rashid
"""
# from typing import Final
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# TOKEN: Final = "6623233596:AAGx4T9YXqa23FBvbohiIqheRgXLPWFoyEI"
# BOT_USERNAME: Final = "@STKFUPM_Update_Bot"

# #Groups 
# ME201_w="https://chat.whatsapp.com/DIHDaLihVdNFnjAIIjvfse"
# CE202_w="https://chat.whatsapp.com/FMNa24AzDQxDd0emq9Ds2R"
# ME203_w="https://chat.whatsapp.com/LOx9wlbPDcOKYm05EXVpTo"
# ME204_w="https://chat.whatsapp.com/IK7rTTvjeYOAgOzhwuryZ7"
# ME210_w="https://chat.whatsapp.com/KzzI8hUq83DDqFw0a8ahlT"
# ME216_w="https://chat.whatsapp.com/Jw5KDNiabcM7qrPpnoe41a"
# ME218_w="https://chat.whatsapp.com/D7T1jb5UekGAEN3YlpmfMb"
# EE234_w="https://chat.whatsapp.com/LYB0JmCtylCKoWL98g8K0L"
# ME301_w="https://chat.whatsapp.com/Cr6ENoJYucvG33shixCsuF"
# ME302_w="https://chat.whatsapp.com/CNvhfl53Ceq5V8QHAHKgRZ"
# ME311_w="https://chat.whatsapp.com/Ikt1Dlmg6KbDb5vop1Fwf5"
# ME315_w="https://chat.whatsapp.com/GSDIWF2NzlQEn2529JlLOI"
# ME322_w="https://chat.whatsapp.com/DDRzwgon8pq9PPTdifBDHk"
# ME401_w="https://chat.whatsapp.com/J3RkvZi6a8A122OKnoTYMK"
# ME411_w="https://chat.whatsapp.com/GahEL8Jyb9KAdX9b6IyiJO"
# ME415_w="https://chat.whatsapp.com/ICo4SXlW99sHmI8Hj1oLht"
# ME427_w="https://chat.whatsapp.com/FYBJowxW7Js8X3S9AzUC67"
# ME438_w="https://chat.whatsapp.com/HESHoGurTWQ69GATT7w9Zn"
# ME444_w="https://chat.whatsapp.com/FeT0O93LNKXGih96qAFXNu"
# ME482_w="https://chat.whatsapp.com/GfiMPtNcY2nBPjVditK2qu"
# ME489_w="https://chat.whatsapp.com/JyuuBQdnFSs3KuTKlvHEYD"
# ME495_w="https://chat.whatsapp.com/ByEALGncgoyFHQaVOZYRN1"
# MATH101_w="https://chat.whatsapp.com/JF2JAavHy8XCXzxw7iQS7L"
# MATH102_w="https://chat.whatsapp.com/B5YppwAaXyC2xJv56oxU38"
# PHYS101_w="https://chat.whatsapp.com/DNOe5RDYXYlDPDquCyFpJm"
# PHYS102_w="https://chat.whatsapp.com/L98WP5RQ11V53VZYVLnjgG"
# CHEM101_w="https://chat.whatsapp.com/FTyJrV1aGsD32PV9a9JWTv"
# CHEM102_w="https://chat.whatsapp.com/DdL4qNj5mIp5alfm4VM2SV"
# English101_w="https://chat.whatsapp.com/K90CNUHJ0HRJHzQD62wyBZ"
# English102_w="https://chat.whatsapp.com/KtrcbhHyVSo5vIqrIBnZ5H"
# ICS104_w="https://chat.whatsapp.com/Fy6KBd5r58y6BkqQYbfR2K"
# IAS111_w="https://chat.whatsapp.com/I1ZoGnTBfRIHBt3lwwcmzg"
# IAS121_w="https://chat.whatsapp.com/J6bzBB61mnOEeYeqvwI0hl"

# #Commands this is for private chats
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello there!")

# #This is for both group and private chats
# def handle_response(text: str) -> str:
#     processed:str = text.lower()
    
#     if "me203 group" == processed or "قروب me203"== processed:
#         return f"here is the ME203 Group {ME203_w}"
    
    
    
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text
        
#     if BOT_USERNAME in text:
#         text: str = text.replace(BOT_USERNAME, "")
        
#     response: str = handle_response(text)
    
#     print("Bot", response)
#     await update.message.reply_text(response)
    
    
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f"update ({update} caused error {context.error} )")
    
# if __name__ == '__main__':
    
#     print("Starting bot...")
#     app = Application.builder().token(TOKEN).build()
    
#     #Commands
#     app.add_handler(CommandHandler('start', start_command))
    
#     #Messages
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
#     #Errors
#     app.add_error_handler(error)
    
#     # pools the bot
#     print("polling...")
#     app.run_polling(poll_interval=3)

