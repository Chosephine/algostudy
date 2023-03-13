-- programmers 12세 이하인 여자 환자 목록 출력하기

-- 1) IFNULL 활용

SELECT
    PT_NAME,
    PT_NO,
    GEND_CD,
    AGE,
    IFNULL(TLNO, 'NONE') as TLNO
FROM PATIENT 
WHERE AGE <= 12 AND GEND_CD = 'W'
    -- GEND_CD == 'W' 아님 주의!
ORDER BY 
    AGE DESC, PT_NAME ASC;

-- 2) CASE문 활용

SELECT
    PT_NAME,
    PT_NO,
    GEND_CD,
    AGE,
    CASE
        WHEN TLNO IS NULL THEN 'NONE' 
        -- TLNO=NULL 로 쓰는게 아님..!!
        ELSE TLNO 
        END as TLNO
FROM PATIENT 
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY 
    AGE DESC, PT_NAME ASC;