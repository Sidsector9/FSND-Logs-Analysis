# Directory Structure
- `_views.py` - Contains all the necessary views stored as a dictionary.
- `_queries.py` - Contains all the SQL queries stored as a dictionary.
- `log-analysis.py` - The main file which you will run.
- `output.txt` - File contains the output of `log-analysis.py`.

# Project
The database `news` consists of 3 relations:
- Articles
- Authors
- Log

### Schema for Articles
| author | title | slug | lead | body | time | id |
|--------|-------|------|------|------|------|----|

### Schema for Authors
| name | bio | id |
|------|-----|----|

### Schema for Log:
| path | ip | method | status | time | id |
|------|----|--------|--------|------|----|

# Challenge
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

# Requirements
- PostgreSQL 9.5.14
- Python 3.5.2

# Installation
- Clone the repository using `git clone git@github.com:Sidsector9/FSND-Logs-Analysis.git`
- cd into `FSND-Logs-Analysis/`
- Import and connect to database `psql -d news -f newsdata.sql` (Assuming database `news` already exists)

# Views
There are 5 views used to simplify the query, they are:
```sql
CREATE OR REPLACE VIEW logsCount AS
SELECT path, COUNT(path) AS views
FROM log
GROUP BY path;
```
```sql
CREATE OR REPLACE VIEW viewsPerAuthor AS
SELECT author, sum(views) AS totalViewsForAuthor
FROM articles
JOIN logsCount
ON path
LIKE CONCAT('%', slug) GROUP BY author;
```
```sql
CREATE OR REPLACE VIEW visitsPerDay AS
SELECT date(time) AS visitDate, COUNT(date(time)) AS visitCount
FROM log
GROUP BY visitDate;
```
```sql
CREATE OR REPLACE VIEW notFoundPerDay AS
SELECT date(time) AS errorDate, status, COUNT(date(time)) AS errorCount
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY errorDate, status;
```
```sql
CREATE OR REPLACE VIEW errored AS
SELECT errorDate, status, (100*cast(errorCount AS float) / visitCount)
AS perc
FROM visitsPerDay
JOIN notFoundPerDay
ON visitDate = errorDate;
```

# Usage
- Run `python3 log-analysis.py`