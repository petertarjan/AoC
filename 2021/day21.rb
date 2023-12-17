#!/usr/bin/ruby
p1s=p1=gets.strip.split[-1].to_i
pp1=0
pp2=0
p2s=p2=gets.strip[-1].to_i
d=1
r=0
print "part1: "
while true do
  p1=(p1+d-1)%10+1
  d=d%100+1
  p1=(p1+d-1)%10+1
  d=d%100+1
  p1=(p1+d-1)%10+1
  pp1+=p1
  d=d%100+1
  r+=3
  if pp1>=1000 then
    print pp2*r
    break
  end
  p2=(p2+d-1)%10+1
  d=d%100+1
  p2=(p2+d-1)%10+1
  d=d%100+1
  p2=(p2+d-1)%10+1
  pp2+=p2
  d=d%100+1
  r+=3
  if pp2>=1000 then
    print pp1*r
    break
  end
end

puts

# pp1,pp2,p1-1,p2-1
# 21*21*10*10
next1=Array.new(21) { Array.new(31) { Array.new(10) { Array.new(10,0) } } }
next2=Array.new(21) { Array.new(31) { Array.new(10) { Array.new(10,0) } } }

cmb=[0,0,0,1,3,6,7,6,3,1]

next1[0][0][p1s-1][p2s-1]=1

p1win=0
p2win=0

21.times{|pp1|
  21.times{|pp2|
    10.times{|p1m1|
      p1=p1m1+1
      10.times{|p2m1|
        p2=p2m1+1
        (3..9).each{|d|
          p1n=(p1-1+d)%10+1
          pp1n=pp1+p1n
          raise "elq" unless pp1n<=30
          incr=next1[pp1][pp2][p1-1][p2-1]*cmb[d]
          if pp1n>20 then
            p1win+=incr
          else
            next2[pp1n][pp2][p1n-1][p2-1]+=incr
          end

          p2n=(p2-1+d)%10+1
          pp2n=pp2+p2n
          raise "elq" unless pp2n<=30
          incr=next2[pp1][pp2][p1-1][p2-1]*cmb[d]
          if pp2n>20 then
            p2win+=incr
          else
            next1[pp1][pp2n][p1-1][p2n-1]+=incr
          end
        }
      }
    }
  }
}
print "part2: ",[p1win,p2win].max

