def disemvowel(string_):
    a = [x for x in string_ if x.lower() not in 'euioa']
    # return s.translate(None, "aeiouAEIOU")
    return a

disemvowel('This website is for losers LOL!')
