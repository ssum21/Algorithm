-- 코드를 작성해주세요
SELECT SUM(HG.SCORE) AS SCORE, HE.EMP_NO AS EMP_NO, HE.EMP_NAME AS EMP_NAME, HE.POSITION AS POSITION, HE.EMAIL AS EMAIL
FROM HR_EMPLOYEES AS HE
JOIN HR_DEPARTMENT AS HD ON HE.DEPT_ID = HD.DEPT_ID
LEFT JOIN HR_GRADE AS HG ON HE.EMP_NO = HG.EMP_NO
GROUP BY EMP_NAME, EMP_NO, POSITION, EMAIL
ORDER BY SCORE DESC
LIMIT 1