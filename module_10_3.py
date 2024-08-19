from threading import Thread, Lock
import random
import time
from time import sleep

class Bank(Thread):

    def __init__(self, balance):
        super().__init__()
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            dep = random.randrange(50, 500)
            self.balance += dep
            if self.balance>=500 and lock.locked():
                lock.release()
                print(f'Пополнение: {dep}. Баланс: {self.balance}')
        time.sleep(0.1)


    def take(self):
        for i in range(100):
            k = random.randrange(50, 500)
            print(f'Запрос на {k}')
            if k <= self.balance:
                self.balance = self.balance - k
                print(f'Снятие: {k}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquiere()





th1 = Thread(target=Bank.deposit, args=(balance, 100))
th2 = Thread(target=Bank.take, args=(balance, 100))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс:{self.balance}')