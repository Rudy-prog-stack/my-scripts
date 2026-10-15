from faker import Faker# эта библиотека нужна для генерации правдопадобных фальшивых данных
import colorama# эта библиотека нужна для изменения текста по цветам
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
fake = Faker()
print(Fore.GREEN + fake.name())
print(Fore.BLUE + fake.email())
print(Fore.RED + fake.address())