#!/usr/bin/ruby
sol=0

def pairof(c)
  if c==")" then return "("
  elsif c=="]" then return "["
  elsif c=="}" then return "{"
  elsif c==">" then return "<"
  else raise "wut"
  end
end

while x=gets do
  s=[]
  for c in x.chop.chars
    if ['[','(','{','<'].include? c then s << c
    elsif pairof(c)==s.last then s.pop
    elsif c==')' then sol+=3; break
    elsif c==']' then sol+=57; break
    elsif c=='}' then sol+=1197; break
    elsif c=='>' then sol+=25137; break
    else raise "("+c+")" end
  end
end
p sol
