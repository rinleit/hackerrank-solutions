/* Oracle */
WITH thousand AS
 (SELECT *
    FROM (SELECT LEVEL lvl
            FROM DUAL
          CONNECT BY LEVEL <= 1000)
   WHERE lvl > 1)
SELECT LISTAGG(t1.lvl, '&') WITHIN GROUP(ORDER BY t1.lvl)
  FROM thousand t1
 WHERE t1.lvl = (SELECT COUNT(DISTINCT t2.lvl) + 2 /* count number between 1 and prime number */
                   FROM thousand t2
                  WHERE t2.lvl < t1.lvl AND MOD(t1.lvl, t2.lvl) > 0);