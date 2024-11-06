import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            time.sleep(0.001)
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()



if __name__ == "__main__":
    bank = Bank()
    
    deposit_thread = threading.Thread(target=bank.deposit)
    take_thread = threading.Thread(target=bank.take)
    deposit_thread.start()
    take_thread.start()
    deposit_thread.join()
    take_thread.join()
    print(f"Итоговый баланс: {bank.balance}")

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


