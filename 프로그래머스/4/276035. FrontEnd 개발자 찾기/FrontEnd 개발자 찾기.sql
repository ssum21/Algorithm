-- 코드를 작성해주세요
WITH FRONT_SKILL AS (
    SELECT SUM(CODE) AS SUM_CODE
    FROM SKILLCODES
    GROUP BY CATEGORY
    HAVING CATEGORY = 'Front End'
)

SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
WHERE D.SKILL_CODE & (SELECT SUM_CODE FROM FRONT_SKILL)
ORDER BY D.ID ASC
