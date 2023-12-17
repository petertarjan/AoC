#!/usr/bin/ruby
g=[]
while x=gets do
  g << x.chop
end
steps=0
while true do
  stop=true
  ng=[]
  g.each{|r|
    ns = []
    r.chars.each_with_index{|c,i|
      stop0=stop
      if c=="." and r[i-1]==">" then ns << ">" ; stop=false
      elsif c==">" and (r[i+1] || r[0])=="." then ns << "."
      else ns << c end
    }
    ng << ns.join("")
  }
  g=ng
  ng=[]
  g.each_with_index{|r,rr|
    ns = []
    r.chars.each_with_index{|c,i|
      if c=="." and g[rr-1][i]=="v" then ns << "v" ; stop=false
      elsif c=="v" and (g[rr+1][i] rescue g[0][i])=="." then ns << "."
      else ns << c end
    }
    ng << ns.join("")
  }
  g=ng
  steps+=1
#  print g.join("\n")+"\n\n"
  if stop then break end
end

print steps
