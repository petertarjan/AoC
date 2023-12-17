#!/usr/bin/ruby
sol=0
while x=gets do
  s=x.split
  raise "wrong input" unless s.size==15
  (10..14).each{|i| if [2,3,4,7].include? s[i].size  then sol+=1 end }
end
print sol

