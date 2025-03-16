import argparse
from CheckingTheNumber import checking_the_number

async def parse_args():
    'Функция для корректного ввода номера и смс'
    parse_args_ = False
    parser = argparse.ArgumentParser(description="Отправить SMS через API.")

    parser.add_argument("--sender", required=True, type=str, help="Номер отправителя") # type=str для проверки на +7, так как в переводе из int(+7) в str плюсик теряется
    parser.add_argument("--recipient", required=True, type=str, help="Номер получателя")
    parser.add_argument("--message", required=True, type=str, help="Текст сообщения")

    args = parser.parse_args()

    if await checking_the_number(sender=args.sender, recipient=args.recipient, message=args.message):
        parse_args_ = {
            "sender": args.sender,
            "recipient": args.recipient,
            "message": args.message
        }
        return parse_args_
    else:
        return parse_args_