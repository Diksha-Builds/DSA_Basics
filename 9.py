# Count

str = input("Enter a string : ")

vow = 0
con = 0
dig = 0
spe = 0

for i in range(len(str)):
    if(str[i] >= '!' and str[i] <= '/' or str[i] >= ':' and str[i] <= '@' or str[i] >= '[' and str[i] <= '`' or str[i] >= '{' and str[i] <= '~'):
        spe+=1
    elif(str[i] >= '0' and str[i] <= '9'):
        dig+=1
    elif(str[i] == 'a' or str[i] == 'A' or str[i] == 'e' or str[i] == 'E' or str[i] == 'i' or str[i] == 'I' or str[i] == 'o' or str[i] == 'O' or str[i] == 'u' or str[i] == 'U'):
        vow+=1
    elif(str[i] >= 'b' and str[i] <= 'd' or str[i] >= 'f' and str[i] <= 'h' or str[i] >= 'j' and str[i] <= 'n' or str[i] >= 'p' and str[i] <= 't' or str[i] >= 'v' and str[i] <= 'z' or str[i] >= 'B' and str[i] <= 'D' or str[i] >= 'F' and str[i] <= 'H' or str[i] >= 'J' and str[i] <= 'N' or str[i] >= 'P' and str[i] <= 'T' or str[i] >= 'V' and str[i] <= 'Z'):
        con+=1

print("Total number of vowels : ",vow)
print("Total number of consonants : ",con)
print("Total number of digits : ",dig)
print("Total number of special characters : ",spe)


