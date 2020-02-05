message ='Hello World'

print(message[2:5])
print(message[0:7])
print(message[6:])
print(message.lower())

message_first ="""Welcome to Farhana's World
to everybody"""
print(message_first)

new_message =message_first.replace('Farhana','Maysha')
print(new_message)

greeting= 'Hello'
name= 'Farhana'
message_second= greeting + ', ' + name

print(message_second)


message_second= '{}, {}. Welcome!'.format(greeting,name)
print(message_second)

message_second= f'{greeting}, {name}. Welcome to office!'
print(message_second)

message_second= f'{greeting}, {name.upper()}. Welcome to office!'
print(message_second)