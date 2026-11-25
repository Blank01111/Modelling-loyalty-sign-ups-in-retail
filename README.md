# Modelling-loyalty-sign-ups-in-retail

## Introduction

Just before her week off my manager had a meeting with the people in charge of our retail company. I asked her what it was about to which she replied that she had to have a talk with me. It was serious yet not serious. I was terrified. Forward a week I am sitting in the office with my manager. There she explained that her meeting was with all the other managers around Gloucestershire. It was a presentation she had to show us. Its contents pushing sales and loyalty sign ups which data suggested we were not doing enough and every employee in this area needed to see it (phew crisis averted). Afterwards filled with determination I went on to push these as much as possible. Something was wrong though. In my mind going back to the meeting as well as my current loyalty sign ups my mind was slowly whirling. I was seeing patterns or lack of them in the amount I got each day. I began to ask questions. What makes a loyalty sign up? What I mean by this question is, are they random? If given enough information, could I predict how many loyalty cards I had signed people up to in 50 shifts? 100 shifts? I set out to answer these questions, with the company’s permission and equipped with the statistical modelling I was learning at the time.

## My initial analysis of the Data

### How the data was collected

Over 50 work shifts spacing over 6 months I recorded the amount of loyalty sign ups I got in that shift, the waiting time until I got one, the date and day of the week, number of people asked and the number of hours I worked. The way the data was collected was as follows:

* I collected data from 05/09/2023 to 25/08/2023.
* The waiting time is measured in the number of people asked.
* People who already had a loyalty card were not counted.
* The length of the shifts were done on the amount of time I was on the shop floor for.
* For waiting times if I asked say 5 people near the end of the shift with no luck then this was added to the waiting time for the next shift until I got one.
* The way I asked each customer was more or less exactly the same through-out.

We define the statistical values for this analysis:
* Let the mean be $\mu_i$ where $i = 1, 2, 3, 4$ for the $4$ bits of analysis I looked at.
* Let the variance be $\sigma^{2}_i$.
* Let the standard deviation be $\sigma_i$.
* Let $M_i$ be the median.
* Let $R_i$ be the interquartile range.

### Plots and statistical values from the data

I work two lengths of shifts. The first length is 4 hours. A histogram for the number of loyalty cards handed out in 37 of these shifts is shown below: $\mu_1 \approx 3.65$, $\sigma^{2}_1 \approx 3.74$, $\sigma_1 \approx 1.93$$, $M_1 = 3.0$, and $R_1 = 3.0$. This bar chart is not symmetric. Values seem to cluster around $2$ and $3$ with a few higher values. This chart is thus right skewed. With a small standard deviation and small interquartile range this dataset is not spread out very much. This dataset is relatively large with $37$ shifts recorded.

