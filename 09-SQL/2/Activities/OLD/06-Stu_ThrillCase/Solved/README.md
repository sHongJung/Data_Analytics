# The Thrill of the CASE

## Instructions

* In this activity, you will practice using the `CASE` statement in MySQL, which lets you construct conditions for executing MySQL code.

* If you aren't already in `top_songsDB`, switch to it.

* In the `top5000` table, create a `CASE` statement so that in the second row:

  * If the `artist` name is "Bill van Halen," change it to "Bill van Halen and the Licks" 
  * If it's "Bill Haliday," change it to "Bill Haliday and the Jazz"
  * Otherwise, change it to "Bill Haley and the Comets"

  ```sql
  UPDATE top5000
  SET artist =
  CASE
   WHEN artist = 'Bill van Halen'
  		 THEN 'Bill van Halen and the Licks'
   WHEN artist = 'Bill Haliday'
    THEN 'Bill Haliday and the Jazz'
  		ELSE 'Bill Haley and the Comets'
  END
  WHERE position = 2;
  ```

## Bonus

* Create a `CASE` statement so that:

  * If the `artist` name is "Bing Crosby," change it to "Bill Throggs Neck" 
  * If it's "Celine Dion," change it to "Sarah Hellion"
  * Otherwise, change it to "Skrillex"
  * But make these modifications **only** in rows 1 through 5!

    ```sql
    UPDATE top5000
     SET `artist` =
     CASE
      WHEN artist = 'Bing Crosby'
    		 THEN 'Bill Throggs Neck'
      WHEN artist = 'Celine Dion'
       THEN 'Sarah Hellion'
    		 ELSE 'Skrillex'
      END
     WHERE position BETWEEN 1 and 5; 
    ```
