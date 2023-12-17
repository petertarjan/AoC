#!/usr/bin/ruby

$dec=gets.strip

def enhance(pic,inf)
  r=pic.size
  c=pic[0].size
  ret=[]
  (-2...r).each{|rr|
    ret << []
    (-2...c).each{|cc|
      ch=0
      3.times{|dr|
        3.times{|dc|
          point=inf
          if rr+dr>=0 and rr+dr<r and cc+dc>=0 and cc+dc<c then
            point=pic[rr+dr][cc+dc]
          end
          if point=="#" then ch+=256>>(3*dr+dc) end
        }
      }
      ret[-1] << $dec[ch]
    }
  }
  inf=inf=="." ? $dec[0] : $dec[511]
  [ret.map{|l|l.join("")},inf]
end

raise "bad input" unless gets.strip==""
s=[]
while x=gets do
  s << x.strip
end

sl,inf=enhance(s,".")
sl,inf=enhance(sl,inf)
print "part1: ",(sl.map{|s|s.chars.count("#")}.inject &:+),"\n"

48.times{ sl,inf=enhance(sl,inf) }

print "part2: ",(sl.map{|s|s.chars.count("#")}.inject &:+),"\n"

