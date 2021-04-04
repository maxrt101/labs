/* Adds dummy rows to `shoes` table */

begin;

use lab6;

insert into shoes(size, shoes_type, manufacturer, model)
  values(39, 'SPORT', 'abibas', 'Super sport'),
        (45, 'SPORT', 'nike', 'Air'),
        (41, 'WINTER', 'nike', 'Boots'),
        (51, 'WINTER', 'adidas', 'Boots'),
        (43, 'SUMMER', 'nike', 'Flip Flops'),
        (44, 'SPORT', 'adidas', 'Sport'),
        (45, 'SPORT', 'nike', 'Sport');

