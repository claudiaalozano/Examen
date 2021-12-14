def minion(s):
    vowels = "AEIOU"
    scoreStuart = 0
    scoreKevin = 0
    s=s.upper()

    for i in range(len(s)):
        if s[i] not in vowels:
            scoreStuart = scoreStuart + (len(s)-i)
        else: 
            scoreKevin = scoreKevin + (len(s)-i)
            