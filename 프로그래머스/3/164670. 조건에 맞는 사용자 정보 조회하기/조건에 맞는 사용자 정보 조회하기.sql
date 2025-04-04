-- 코드를 입력하세요
SELECT UU.USER_ID, UU.NICKNAME,
(CONCAT(UU.CITY,' ' ,UU.STREET_ADDRESS1,' ', UU.STREET_ADDRESS2)) AS 전체주소, 
CONCAT(LEFT(UU.TLNO, 3), '-', MID(UU.TLNO, 4, 4), '-', RIGHT(UU.TLNO,4)) AS '전화번호'
FROM USED_GOODS_BOARD AS UB
JOIN USED_GOODS_USER AS UU ON UB.WRITER_ID = UU.USER_ID
GROUP BY UB.WRITER_ID
HAVING COUNT(*)>2
ORDER BY UU.USER_ID DESC