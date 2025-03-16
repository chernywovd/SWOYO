async def checking_the_number(sender: str, recipient: str, message: str):
    check = False
    try:
        int(sender)
        int(recipient)

        if (sender[:1] == '8' and len(sender) == 11 or sender[:2] == '+7' and len(sender) == 12) and (recipient[:1] == '8' and len(recipient) == 11 or recipient[:2] == '+7' and len(recipient) == 12):
            if sender == recipient:
                print('\nНомер отправителя не должен быть таким же, как номер получателя\n'
                      'Пожалуйста, введите разные номера\n')
                return check
            else:
                if len(message) < 1000:
                    check = True
                    return check
                else:
                    print('\nСлишком длинное смс. Пожалуйста, напишите сообщение короче\n')
                    return check
        else:
            print('\nРоссийские номера должны начинаются на «8» либо «+7» и состоять из 11 цифр. '
                  'Пожалуйста, введите номера корректно\n')
            return check

    except Exception as ex:
        print('\nНомера должны состоять из цифр. '
              'Пожалуйста, введите номера корректно\n')
        print(ex)
        return check