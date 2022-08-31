from re import Pattern

Text = "CATGCCATTCGCATTGTCCCAGTGA"
Pattern = "CCC"
PATTERNCOUNT(Text, Pattern)
count = 0
for i in 0 : |Text|  |Pattern|
if Text(i, |Pattern|) = Pattern
count count + 1
return count