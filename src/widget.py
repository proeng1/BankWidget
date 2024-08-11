from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    :param info: Строка, содержащая тип и номер карты или счета.
    :return: Строка с замаскированным номером.
    """
    if "Счет" in info:
        account_number = info.split()[-1]
        masked_account = get_mask_account(int(account_number))
        return f"{info.split()[0]} {masked_account}"
    else:
        card_number = info.split()[-1]
        masked_card = get_mask_card_number(int(card_number))
        return f"{' '.join(info.split()[:-1])} {masked_card}"


from datetime import datetime


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формат ДД.ММ.ГГГГ.

    :param date_str: Строка с датой в формате "2024-03-11T02:26:18.671407".
    :return: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
