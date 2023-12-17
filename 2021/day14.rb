#!/usr/bin/ruby
s=gets.chop
gets
d={}
while x=gets do
  a=x.chop.split
  raise "bad" unless a[1]=="->"
  d[a[0]]=a[2]
end

sl=Hash.new(0)
(s.size-1).times{|i|
  from=s[i..i+1]
  sl[from]+=1
}

def calc(sl,s)
  sum=Hash.new(0)
  sl.each{|k,v|
    sum[k[0]]+=v
    sum[k[1]]+=v
  }
  sum[s[0]]+=1
  sum[s[-1]]+=1
  
  sum.values{|v| raise "baj" unless v%2==0}

  (sum.values.max-sum.values.min)/2
end

40.times{|i|
  nsl=Hash.new(0)
  sl.each{|k,v|
    to=d[k]
    to1=k[0]+to
    to2=to+k[1]
    nsl[to1]+=v
    nsl[to2]+=v
    sl=nsl
  }
  if i==9 then puts "part1: "+calc(sl,s).to_s end
}


puts "part2: "+calc(sl,s).to_s
