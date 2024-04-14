from src.api import api
import src.config as conf

import time


def work_orders(bot: api.API):

    user_orders = bot.get_user_orders()
    
    for user_order in user_orders:
        # if not user_order['isActive']:
        #     continue

        all_orders = bot.get_stat_order(user_order)

        type_currency = list(user_order["currencies"].keys())[0]
        print(f"В обработке предмет: {user_order['item']['name']} c ценой: {user_order["currencies"][type_currency]} {type_currency}")
        if len(all_orders) < 2:
            continue

        max_price = 0
        for order in all_orders:
            if order['steamid'] == conf.MY_STEAM_ID:
                continue
            if order['currencies'][type_currency] > max_price:
                max_price = order['currencies'][type_currency]

        if type_currency == 'keys':
            user_order["currencies"][type_currency] = max_price + conf.STEP_KEY
        else:
            user_order["currencies"][type_currency] = max_price + conf.STEP_REF

        print(f"Его максимальная цена {max_price}. Наша новая цена: {user_order["currencies"][type_currency]}")
        bot.update_order(order=user_order)

    print("Прошлись по всем предметам! Замираем на минуту")
    time.sleep(300)