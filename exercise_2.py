class Edits:
    def editCount(str1, str2, x, y):
        if x == 0:
            return y
    
        if y == 0:
            return x
    
        if str1[x-1] == str2[y-1]:
            return Edits.editCount(str1, str2, x-1, y-1)
    
        return 1 + min(Edits.editCount(str1, str2, x, y-1),
                   Edits.editCount(str1, str2, x-1, y),
                   Edits.editCount(str1, str2, x-1, y-1)
                   )

str1 = "sunday"
str2 = "saturday"

if __name__ == '__main__':
  func1 = Edits()
  print(func1.editCount(str1,str2,len(str1)))
