-- 코드를 입력하세요
SELECT HOUR(DATETIME), COUNT(HOUR(DATETIME))
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME) ASC