DROP TABLE IF EXISTS cultivated-link-373708.sample_dataset.sample;

CREATE TABLE cultivated-link-373708.sample_dataset.sample
(
  id int64,
  label string,
  value string
)
;

insert into cultivated-link-373708.sample_dataset.sample
values
(1, 'name', 'oscar'),
(2, 'name', 'monika')
;