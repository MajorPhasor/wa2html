import wamsg
import re
import sys
import codecs

def import_message_file(filename):
    with codecs.open(filename, "r", encoding='utf-8') as f:
        text_lines = []
        for item in f:
            number = 0
            text_lines.append(item)
    return(text_lines)

def extract_messages_from_text(text_lines):
    date_format = "^[0-9]+/[0-9]+/[0-9]+"
    time_format = "[0-9]+\:[0-9]+ ?[AP]?M? -"
    sender_format = "-.+?\:"

    message_suffix = ""
    messages = []

    for item in reversed(text_lines):
        if len(item) > 0:
            try:
                date_group = re.search(date_format, item).group()
                time_re = re.search(time_format, item)
                time_group = time_re.group().strip(' - ')
                sender = re.search(sender_format, item).group().strip(':').strip('- ')
                text = re.search(f"{sender}\:.*", item).group().strip(f"{sender}: ") + message_suffix
                messages.append(wamsg.WAMSG(date_group, time_group, sender, text))
                message_suffix = ""
            except:
                message_suffix += (" " + item).strip('\n')
    return(reversed(messages))

def display_messages(messages):
    for msg in messages:
        print(f'Date: {msg.date} Time: {msg.time} Sender: {msg.sender} Message: {msg.text}')   
    
def generate_html(sender, messages):
    html_header = '<!DOCTYPE html>\n<html>\n<head>\n<link rel="stylesheet" href="imessage.css">\n</head>\n<body>\n'
    h1 = f'<h1>WhatsApp Chat with {sender}</h1>\n'
    chat_div_class = '<div class="chat">\n'
    me_div_class = '  <div class="mine messages">\n'
    remote_div_class = '  <div class="yours messages">\n'
    message_div_class = '    <div class="message last">\n'
    end_message_div = '     </div>\n'
    end_sender_div = '   </div>\n'
    end_chat_div = ' </div>\n'
    
    output_file_text = html_header
    output_file_text += h1
    output_file_text += chat_div_class
    
    for message in messages:
        if sender in message.sender:
            output_file_text += remote_div_class
        else:
            output_file_text += me_div_class
        output_file_text += message_div_class
        output_file_text += "      " + message.text + '\n'
        output_file_text += end_message_div
        output_file_text += message.date + " " + message.time + "\n"
        output_file_text += end_sender_div
        
    output_file_text += end_chat_div
    return output_file_text
    
def export_file(html_text):
    output_file=codecs.open("testoutput.html",'w',"utf-8")
    output_file.write(html_text)
    output_file.close()
    
def main():
    filename = sys.argv[1]
    print(filename)
    sender = filename.strip(".\\WhatsApp Chat with").strip(".txt")
    print(sender)
    messages_list = import_message_file(filename)
    messages = extract_messages_from_text(messages_list)
    # display_messages(message)
    html_text = generate_html(sender, messages)
    export_file(html_text)
    
if __name__ == "__main__":
    main()