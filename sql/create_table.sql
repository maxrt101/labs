/* Create the table `shoes` */

use lab6;

create table if not exists shoes (
  id            serial primary key,
  size          int  not null default 0,
  shoes_type    enum ('SPORT', 'SUMMER', 'WINTER')  not null,
  manufacturer  text not null,
  model         text not null
);

