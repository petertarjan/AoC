#include <iostream>
#include <string>
#include <vector>
using namespace std;

char t[6][3]={
	{'A','B','C'},
	{'A','C','B'},
	{'B','A','C'},
	{'B','C','A'},
	{'C','A','B'},
	{'C','B','A'}};

int main() {
	std::string line;
	int point=0,p2=0;
	while (std::getline(std::cin, line)) {
		if (line.empty()) break;
		char enemy=line[0];
		char coded=line[2];
		char my=t[0][coded-'X'];
		point+=1+int(my-'A');
		if (my==enemy) point+=3;
		else if (enemy=='A' && my=='B' ||
						 enemy=='B' && my=='C' ||
						 enemy=='C' && my=='A') point+=6;

		if (coded=='Y') p2+=3; else if (coded=='Z') p2+=6;
		if (coded=='Y') my=enemy;
		else if (coded=='Z') my=t[3][int(enemy-'A')];
		else my=t[4][int(enemy-'A')];
		p2+=int(my-'A')+1;
		//		cout<<my<<endl;
		//		cout<<p2<<endl;
	}
	cout<<"part1 : "<<point<<endl;
	cout<<"part2 : "<<p2<<endl;
	return 0;
}
