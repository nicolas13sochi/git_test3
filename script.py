import random

abcd = '1234567890qwertyuiopasdfghjklzxcvbnm_'

print("".join([random.choice(abcd) for i in range(random.randint(8,16))]))

