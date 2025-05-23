-- 1. 5회 이상 대여된 자동차 ID 찾기
WITH FILTERED_CARS AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY CAR_ID
    HAVING COUNT(*) > 4
)
-- 2. 월별 대여 횟수 집계
SELECT 
    MONTH(START_DATE) AS MONTH, 
    CAR.CAR_ID, 
    COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CRH
JOIN FILTERED_CARS CAR ON CRH.CAR_ID = CAR.CAR_ID
WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH(START_DATE), CAR.CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;
