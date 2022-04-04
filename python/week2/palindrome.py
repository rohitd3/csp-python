class Palindrome:
    def __init__(self, text):
        self.text = text

    def __call__(self):
        text_strip = list([val for val in self.text if val.isalpha() or val.isnumeric()])
      # checking to see if numbers or alphabets
        self.text = "".join(text_strip)
        self.text = self.text.lower()
      # making the alphabets into lower case

        if self.text == self.text[::-1]:
          # checking by reversing the text or numeric pattern
            return True
        else:
            return False

test_cases = ["A man, a plan, a canal Panama!", "qwerrewq", "lmao", "racecar", "rohitttttrohit", "lol"]

def tester():
  for n in test_cases:
      palindrome = Palindrome(text=n)
      print(n, palindrome())