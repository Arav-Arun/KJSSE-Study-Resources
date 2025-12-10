def convert_to_words(input):  
    if input == 0:  
        return "zero"  
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    words = ""    
    if input>= 100:  
        words += ones[input // 100] +" hundred "  
        input %= 100  
    if input>= 10 and input<= 19:  
        words += teens[input - 10] + " "  
        input = 0  
    elif input>= 20:  
        words += tens[input // 10] + " "  
        input %= 10  
    if input>= 1 and input<= 9:  
        words += ones[input] + " "  
    return words.strip()  


input = int(input("Enter a number; "))  

words = convert_to_words(input)  
print(words) 