from models import Store, ShoppingCart, Item

def main():
    store = Store("DIC Store")
    store.add_item(Item("2.5インチSSD", 13370, 10))
    store.add_item(Item("3.5インチHDD", 10980, 10))
    store.add_item(Item("CPU", 40830, 10))
    store.add_item(Item("CPUクーラー", 13400, 10))
    store.add_item(Item("M.2 SSD", 12980, 10))
    store.add_item(Item("PCケース", 8727, 10))
    store.add_item(Item("グラフィックボード", 23800, 10))
    store.add_item(Item("マザーボード", 28980, 10))
    store.add_item(Item("メモリー", 13880, 10))
    store.add_item(Item("電源ユニット", 8980, 10))

    print("🤖 あなたの名前を教えてください")
    user_name = input()
    print("🏧 ウォレットにチャージする金額を入力にしてください")
    wallet_amount = int(input())
    cart = ShoppingCart(user_name, wallet_amount)

    while True:
        print("🛍️ ショッピングを開始します")
        print("📜 商品リスト")
        store.display_items()
        print("⛏ 商品番号を入力してください")
        item_number = int(input())
        print("⛏ 商品数量を入力してください")
        item_quantity = int(input())
        cart.add_item(store.get_item(item_number), item_quantity)
        print("🛒 カートの中身")
        cart.display_cart()
        print("🤑 合計金額:", cart.total_cost())
        print("😭 買い物を終了しますか？(yes/no)")
        if input() == "yes":
            break

    print("💸 購入を確定しますか？(yes/no)")
    if input() == "yes":
        cart.check_out(store)
    print("🎉 終了")

if __name__ == "__main__":
    main()
