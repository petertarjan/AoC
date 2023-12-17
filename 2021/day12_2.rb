#!/usr/bin/ruby
$rt={}
while x=gets do
  a,b=x.chop.split("-")
  if not $rt[a] then $rt[a]=[b]
  else $rt[a] << b end
  if not $rt[b] then $rt[b]=[a]
  else $rt[b] << a end
end

def trav2()
  $rt[$r.last].each{|n|
    if n.downcase==n and $r.include? n then next end
    if n=="end" then $s+=1
    else
      $r << n
      trav2()
      $r.pop
    end
  }
end

def traverse()
  $rt[$r.last].each{|n|
    if n.downcase==n and $r.include? n then
      if not ["start","end"].include? n then
        $r << n
        trav2()
        $r.pop
      end
    elsif n=="end" then $s+=1
    else
      $r << n
      traverse()
      $r.pop
    end
  }
end

$r=["start"]
$s=0
traverse()
p $s
