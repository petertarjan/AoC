#!/usr/bin/ruby
require 'set'

def rot_x(v)
  [v[0],v[2],-v[1]]
end
def rot_y(v)
  [v[2],v[1],-v[0]]
end
def rot_z(v)
  [v[1],-v[0],v[2]]
end

def rot(v,c)
  vc=v.clone
  if c<4 then c.times{ vc=rot_x(vc) }
  elsif c<8 then
    vc=rot_y(vc)
    (c-4).times{ vc=rot_z(vc) }
  elsif c<12 then
    vc=rot_y(vc)
    vc=rot_y(vc)
    (c-8).times{ vc=rot_x(vc) }
  elsif c<16
    vc=rot_y(vc)
    vc=rot_y(vc)
    vc=rot_y(vc)
    (c-12).times{ vc=rot_z(vc) }
  elsif c<20
    vc=rot_z(vc)
    (c-16).times{ vc=rot_y(vc) }
  else
    vc=rot_z(vc)
    vc=rot_z(vc)
    vc=rot_z(vc)
    (c-20).times{ vc=rot_y(vc) }
  end
  vc
end

def match(s1,s2)
  d=Hash.new(0)
  s1.each{|p1|
    s2.each{|p2|
      dx=p2[0]-p1[0]
      dy=p2[1]-p1[1]
      dz=p2[2]-p1[2]
      d[[dx,dy,dz]]+=1
      if d[[dx,dy,dz]]==12 then
        return dx,dy,dz
      end
    }
  }
  nil
end

s=[]
while x=gets do
  x=x.strip
  if /--- scanner [0-9]+ ---/.match(x) then
    s << []
  else
    a=x.split(",")
    if a.size==3 then
      s.last << a.map{|s|s.to_i}
    end
  end
end


sol=[s[0]]
rest=Array(1...s.size)
pos=[[0,0,0]]
while rest.size>0 do
  osols=sol.size
  rest.size.times{|i|
    24.times{|c|
      rt=s[rest[i]].map{|v| rot(v,c)}
      sol.each{|b|
        v=match(rt,b)
        if v then
          pos << v
          sol << rt.map{|r| [r[0]+v[0],r[1]+v[1],r[2]+v[2]] }
          rest[i]=rest[-1]
          rest.pop
          break
        end
      }
      if sol.size>osols then break end
    }
    if sol.size>osols then break end
  }
end

#p sol.size
sl=Set[]
sol.each{|s| s.each{|v| sl << v} }
puts "part1: "+sl.size.to_s
maxdist=0
(pos.size-1).times{|i|
  (i+1...pos.size).each{|j|
    dist=(pos[i][0]-pos[j][0]).abs+(pos[i][1]-pos[j][1]).abs+(pos[i][2]-pos[j][2]).abs
    maxdist=[maxdist,dist].max
  }
}
puts "part2: "+maxdist.to_s
