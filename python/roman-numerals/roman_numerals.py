def roman(n):
    roman_conversion = [[1000, 'M'],
                        [900, 'CM'],
                        [500, 'D'],
                        [400, 'CD'],
                        [100, 'C'],
                        [90, 'XC'],
                        [50, 'L'],
                        [40, 'XL'],
                        [10, 'X'],
                        [9, 'IX'],
                        [5, 'V'],
                        [4,'IV'],
                        [1, 'I'],]
    
    digits = [1000,100,10,1]
    
    def split_number(n):
        numbers = []
        for digit in digits:
            count, n = divmod(n, digit)
            numbers.append(count*digit)
        return numbers
    
    numerals = []
    print(split_number(n))
    for n in split_number(n):
        for decimal, roman in roman_conversion:
            while n > 0 and n >= decimal:
                print(n,decimal)
                count, n = divmod(n, decimal)
                print(count,n)
                numerals.append(count*roman)
        
    return ''.join(numerals)
        
print(roman(1990))