price_book=[('Horror',1.63),('Love',2.6),('Fiction',1.25)]

def book_more_cost(list_books):
    more_cost=0
    book_cost=''
    
    for book,cost in list_books:
        if cost>more_cost:
            more_cost=cost
            book_cost=book
        else:
            pass
        
        return (more_cost,book_cost)
    
    
cost,book=book_more_cost(price_book) 

print(f'The book about {book} have the higthear price, it is {cost}')   
    
