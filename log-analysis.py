import psycopg2
from _views import view_dictionary
from _queries import query_dictionary


def main():

    # Connect to the database 'news'.
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()

    # Create views.
    for key in view_dictionary:
        cursor.execute(view_dictionary[key])

    # Display the top 3 articles of all time.
    print("""
    -----------------------------------------------
    # Most popular three articles of all time
    -----------------------------------------------""")
    cursor.execute(query_dictionary['popular_articles'])
    for (title, view) in cursor.fetchall():
        print('    {} -- {}' . format(title, view))

    # Display most viewed authors.
    print("""
    -----------------------------------------------
    # Most popular authors of all time
    -----------------------------------------------""")
    cursor.execute(query_dictionary['popular_authors'])
    for (name, view) in cursor.fetchall():
        print('    {} -- {}' . format(name, view))

    # Display dates which have more that 1% of 404 visits per day.
    print("""
    -----------------------------------------------
    # Days with 404 more than 1%
    -----------------------------------------------""")
    cursor.execute(query_dictionary['error_rate'])
    for (date, percentage) in cursor.fetchall():
        print('    {} -- {}% errors' . format(date.strftime('%B %d, %Y'),
                                              round(percentage, 2)))

    # Close cursor.
    cursor.close()

    # Close connection.
    conn.close()


if __name__ == '__main__':
    main()
