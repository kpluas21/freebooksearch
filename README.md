# freebooksearch
A small Python script to find links to full, free eBooks using Google Books API.

## How to Use
Simply execute the main python file, providing the name of the book as the first and main argument.

```
python3 main.py <BookTitle>
```
The program will attempt to retrieve a list of links for you. Up to a maximum of 10.

Example 
```
➜  src ./main.py prideandprejudice
Searching for free eBook links for: prideandprejudice
('0: Pride and Prejudice '
 'https://play.google.com/store/books/details?id=kQ0mAAAAMAAJ')
('1: Pride and Prejudice '
 'https://play.google.com/store/books/details?id=s1gVAAAAYAAJ')
('2: Pride and Prejudice '
 'https://play.google.com/store/books/details?id=7KkzAQAAMAAJ')
('3: Pride and Prejudice '
 'https://play.google.com/store/books/details?id=FaozAQAAMAAJ')
.
.
.

```

From here, you can select which link you want and it will automatically open up your default browser to that URL.
