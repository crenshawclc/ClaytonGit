def monty_hall()
	doors = [false,false,false]
	doors[rand(3)] = true
	if doors[rand(3)] == true
		return 0 
	else
		return 1
	end
end

n = 10000
wins = 0
for i in 0..n
	wins+=monty_hall()
end
puts "ended"puts "#{wins} / #{String(n)} : #{Float(wins)/Float(n)}"