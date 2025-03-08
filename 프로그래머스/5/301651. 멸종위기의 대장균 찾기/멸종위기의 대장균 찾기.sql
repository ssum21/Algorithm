-- 코드를 작성해주세요
WITH RECURSIVE GEN AS (
    SELECT
    ID,
    PARENT_ID,
    1 AS Generation
    FROM
    ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT
    E.ID,
    E.PARENT_ID,
    G.Generation+1
    FROM ECOLI_DATA E
    JOIN GEN AS G ON G.ID = E.PARENT_ID
), Childless AS (
    SELECT *
    FROM GEN
    WHERE ID NOT IN (
        SELECT DISTINCT PARENT_ID
        FROM ECOLI_DATA
        WHERE PARENT_ID IS NOT NULL
    )
)

SELECT COUNT(Generation) AS COUNT, Generation AS GENERATION
FROM Childless
GROUP BY Generation
ORDER BY Generation