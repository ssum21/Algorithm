-- 코드를 입력하세요
WITH TOT_HALF AS (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_HALF
    FROM FIRST_HALF
    GROUP BY FLAVOR
), TOT_JULY AS (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_JULY
    FROM JULY
    GROUP BY FLAVOR
)
SELECT F.FLAVOR
FROM TOT_HALF AS F
LEFT JOIN TOT_JULY AS J ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY (F.TOTAL_HALF + IFNULL(J.TOTAL_JULY, 0)) DESC
LIMIT 3