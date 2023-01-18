import itertools

text = ['code', 'aaagmnrs', 'anagrams', 'doce']

lenText = len(text)
index = len(text)

for i in range(lenText):
    if i < index:
      word = text[i]            
      letters = list(word)
      perms = list(itertools.permutations(word, len(word)))
      for j in range(len(perms)):
          perms[j] = ''.join(perms[j])
      while word in perms:
        perms.remove(word)
      for ele in text:
          if ele in perms:
              text.remove(ele)
              index -= 1
            
print(text)
