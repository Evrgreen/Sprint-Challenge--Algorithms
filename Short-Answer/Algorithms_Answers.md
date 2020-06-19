#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I


 O(n), initially looks like n**3 but because after  a=n*n it should always run in linear time 

O(n log n) the nested j loop is a function of n so should be log n complexity 

O(n) the function is being called recursively as n-1 should linearly shrink or grow with n




## Exercise II

This is a perfect opportunity to use a binary search. Since floors are ordered in ascending order, we already have a sorted list of values to work off of. So what we should do is choose the midpoint and see if the egg breaks or doesnt break when tossed from that floor, if it doesn't break then we divide the remaining rooms above us in half and move to that point. If it does break, then we move to the midpoint of the rooms below us. We then repeat this process until we find the exact highest floor you can drop an egg from so that it doesn't break.
The runtime of this algo is O(log N). Which means that if we moved from 32 -> 64 floors, it would only take 1 extra move to find the exact floor


