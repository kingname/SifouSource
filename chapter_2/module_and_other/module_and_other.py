import chapter_2.module_and_other.my_script as my_script

print('my_scrpt 的类型是：', type(my_script))


from chapter_2.module_and_other.my_script import People, address, say_something

print('People 的类型是：', type(People))
print('address 的类型是：', type(address))
print('say_something 的类型是：', type(say_something))

import chapter_2
chapter_2.module_and_other.my_script.address
