import pywhatkit
import os

def send_message_inst():
    mobile = os.environ.get('MOBILE')
    if not mobile:
        raise ValueError("Переменная окружения MOBILE не установлена")
    message = input('Введите текст сообщения: ')
    
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)
    
def send_message():
    mobile = os.environ.get('MOBILE')
    if not mobile:
        raise ValueError("Переменная окружения MOBILE не установлена")
    message = input('Введите текст сообщения: ')
    hour = input('Введите час отправки: ')
    minute = input('Введите минуту отправки: ')
    
    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=int(hour), time_min=int(minute))
    
def main():
    # send_message_inst()
    send_message()
    
if __name__ == '__main__':
    main()