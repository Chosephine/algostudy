-- 프로그래머스 59409 중성화 여부 파악하기

SELECT  ANIMAL_ID, 
        NAME, 
        IF(
            SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%' , 'O', 'X' 
        ) AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;