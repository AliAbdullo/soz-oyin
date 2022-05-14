import random as r
from uzwords import words   

def get_word():
  word = r.choice(words)
  while '-' in word  or ' ' in word:
     word = r.choice(words)
  return word.upper()

def display(user_letters, word):
  display_letter = ""
  for letter in word:
    if letter in user_letters.upper():
      display_letter += letter
          
    else:
      display_letter+='-'
  return display_letter


def play():
  word=get_word()
  word_letters=set(word)
  
  user_letters=''
  print(f"Men {len(word)} xonali so'z o'yladim! Topa olasizmi?")
  while len(word_letters)>0:
    print(display(user_letters, word))
    if len(user_letters)>0:
      print(f"Shu vaqtgacha kiritgan xarflaringiz: {user_letters} ")
    
    letter=input("Xarf kiriting: ").upper()
    
    if letter in user_letters.upper():
      print("\nBu xarifni avval kiritgansiz boshqa xarf kiriting!")
      continue
    elif letter in word:
      word_letters.remove(letter)
      print(f" \n{letter} xarfi to'g'ri ")
    else:
      print(f"\nKiritilgan {letter} xarfi yo'q")
    user_letters+=letter
  print(f"\nTabriklayman! Siz \"{word} \"so'zini {len(user_letters )} marta urinish bilan topdingiz! ")  
      
      
  