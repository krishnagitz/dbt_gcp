05:55:21  Running with dbt=1.5.2
05:55:32  Registered adapter: bigquery=1.5.3
05:55:35  Found 2 models, 16 tests, 0 snapshots, 0 analyses, 757 macros, 0 operations, 0 seed files, 1 source, 0 exposures, 0 metrics, 0 groups
| column_name         | data_type | row_count | not_null_proportion | distinct_proportion | distinct_count | is_unique | min | max | avg | median | std_dev_population | std_dev_sample | ... |
| ------------------- | --------- | --------- | ------------------- | ------------------- | -------------- | --------- | --- | --- | --- | ------ | ------------------ | -------------- | --- |
| id                  | string    |     2,240 |                   1 |         1.000000000 |          2,240 |      True |     |     |     |        |                    |                | ... |
| year_birth          | string    |     2,240 |                   1 |         0.026339286 |             59 |     False |     |     |     |        |                    |                | ... |
| education           | string    |     2,240 |                   1 |         0.002232143 |              5 |     False |     |     |     |        |                    |                | ... |
| marital_status      | string    |     2,240 |                   1 |         0.003571429 |              8 |     False |     |     |     |        |                    |                | ... |
| income              | string    |     2,240 |                   1 |         0.881696429 |          1,975 |     False |     |     |     |        |                    |                | ... |
| kidhome             | string    |     2,240 |                   1 |         0.001339286 |              3 |     False |     |     |     |        |                    |                | ... |
| teenhome            | string    |     2,240 |                   1 |         0.001339286 |              3 |     False |     |     |     |        |                    |                | ... |
| dt_customer         | string    |     2,240 |                   1 |         0.295982143 |            663 |     False |     |     |     |        |                    |                | ... |
| recency             | string    |     2,240 |                   1 |         0.044642857 |            100 |     False |     |     |     |        |                    |                | ... |
| mntwines            | string    |     2,240 |                   1 |         0.346428571 |            776 |     False |     |     |     |        |                    |                | ... |
| mntfruits           | string    |     2,240 |                   1 |         0.070535714 |            158 |     False |     |     |     |        |                    |                | ... |
| mntmeatproducts     | string    |     2,240 |                   1 |         0.249107143 |            558 |     False |     |     |     |        |                    |                | ... |
| mntfishproducts     | string    |     2,240 |                   1 |         0.081250000 |            182 |     False |     |     |     |        |                    |                | ... |
| mntsweetproducts    | string    |     2,240 |                   1 |         0.079017857 |            177 |     False |     |     |     |        |                    |                | ... |
| mntgoldprods        | string    |     2,240 |                   1 |         0.095089286 |            213 |     False |     |     |     |        |                    |                | ... |
| numdealspurchases   | string    |     2,240 |                   1 |         0.006696429 |             15 |     False |     |     |     |        |                    |                | ... |
| numwebpurchases     | string    |     2,240 |                   1 |         0.006696429 |             15 |     False |     |     |     |        |                    |                | ... |
| numcatalogpurchases | string    |     2,240 |                   1 |         0.006250000 |             14 |     False |     |     |     |        |                    |                | ... |
| numstorepurchases   | string    |     2,240 |                   1 |         0.006250000 |             14 |     False |     |     |     |        |                    |                | ... |
| numwebvisitsmonth   | string    |     2,240 |                   1 |         0.007142857 |             16 |     False |     |     |     |        |                    |                | ... |
| acceptedcmp3        | string    |     2,240 |                   1 |         0.000892857 |              2 |     False |     |     |     |        |                    |                | ... |
| acceptedcmp4        | string    |     2,240 |                   1 |         0.000892857 |              2 |     False |     |     |     |        |                    |                | ... |
| acceptedcmp5        | string    |     2,240 |                   1 |         0.000892857 |              2 |     False |     |     |     |        |                    |                | ... |
| acceptedcmp1        | string    |     2,240 |                   1 |         0.000892857 |              2 |     False |     |     |     |        |                    |                | ... |
| acceptedcmp2        | string    |     2,240 |                   1 |         0.000892857 |              2 |     False |     |     |     |        |                    |                | ... |
| response            | string    |     2,240 |                   1 |         0.000892857 |              2 |     False |     |     |     |        |                    |                | ... |
| complain            | string    |     2,240 |                   1 |         0.000892857 |              2 |     False |     |     |     |        |                    |                | ... |
| country             | string    |     2,240 |                   1 |         0.003571429 |              8 |     False |     |     |     |        |                    |                | ... |
