query_dictionary = {
    'popular_articles': """
        SELECT title, views
        FROM articles
        JOIN logsCount
        ON path
        LIKE concat('%', slug)
        ORDER BY views
        DESC
        LIMIT 3;
    """,

    'popular_authors': """
        SELECT name, totalviewsforauthor
        FROM authors
        JOIN viewsPerAuthor
        ON id = author
        ORDER BY totalviewsforauthor
        DESC;
    """,

    'error_rate': """
        SELECT errordate, perc
        FROM errored
        WHERE perc > 1;
    """
}
