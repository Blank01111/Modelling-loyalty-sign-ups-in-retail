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

<img width="757" height="570" alt="Screenshot From 2026-11-25 14-14-38" src="https://github.com/user-attachments/assets/d1c090a1-6b02-48e0-a56f-aa4098bd11dd" />

<img width="757" height="570" alt="Screenshot From 2026-11-25 14-15-26" src="https://github.com/user-attachments/assets/94c7f274-3f21-4fce-9777-51270b53a653" />

<img width="757" height="570" alt="Screenshot From 2026-11-25 14-16-17" src="https://github.com/user-attachments/assets/1d49dafe-ee3a-414a-84f9-e1b2c7fe10bc" />

I also work 5.5 hour shifts. A bar plot for the number of loyalty cards handed out in 13 of these shifts is shown below: $\mu_2 \approx 3.23$, $\sigma^{2}_2 \approx 2.18$, $\sigma_2 ≈ 1.48$,  $M_2 = 3.0$, and $R_2 = 2.0$. This bar chart is very symmetric with one value of $6$ breaking this pattern a little bit. The standard deviation and interquartile range for this shift is smaller than the four-hour shifts. This suggests the number of loyalty sign-ups is less variable for this shift. It is worth mentioning though this dataset is a lot smaller with $13$ shifts recorded. The bar chart for both shifts is shown below: $\mu_3 \approx 3.54$, $\sigma^{2}_3 \approx 3.37$, $\sigma_3 \approx 1.84$, $M_3 = 3.0$, and $R_3 = 3.0$. From this chart it seems to follow a Poisson distribution well as it follows the shape of this sort of distribution. The Poisson distribution will be discussed shortly.

<img width="757" height="570" alt="Screenshot From 2026-11-25 14-31-01" src="https://github.com/user-attachments/assets/410dd545-dbff-4164-b6b4-89b163331226" />

Moving on to waiting times the histogram for this is shown above for 177 data values: $\mu_4 \approx 8.36$, $\sigma^{2}_4 \approx 51.43$, $\sigma \approx 7.17$, $M_4 = 6.0$, and $R_4 = 8.0$. This histogram has a single mode at (approximately) the $1$ to $5$ bin. It can be argued that this is bimodal with the second mode being at (approximately) the $18$ to $22$ bin. This histogram has a decreasing trend which suggests fitting it to a geometric distribution would be a good idea. This will also be discussed shortly.

## Fitting my first models

### The Poisson process

We can define something called a Poisson process. The assumptions for this are as follows:
1. The mean and variance are approximately even.
2. Events are independent. For this situation it means one person saying yes or no to a loyalty card does not affect another's.
3. The rate of occurrence of each event is constant. That is the rate of loyalty signups is constant.
4. Events occur singly. Two people cannot sign up to a loyalty card at the same time.

For both shifts $\mu_3 \approx 3.54$ and $\sigma^{2}_3 ≈ 3.37$. These values are close together so the first assumption seems to be met.

As for the second it is much more difficult to determine. It could be said that the events are not independent as one person saying yes or no to a loyalty card affects another. After all humans are social animals. I would however argue against this as if someone generally wanted a loyalty card would say yes even if the person in front answered no and vice-versa. I had this happen many times in the collection of this data. A main concern about independence is the fact that family members or friendship groups who come to the till separately would answer differently. This was overcome by asking only one person in this family or friend from the group.

For the third assumption this may not be met. Through my collection of data there were certain days where I constantly got loads of signups and some where I got little. An example of this is when I worked on Easter Sunday where I only got $1$. It is worth mentioning though that not enough data has been collected to verify this claim. That aside it seems the more people that you have to ask the more you are likely to get. This can change especially around the Christmas period. We will return to these points later. A different model will be given were we can take this into account.

Finally for the last assumption since I can only serve one customer at a time I could only sign up at most one person. This assumption is certainly met.

So assumptions $1$, $2$, and $4$ seem to be met but not $3$. We will ignore this for the time being.

The Poisson distribution is written as $Y \sim Poisson(\lambda)$ and it has probability mass function (p.m.f):

$$
f(x) = \frac{e^{\lambda}(\lambda)^{y}}{y!}
$$

The variable $y$ takes values $0, 1, 2, 3, \ldots$. Note it only takes integers or more accurately natural numbers. This distribution is thus called a discrete distribution which means its function is a p.m.f.

The parameter $\lambda$ is the expected number of events. In this context it is the mean number of loyalty signups per shift. The output for this function is the probability of me obtaining $y$ amount of loyalty cards.

A Poisson process is written as $Y \sim Poisson(t\lambda)$ and it has p.m.f:

$$
f(y) = \frac{e^{-t\lambda}(t\lambda)^{y}}{y!}
$$

The variable $y$ takes values $0, 1, 2, 3, \ldots$.

Here it takes an extra parameter which is time. Here we are going to define time as number of shifts. So the Poisson process for $5$ shifts is given by $Y \sim Poisson(5\lambda)$. Time can also be numbers such as half an hour or $50$ seconds but we will not discuss this any further.

From my initial analysis $\lambda = 3.54$. Hence our distribution is $Y \sim Poisson(3.54)$. Here $t = 1$ as we are just talking about the probability distribution for each single shift. A table of probabilities for each number of loyalty card signups in a shift are given below:

<img width="588" height="365" alt="Screenshot From 2026-11-25 15-07-48" src="https://github.com/user-attachments/assets/304f0f91-be12-4c59-a54d-cc1c18871b7e" />

### The Geometric distribution

We will now move on to waiting times for a loyalty sign up which we will model them using a Geometric distribution.

The Geometric Distribution is derived as the waiting time for $1, 2, 3, 4, 5, \ldots$ Bernoulli trial events until a ”success”. A Bernoulli trial is defined to be:

$$
f(y) = p(1-p)^{1-y}
$$

for $y = 0, 1$ where $1$ is a success with probability $p$ and $0$ a failure with probability $1 − p$. Here a success is someone saying yes to a loyalty card and a failure is someone saying no.

It has the following assumptions:
1. Events are independent. For this situation it means one person saying yes or no to a loyalty card does not affect another's.
2. The probability of a success is constant. That is the probability the next person says yes to a loyalty card is constant throughout.
3. Each trial has only two possible outcomes a success (they say yes to a loyalty card) or a failure (they say no).

Again, I would say that the first assumption is true with the same reason I gave when talking about the Poisson process. I also see no reason why the second assumption does not hold. After all I can’t control who comes to the till next. They could very well say yes or no at a constant rate. I would say this assumption is then reasonable. Since I discounted anyone who already had a loyalty card assumption $3$ certainly holds.

The Geometric distribution is written as $Y \sim G_1(p)$ and it has p.m.f function:

$$
f(y) = p(1-p)^{y-1}
$$

The variable $y$ takes values $1, 2, 3, \ldots$. Again we can say this is a discrete distribution.

Here p is the probability of getting a loyalty sign up from the next person asked. How do we calculate p though? It can be shown (but I will not do so here) that p is the reciprocal of the mean for all the waiting times. Well from my initial analysis:

$$
\mu_4 = \frac{1480}{177}
$$

so,

$$
p = \frac{177}{1480}
$$

Hence our distribution is $Y \sim G_1\left(\frac{177}{1480}\right)$
