#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <cassert>
using namespace std;

template<typename T>
ostream& operator<<(ostream& o,const vector<T>& vv) {
  if (vv.size()) {
    o<<vv[0];
    for (size_t i=1;i<vv.size();++i) o<<' '<<vv[i];
  }
  return o;
}

class vremap {
	unordered_map<string,int> m;
	vector<string> vmi;
public:
	static int next;
	int getID(const string& s) {
		auto it=m.find(s);
		if (it==m.end()) {
			m[s]=++next;
			vmi.emplace_back(s);
			return next;
		}
		return it->second;
	}
	string gets(int i) {
		assert(0<=i && i<int(vmi.size()));
		return vmi[i];
	}
};
int vremap::next=-1;

struct cell {
	vector<int> out;
	int cap;
};

vremap vm;
vector<cell> cells;

inline int posmask(int pos,int mask) {
	return (pos<<16)|mask;
}

inline int getpos(int posmask) {
	return posmask>>16;
}

inline int getmask(int posmask) {
	return posmask&((1<<16)-1);
}

int main() {
	string line;
	assert(vm.getID("AA")==0);
	while (getline(cin, line)) {
		int input=vm.getID(line.substr(6,2));
		//		cout<<input<<" ->";
		if (int(cells.size())<=input) cells.resize(input+1);
		int pr=int(line[23]-'0');
		int i=24;
		while (line[i]!=';') { pr=10*pr+int(line[i]-'0'); ++i; }
		cells[input].cap=pr;
		i+=24;
		if (line[i]==' ') ++i;
		for (;;) {
			int output=vm.getID(line.substr(i,2));
			cells[input].out.push_back(output);
			if (line[i+2]!=',') break;
			i+=4;
		}
	}
	const int N=vremap::next+1;
	vector<vector<int> > shortest(N,vector<int>(N,999999999));
	for (int i=0;i<N;++i) {
		shortest[i][i]=0;
		for (int e : cells[i].out) {
			shortest[i][e]=1;
		}
	}
	for (int k=0;k<N;++k) {
		for (int i=0;i<N;++i) {
			if (i==k) continue;
			for (int j=0;j<N;++j) {
				if (j==i || j==k) continue;
				shortest[i][j]=min(shortest[i][j],shortest[i][k]+shortest[k][j]);
			}
		}
	}
	//	cout<<shortest<<endl;
	unordered_map<int,int> n2x;
	vector<int> x2n={0};
	n2x[0]=0;
	int N1=1;
	for (int i=1;i<N;++i) if (cells[i].cap>0) {
			x2n.push_back(i);
			n2x[i]=N1;
			++N1;
		}
	vector<vector<int> > shr(N1);
	vector<int> cp;
	for (int i=0;i<N1;++i) {
		cp.push_back(cells[x2n[i]].cap);
		for (int j=0;j<N1;++j) {
			if (i==j) shr[i].push_back(0);
			else {
				shr[i].push_back(shortest[x2n[i]][x2n[j]]+1);
			}
		}
	}
	
	//	cout<<N1<<endl;
	//	cout<<shr<<endl;
	/*
	for (int i=0;i<N1;++i) {
		cout<<vm.gets(x2n[i])<<":\n";
		for (int j=0;j<N1;++j) {
			cout<<' '<<vm.gets(x2n[j])<<':'<<shr[i][j];
		}
		cout<<endl;
		}*/
	
	unordered_map<int,int> steps[30];
	steps[0][posmask(0,0)]=0; // pos, mask -> max. score
	int maxscore=0;
	for (int i=0;i<30;++i) {
		for (auto p : steps[i]) {
			int pos=getpos(p.first);
			int mask=getmask(p.first)|(1<<pos);
			int score=p.second+cp[pos]*(30-i);
			maxscore=max(score,maxscore);
			for (int j=0;j<N1;++j) {
				if (((mask>>j)&1)==0) {
					int nexti=i+shr[pos][j];
					if (nexti<30) steps[nexti][posmask(j,mask)]=max(steps[nexti][posmask(j,mask)],score);
				}
			}
		}
	}
	cout<<maxscore<<endl;
	return 0;
}
