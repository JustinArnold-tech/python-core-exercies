class Anagrams:
    def is_anagram(self,w1, w2):
        if(sorted(w1) == sorted(w2)):
            return f"{w1} and {w2} are anagrams"
        else:
            return f"'{w1}' and '{w2}' are not anagrams"

w1 = 'arc'
w2 = 'car'

if __name__ == '__main__':
    func1 = Anagrams()
    print(func1.is_anagram(w1,w2))