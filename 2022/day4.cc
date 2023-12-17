#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

int main() {
	std::string line;
	int sol=0;
	int sol2=0;
	while (std::getline(std::cin, line)) {
		if (line.empty()) break;
		size_t p0=line.find('-',0);
		int a0=atoi(line.substr(0,p0).c_str());
		size_t p1=line.find(',',p0+1u);
		int a1=atoi(line.substr(p0+1u,p1-p0-1u).c_str());
		size_t p2=line.find('-',p1+1u);
		int a2=atoi(line.substr(p1+1u,p2-p1-1u).c_str());
		size_t p3=line.find(',',p2+1u);
		int a3=atoi(line.substr(p2+1u,p3-p2-1u).c_str());
		if (a0<=a2 && a1>=a3 || a0>=a2 && a1<=a3) ++sol;
		if (max(a0,a2)<=min(a1,a3)) ++sol2;
	}
	cout<<"Part 1 : "<<sol<<endl;
	cout<<"Part 2 : "<<sol2<<endl;
	return 0;
}
