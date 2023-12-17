#!/usr/bin/ruby
a=gets.split(",").map &:to_i
best=999999999
b_i=-1
(a.min..a.max).each{|x| best=[best, a.inject(0){|s,y| s+((y-x)*(y-x)+(y-x).abs)/2}].min }
p best



