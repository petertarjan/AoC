#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

int main() {
	std::string line;
	int sol=0;
	int sol3=0;

	vector<int> prio3(52,0);
	int cs=0;
	while (std::getline(std::cin, line)) {
		if (line.empty()) break;
		vector<bool> prio(52,false);

		for (size_t i=0u;i<line.size()/2u;++i) {
			if ('a'<=line[i] && line[i]<='z') prio[line[i]-'a']=true;
			else if ('A'<=line[i] && line[i]<='Z') prio[line[i]-'A'+26]=true;
			else assert(false);
		}
		for (size_t i=line.size()/2u;i<=line.size();++i) {
			if ('a'<=line[i] && line[i]<='z' && prio[line[i]-'a']) {
				sol+=1+line[i]-'a';
				break;
			}
			else if ('A'<=line[i] && line[i]<='Z' && prio[line[i]-'A'+26]) {
				sol+=line[i]-'A'+27;
				break;
			}
		}

		if (cs==0) {
			for (size_t i=0u;i<line.size();++i) {
				if ('a'<=line[i] && line[i]<='z') prio3[line[i]-'a']=1;
				else if ('A'<=line[i] && line[i]<='Z') prio3[line[i]-'A'+26]=1;
				else assert(false);
			}
		}
		if (cs==1) {
			for (size_t i=0u;i<line.size();++i) {
				if ('a'<=line[i] && line[i]<='z' && prio3[line[i]-'a']) {
					prio3[line[i]-'a']=2;
				}
				else if ('A'<=line[i] && line[i]<='Z' && prio3[line[i]-'A'+26]) {
					prio3[line[i]-'A'+26]=2;
				}
			}
		}
		if (cs==2) {
			for (size_t i=0u;i<line.size();++i) {
				if ('a'<=line[i] && line[i]<='z' && prio3[line[i]-'a']==2) {
					sol3+=1+line[i]-'a';
					break;
				}
				else if ('A'<=line[i] && line[i]<='Z' && prio3[line[i]-'A'+26]==2) {
					sol3+=line[i]-'A'+27;
					break;
				}
			}
			fill(prio3.begin(),prio3.end(),0);
		}
		cs=(cs+1)%3;
	}
	cout<<"Part 1 : "<<sol<<endl;
	cout<<"Part 2 : "<<sol3<<endl;
	return 0;
}
