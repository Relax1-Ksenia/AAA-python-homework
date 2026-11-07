def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print(moscow & kazan)  # - что можно забрать в любом из двух городов

    print(moscow - kazan)  # - что есть только в Москве

    print(kazan - moscow)  # - что есть только в Казани

    print(len(kazan | moscow))  # - сколько разных товаров на обоих складах вместе


if __name__ == "__main__":
    main()