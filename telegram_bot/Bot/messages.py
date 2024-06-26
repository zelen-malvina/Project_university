from aiogram import html


def start_message(*, msg: str) -> str:
    """
    Сообщение стартовой команды (/start)
    """

    START_MESSAGE = (f"👋 Привет, {html.bold(msg.from_user.full_name)}!\n\n"
                     f"Укажи логин, который был выдан тебе для сайта VyatFlow.")

    return START_MESSAGE


#Сообщения авторизации с помощью логина.

LOGINING_SUCCESSFULY = (f"✅ {html.bold('Вы успешно авторизовались!')}\n\n"
                        "Ожидайте информацию о лабораторных работах.")

LOGINING_FAILED = (f"❌ {html.bold('Такого логина не существует!')}\n\n"
                    "Пожалуйста, проверьте корректность данных и отправьте снова.")

def work_accepted(*, msg: str) -> str:
    """
    Сообщение о том, что работа принята
    """
    WORK_ACCEPTED = (f"{html.bold(f'Ура! Лабораторная работа «{msg}» успешно принята.')}\n\n"
                    f"Продолжай в том же духе. 😊")
    
    return WORK_ACCEPTED

def work_rejected(*, msg: str) -> str:
    """
    Сообщение о том, что работа отправлена на доработку
    """
    WORK_REJECTED = (f"{html.bold(f'Эх... Лабораторную работу «{msg}» отправили на доработку.')}\n\n"
                    f"Ты всё сможешь! 😉")
    
    return WORK_REJECTED