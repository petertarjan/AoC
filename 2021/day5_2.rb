#!/usr/bin/ruby
t=[]
sol=0
while x=gets do
  x=x.chop.split
  raise "wrong input" unless x.size==3
  raise "wrong input" unless x[1]=="->"
  x1,y1=x[0].split(",").map &:to_i
  x2,y2=x[2].split(",").map &:to_i
  if x1==x2 then
    from=[y1,y2].min
    to=[y1,y2].max
    while to>=t.size do
      t << []
    end
    (from..to).each do |y|
      while x1>=t[y].size do
        t[y] << 0
      end
      if t[y][x1]==1 then
        sol+=1
      end
      t[y][x1]+=1
#      puts y.to_s+","+x1.to_s
    end
  elsif y1==y2 then
    while y1>=t.size do
      t << []
    end
    from=[x1,x2].min
    to=[x1,x2].max
    while to>=t[y1].size do
      t[y1] << 0
    end
    (from..to).each do |x|
      if t[y1][x]==1 then
        sol+=1
      end
      t[y1][x]+=1
#      puts y1.to_s+","+x.to_s
    end
  else
    if x1>x2 then
      x1,x2=x2,x1
      y1,y2=y2,y1
    end
    if y1<y2 then
      raise "wrong input" unless y2==y1+x2-x1
      (x1..x2).each do |x|
        y=y1+x-x1
        while y>=t.size do
          t << []
        end
        while x>=t[y].size do
          t[y] << 0
        end
        if t[y][x]==1 then
          sol+=1
        end
        t[y][x]+=1
      end
    else
      raise "wrong input" unless y2==y1+x1-x2
      (x1..x2).each do |x|
        y=y1-x+x1
        while y>=t.size do
          t << []
        end
        while x>=t[y].size do
          t[y] << 0
        end
        if t[y][x]==1 then
          sol+=1
        end
        t[y][x]+=1
      end
    end
  end
end

print sol

