from src.api import api
from src.service.order import work_orders
from src.database.db import create_session, create_tables

def main():
    bot = api.API()
    create_tables()
    # session = create_session()

    # while True:
    #     work_orders(bot=bot)

    

if __name__ == "__main__":
    main()