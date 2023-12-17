#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

inline int enc(int x,int y,int z) {
	return x|(y<<8)|(z<<16);
}

inline int getx(int e) {
	return e&255;
}

inline int gety(int e) {
	return (e>>8)&255;
}

inline int getz(int e) {
	return (e>>16)&255;
}

int main() {
	unordered_set<int> pt;

	string line;
	while (getline(cin, line)) {
		//	while (scanf("%d%d%d",&x,&y,&z)==3) {
		auto c1=line.find(',');
		auto c2=line.find(',',c1+1);
		int x=atoi(line.substr(0, c1).c_str());
		int y=atoi(line.substr(c1+1,c2-c1-1).c_str());
		int z=atoi(line.substr(c2+1).c_str());
		pt.insert(enc(x,y,z));
	}
	int sol=0;
	for (auto p : pt) {
		int x=getx(p);
		int y=gety(p);
		int z=getz(p);
		if (pt.find(enc(x+1,y,z))==pt.end()) ++sol;
		if (pt.find(enc(x-1,y,z))==pt.end()) ++sol;
		if (pt.find(enc(x,y+1,z))==pt.end()) ++sol;
		if (pt.find(enc(x,y-1,z))==pt.end()) ++sol;
		if (pt.find(enc(x,y,z+1))==pt.end()) ++sol;
		if (pt.find(enc(x,y,z-1))==pt.end()) ++sol;
	}
	cout<<"Part 1: "<<sol<<endl;

	int vis[24][24][24];
	for (int x=0;x<24;++x) {
		for (int y=0;y<24;++y) {
			for (int z=0;z<24;++z) {
				if (pt.find(enc(x-1,y-1,z-1))==pt.end()) vis[x][y][z]=-1;
				else vis[x][y][z]=0;
			}
		}
	} // -1: empty, 0: wall, 1: outer space
	vector<int> prc;
	vis[0][0][0]=1;
	prc.push_back(enc(0,0,0));
	while (!prc.empty()) {
		int xyz=prc.back();
		int x=getx(xyz);
		int y=gety(xyz);
		int z=getz(xyz);
		//		cout<<x<<' '<<y<<' '<<z<<endl;
		prc.pop_back();
		if (x>0 && vis[x-1][y][z]==-1) { vis[x-1][y][z]=1; prc.push_back(enc(x-1,y,z)); }
		if (y>0 && vis[x][y-1][z]==-1) { vis[x][y-1][z]=1; prc.push_back(enc(x,y-1,z)); }
		if (z>0 && vis[x][y][z-1]==-1) { vis[x][y][z-1]=1; prc.push_back(enc(x,y,z-1)); }
		if (x<23 && vis[x+1][y][z]==-1) { vis[x+1][y][z]=1; prc.push_back(enc(x+1,y,z)); }
		if (y<23 && vis[x][y+1][z]==-1) { vis[x][y+1][z]=1; prc.push_back(enc(x,y+1,z)); }
		if (z<23 && vis[x][y][z+1]==-1) { vis[x][y][z+1]=1; prc.push_back(enc(x,y,z+1)); }
	}
	sol=0;
	for (int x=0;x<23;++x) {
		for (int y=0;y<24;++y) {
			for (int z=0;z<24;++z) {
				if (vis[x][y][z]==0 && vis[x+1][y][z]==1) ++sol;
				if (vis[x][y][z]==1 && vis[x+1][y][z]==0) ++sol;
			}
		}
	}
	for (int x=0;x<24;++x) {
		for (int y=0;y<23;++y) {
			for (int z=0;z<24;++z) {
				if (vis[x][y][z]==0 && vis[x][y+1][z]==1) ++sol;
				if (vis[x][y][z]==1 && vis[x][y+1][z]==0) ++sol;
			}
		}
	}
	for (int x=0;x<24;++x) {
		for (int y=0;y<24;++y) {
			for (int z=0;z<23;++z) {
				if (vis[x][y][z]==0 && vis[x][y][z+1]==1) ++sol;
				if (vis[x][y][z]==1 && vis[x][y][z+1]==0) ++sol;
			}
		}
	}
	cout<<"Part 2: "<<sol<<endl;
	return 0;
}
