#include <iostream>
#include <string>
#include <algorithm>

int main() {
	std::string line;
	int s=0;
	int maxs[3]={0,0,0};
	while (std::getline(std::cin, line)) {
		if (line.empty()) {
			maxs[0]=std::max(s,maxs[0]);
			std::sort(maxs,maxs+3);
			s=0;
		} else {
			s+=atoi(line.c_str());
		}
	}
	maxs[0]=std::max(s,maxs[0]);
	std::sort(maxs,maxs+3);
	std::cout<<"Part 1: "<<maxs[2]<<std::endl;
	std::cout<<"Part 2: "<<maxs[0]+maxs[1]+maxs[2]<<std::endl;
	return 0;
}
