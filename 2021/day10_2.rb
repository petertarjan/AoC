#!/usr/bin/ruby

def pairof(c)
  if c==")" then return "("
  elsif c=="]" then return "["
  elsif c=="}" then return "{"
  elsif c==">" then return "<"
  else raise "wut"
  end
end
sls=[]
while x=gets do 
  sol=0
  s=[]
  good=true
  for c in x.chop.chars
    if ['[','(','{','<'].include? c then s << c
    elsif pairof(c)==s.last then s.pop
    elsif c==')' then good=false; break
    elsif c==']' then good=false; break
    elsif c=='}' then good=false; break
    elsif c=='>' then good=false; break
    else raise "("+c+")" end
  end
  if good then
    while s.size>0 do
      c=s.pop
      if c=='(' then sol=sol*5+1
      elsif c=='[' then sol=sol*5+2
      elsif c=='{' then sol=sol*5+3
      elsif c=='<' then sol=sol*5+4
      else raise "ooops" end       
    end
    sls << sol
  end
end
p sls.sort[sls.size/2]

