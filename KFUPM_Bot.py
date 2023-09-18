import pandas as pd
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, filters, ContextTypes, MessageHandler, CallbackQueryHandler
from math import ceil

TOKEN = "6429830845:AAFRE-CV-DkmHTbvujDYKSQXd-FXZbGMksA"
BOT_USERNAME = "@TagrebyBot"

# TOKEN = '6389988766:AAHu3HD3HEEAuQxxSaCdul9RX4fqPRyjwIo'
# BOT_USERNAME = "@KFUPM_2023_Bot"

df = pd.read_csv('Telegram_Bot_KFUPM/Telegram Bot data.csv', delimiter=',', index_col='Course Name')
df_Faculty = pd.read_csv('Telegram_Bot_KFUPM/KFUPM_Faculty.csv', delimiter=',', index_col='Professors')

global COURSE_NAME
FACULTY = []

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there!, I am your KFUPM Bot👋\nSend me Your Course Name e.g., MATH101")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("KFUPM Bot is in your service\n\nYou should write your course name with the number in this format: ICS104.")


# Input Message (From User) In Group
def handle_response_inGroup(text: str) -> str:

    # Filter the message from bot's id
    if BOT_USERNAME in text:
        text = text.replace(BOT_USERNAME, "")
    text = text.upper()

    if text in df.index:
        return "CourseRequest"
    elif text in df_Faculty.index:
        return "FacultyRequest"
    else:
        return "IgnoreMessage"

# Input Message (From User) In Private
def handle_response_inPrivate(text: str) -> str:

    # This Function needs More Improvements
    text: str = text.upper()
    if text in df.index:
        return "CourseRequest"
    elif text in df_Faculty.index:
        return "FacultyRequest"
    elif text != "/START" and text != "/HELP":
        return "Explianation"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global COURSE_NAME  
    global FACULTY
    Explian_Message = "It seems that you sent an unapporpiate message, This Course does not Exist\nPlease type /help."
    Message = update.message.text

    if update.message.chat_id == update.effective_user.id: # In-Private Message
        input = handle_response_inPrivate(Message)
    else:
        input = handle_response_inGroup(Message)
    
    # Sending the correct response depending on the message sent by user
    if input == "IgnoreMessage":
        "Do No Thing"
    elif input == "CourseRequest":
        COURSE_NAME = Message.upper()
        FACULTY = df.loc[COURSE_NAME, 'Faculty'].__str__().split('/')
        await update.message.reply_text(text=COURSE_NAME, reply_markup=generate_keyboard_layout(COURSE_NAME))
    elif input == "FacultyRequest":
        "New Feature"
    elif input == "Explianation":
        await update.message.reply_text(Explian_Message)


# Return The correct keyboard layout depending on the request
def generate_keyboard_layout(request: str) -> InlineKeyboardMarkup:
    errorNum = 0
    global COURSE_NAME
    global FACULTY

    layout = []

    if request == "Details":
        # Layout For Details
        layout = [[InlineKeyboardButton("Groups", callback_data="Groups")],
                   [InlineKeyboardButton("Faculty",callback_data="Faculty Page: 1")],
                   [InlineKeyboardButton("Drive Link", callback_data="Drive Link", url=df.loc[COURSE_NAME,'Drive Link'])],
                   [InlineKeyboardButton("Course Info", callback_data="Course Info")],
                   [InlineKeyboardButton("Return To Menu 🔙", callback_data="Click on Details")]]

    elif request == "Groups":
        # Layout For Groups
        layout = [[InlineKeyboardButton("Telegram Group", callback_data= "Telegram Group",url=df.loc[COURSE_NAME, 'Telegram Group URL'])],
                   [InlineKeyboardButton("WhatsApp Group", callback_data= "WhatsApp Group", url=df.loc[COURSE_NAME, 'Whatsapp Group URL'])],
                   [InlineKeyboardButton("Return To Menu 🔙", callback_data="Details")]]

    elif "Faculty" in request:
        # Dynamic Layout For Faculty
        MAX_NUM_OF_PROF_PER_PAGE = 3
        numOfProf = FACULTY.__len__()   # Number of Proffesors we have in the file
        pageNum = int(request[-1])  # Tracing the page number by this variable helps as in the generation 

        last_index = (pageNum) * MAX_NUM_OF_PROF_PER_PAGE
        index = (pageNum - 1) * MAX_NUM_OF_PROF_PER_PAGE

        # Adding the faculty depending on the number of pages. Condtion1: To Avoid-> to cover all prof, Condition2: out of bound index
        while index < numOfProf and index < last_index:
            layout.append([InlineKeyboardButton(FACULTY[index], callback_data= FACULTY[index],url=df_Faculty.loc[FACULTY[index], 'URL'])])
            index += 1

        # if we still have more profs in the list, add next page button
        if index < numOfProf:
            layout.append([InlineKeyboardButton("Next", callback_data="Faculty Page: "+str(pageNum+1))])

        # if the page number equals 1, the button must return to details
        if pageNum == 1:
            layout.append([InlineKeyboardButton("Return🔙", callback_data="Details")])
        else:
            layout.append([InlineKeyboardButton("Return🔙", callback_data="Faculty Page: "+str(pageNum-1))])      
            

    elif request == "Course Info" or request == "Try Again":
        # Layout For Course Info
        layout = [[InlineKeyboardButton("STKFUPM", callback_data= "STKFUPM",url=df.loc[COURSE_NAME, 'Course info STKFUPM URL'])],
                   [InlineKeyboardButton("Overall Info", callback_data= "Overall Info")],
                   [InlineKeyboardButton("Study Tips", callback_data= "Study Tips")],
                   [InlineKeyboardButton("Return To Menu 🔙", callback_data="Details")]]
        
    elif (request == "Overall Info" or request == "Study Tips") and errorNum == 1:
        layout = [[InlineKeyboardButton("You Can Not Use This Feature! \nClick On This Link, Then Click: (START) \nhttps://t.me/TagrebyBot \nThen Try Again", callback_data= "AAA")],
                    [InlineKeyboardButton("Try Again", callback_data="Try Again")]]
    
    else: # request = Course Name
        layout = [[InlineKeyboardButton("Details", callback_data="Details")]]

    show = InlineKeyboardMarkup(layout)

    return show


async def update_Menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global COURSE_NAME

    query = update.callback_query
    request = query.data
    show: InlineKeyboardMarkup = generate_keyboard_layout(request)

    # Special If Condition For In Private Needs
    if request == "Overall Info":
        await context.bot.send_message(chat_id=update.effective_user.id,
                                       text= df.loc[COURSE_NAME, 'Course overall info'])
    elif request == "Study Tips":
        await context.bot.send_message(chat_id=update.effective_user.id,
                                       text=df.loc[COURSE_NAME, 'Study Tips'])
    await query.edit_message_text(text=request, reply_markup=show)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.error.__str__() == "Forbidden: bot can't initiate conversation with a user":
        await context.bot.send_message(chat_id=context._chat_id, text='Please send "/Start" to me in "https://t.me/TagrebyBot",\nthen try again.')


if __name__ == '__main__':
    print("Starting bot...")
    app = ApplicationBuilder().token(TOKEN).build()
    
     # Command handlers for both private and group chats
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.add_handler(CallbackQueryHandler(update_Menu))

    
    app.add_error_handler(error)
    app.run_polling()