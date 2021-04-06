import numpy as np

def total(basket):
    book_cost = 800
    unique_books = list(set(basket))
    unique_books_count = [basket.count(book) for book in unique_books]
    print(unique_books, unique_books_count)
    basket_total = 0
    while sum(unique_books_count) > 0:
        if len(unique_books_count) == 5:
            print("Whole Series, 25% discount")
            basket_total += 5*(book_cost*0.75)
        elif len(unique_books_count) == 4:
            print("Four of Series, 20% discount")
            basket_total += 4*(book_cost*0.80)
        elif len(unique_books_count) == 3:
            print("Three of Series, 10% discount")
            basket_total += 3*(book_cost*0.90)
        elif len(unique_books_count) == 2:
            print("Two of Series, 5% discount")
            basket_total += 2*(book_cost*0.95)  
        elif len(unique_books_count) == 1:
            basket_total += 1*(book_cost) 
        unique_books_count = [x-1 for x in unique_books_count]
        unique_books_count = [x for x in unique_books_count if x!=0]
        print(unique_books_count)
    return int(basket_total)

print(total([1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]))
#print(5*(800*0.75) + 3*(800*0.9))
