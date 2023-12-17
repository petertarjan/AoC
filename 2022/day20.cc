#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;
using ll=long long;

void dump(const vector<int>& a,const vector<int>& pos) {
	vector<int> dumpv(a.size(),-987654321);
	for (int i=0;i<int(a.size());++i) dumpv[pos[i]]=a[i];
	for (int i=0;i<int(a.size());++i) cout<<' '<<dumpv[i];
	cout<<endl;
}

int al;

void shuffle(const vector<int>& a,vector<int>& pos,ll mul=1ll) {
	for (int i=0;i<al;++i) {
		int p=pos[i];
		int np=(p+mul*a[i])%(al-1);	
		if (np<0) np+=al-1;
		if (np<p) {
			for (int i=0;i<al;++i) {
				if (pos[i]>=np && pos[i]<p) ++pos[i];
			}
		} else if (np>p) {
			for (int i=0;i<al;++i) {
				if (pos[i]>p && pos[i]<=np) --pos[i];
			}
		}
		pos[i]=np;
	}
}

int getsol(const vector<int>& a,vector<int>& pos) {
	int pos0=-1;
	for (int i=0;i<al;++i) if (a[i]==0) { pos0=pos[i]; break; }
	assert(pos0>=0);
	int pos1000=(pos0+1000)%al;
	int pos2000=(pos0+2000)%al;
	int pos3000=(pos0+3000)%al;
	int sol=0;
	for (int i=0;i<al;++i) {
		if (pos[i]==pos1000) sol+=a[i];
		else if (pos[i]==pos2000) sol+=a[i];
		else if (pos[i]==pos3000) sol+=a[i];
	}
	return sol;
}

int main() {
	int i;
	vector<int> a;
	while (cin>>i) a.push_back(i);
	al=int(a.size());
	vector<int> pos(al);
	iota(pos.begin(),pos.end(),0);
	shuffle(a,pos);
	cout<<"Part1: "<<getsol(a,pos)<<endl;
	iota(pos.begin(),pos.end(),0);
	const ll M=811589153ll;
	for (i=0;i<10;++i) shuffle(a,pos,M);
	cout<<"Part2: "<<M*getsol(a,pos)<<endl;
	return 0;
}
