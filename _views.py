view_dictionary = {
    'logsCount': """
        CREATE OR REPLACE VIEW logsCount AS
        SELECT path, count(path) AS views
        FROM log
        GROUP BY path;
    """,

    'viewsPerAuthor': """
        CREATE OR REPLACE VIEW viewsPerAuthor AS
        SELECT author, SUM(views) AS totalViewsForAuthor
        FROM articles
        JOIN logsCount
        ON path
        LIKE CONCAT('%', slug) GROUP BY author;
    """,

    'visitsPerDay': """
        CREATE OR REPLACE VIEW visitsPerDay AS
        SELECT date(time) AS visitDate, count(date(time)) AS visitCount
        FROM log
        GROUP BY visitDate;
    """,

    'notFoundPerDay': """
        CREATE OR REPLACE VIEW notFoundPerDay AS
        SELECT date(time) AS errorDate, status, COUNT(date(time)) AS errorCount
        FROM log
        WHERE status = '404 NOT FOUND'
        GROUP BY errorDate, status;
    """,

    'errored': """
        CREATE OR REPLACE VIEW errored AS
        SELECT errorDate, status, (100*cast(errorCount AS float) / visitCount)
        AS perc
        FROM visitsPerDay
        JOIN notFoundPerDay
        ON visitDate = errorDate;
    """
}
