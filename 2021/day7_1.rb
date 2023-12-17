#!/usr/bin/ruby
i=gets.split(",").map &:to_i
i=i.sort
v=i.size/2

p v.times.inject(0){|a,x|i[v]-i[x]+a}+(v+1...i.size).inject(0){|a,x|i[x]-i[v]+a}


