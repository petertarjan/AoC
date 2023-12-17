#!/usr/bin/ruby
depth=0
horiz=0
aim=0
while x=gets do
  cmd,v=x.split
  v=v.to_i
  if cmd=="forward" then
    horiz+=v
    depth+=aim*v
  elsif cmd=="down" then
    aim+=v
  elsif cmd=="up" then
    aim-=v
  end
end
p depth*horiz
