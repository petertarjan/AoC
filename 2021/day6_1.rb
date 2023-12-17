#!/usr/bin/ruby
i=gets.split(",").map &:to_i
a=Array.new(9,0)
i.each{|x|a[x]+=1}
80.times{
  z=a[0]
  8.times{|x|a[x]=a[x+1]}
  a[8]=z
  a[6]+=z
}
p a.inject &:+
