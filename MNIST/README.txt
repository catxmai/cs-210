Part 1

I ran 4 trials and sum-of-squares and sum-absolute using median at leaves works best, but only by a small margin 
compared to logloss. But the result fluctuated a lot too. I think because there's a lot of variance in the data and 
we're only sampling them with every run.

Running through the data's variance and stddev, column 2 (plasma glucose concentration), column 5 (2-Hour serum insulin) are the highest
of var and stddev. Also, some data has 0's (zeroes) in places where I assume there shouldn't be 0, like measurements
of thickness.
So to make it more accurate, maybe we could filter the 0's out, or plot a scatter plot and filter the extreme
outliers. 