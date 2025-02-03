# Shiller's-CAPE-Ratio


This repository is the implementation of the paper on predicting US equities using CAPE with a modification (results obtained were similar to the paper)/

# Shiller's regression
R <sub> t + 120 </sub> = a1 + a2*CAPE <sub> t </sub> + epsilon
<br>
![e4003932-7dbc-484a-8f43-b81faa98c857](https://github.com/user-attachments/assets/ec198d77-7caf-436c-bce2-dd8eed76a4db)
<br>
R_2 Score = 53% (indicating CAPE is able to explain the returns to some extent)

# ML models using CAPE
![c542623a-e40c-4d36-aeb6-fabac1e64ead](https://github.com/user-attachments/assets/bf937f3e-baef-4b4e-a9d4-9e098dc96b81)

| Model Name            | RMSE Score |
|----------------------|------------|
| Linear Regression (shiller's) | 4.94 %      |
| Random Forest | 5.17 %    |
| GBM  | 5.18 %     |
| SVR | 5.41 %     |

# ML models using "CAPE_INV", "Bond_Returns_10Y", "Inflation", "S&P Vol", "Bond Vol" 

![db98bde8-73c5-48c2-bfcf-857006fa17bd](https://github.com/user-attachments/assets/713527af-b0b2-4302-b770-23d6615dec81)
<br>
For calculating returns following equation was used :
 r_{t+1} = \%\Delta PE<sub>t+1</sub> + \%\Delta E<sub>t+1</sub> + DP<sub>t+1</sub>

| Model Name            | RMSE Score |
|----------------------|------------|
| Linear Regression (shiller's) | 3.88 %      |
| Random Forest | 3.98 %    |
| GBM  | 3.80 %     |
| SVR | 3.85 %     |
