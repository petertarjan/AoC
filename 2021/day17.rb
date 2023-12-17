#!/usr/bin/ruby
a=gets.strip.split
raise "bad" unless a[0]=="target" and a[1]=="area:"
x=a[2].split("=")
y=a[3].split("=")
raise bad2 unless x[0]=="x" and y[0]=="y"
x=x[1].split("..").map &:to_i
y=y[1].split("..").map &:to_i
#p x,y

def xreach(dx)
  dx*(dx+1)/2
end

idx=0
while xreach(idx)<x[0] do idx+=1 end

dy=-y[0]-1
puts "part1: "+xreach(dy).to_s

sol=0
(idx..x[1]).each{|adx|
  (y[0]..-y[0]-1).each{|ady|
#    debuglog = adx.to_s+","+ady.to_s
    dx=adx
    dy=ady
    px=0
    py=0
    while true do
      px+=dx
      py+=dy
      dy-=1
      if dx>0 then dx-=1 end
      if px>x[1] or py<y[0] then break end
      if px>=x[0] and py<=y[1] then
        sol+=1
#        puts debuglog
        break
      end
    end
  }
}

puts "part2: "+sol.to_s



