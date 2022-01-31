class Edits:
    def editCount(self, str1, str2):
        x = len(str1)
        y = len(str2)
        if x == 0:
            return y
    
        if y == 0:
            return x
    
        if str1[x-1] == str2[y-1]:
            return self.editCount(str1, str2, x-1, y-1)
    
        return 1 + min(self.editCount(str1, str2, x, y-1), self.editCount(str1, str2, x-1, y), self.editCount(str1, str2, x-1, y-1))

str1 = "sunday"
str2 = "saturday"

if __name__ == '__main__':
    func1 = Edits()
    print(func1.editCount(str1, str2))
