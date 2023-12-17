#!/usr/bin/ruby
depth=0
horiz=0
while x=gets do
  cmd,v=x.split
  v=v.to_i
  if cmd=="forward" then
    horiz+=v
  elsif cmd=="down" then
    depth+=v
  elsif cmd=="up" then
    depth-=v
  end
end
p depth*horiz
