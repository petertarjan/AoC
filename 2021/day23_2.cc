#include <iostream>
#include <string>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <cassert>
#include "day23_2.h"

//#define ORIGIN

using namespace std;

using ll=long long;

ll hlp[256]={};
char hlpi[5]={'.','A','B','C','D'};

ll p5[24]={1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125,
				 244140625, 1220703125, 6103515625ll, 30517578125ll, 152587890625ll,
				 762939453125ll, 3814697265625ll, 19073486328125ll, 95367431640625ll,
				 476837158203125ll, 2384185791015625ll, 11920928955078125ll};

// least significant first
ll pack(string s) {
	assert(s.size()==23u);
	ll ret=0ll;
	for (int i=0;i<23;++i) {
		ret+=hlp[s[i]]*p5[i];
	}
	return ret;
}

char geti(ll x,int i) {
	return (x/p5[i])%5;
}

string unpack(ll x) {
	string s("                       ");
	for (int i=0;i<23;++i) {
		s[i]=hlpi[x%5ll];
		x/=5ll;
	}
	return s;
}

int main() {
	for (int i=0;i<5;++i) hlp[hlpi[i]]=i;

	string s;
	cin >> s;
	s=s.substr(0,11)+"DCBADBAC"+s.substr(11);

	priority_queue<pair<int, ll> > pq;
	ll sll=pack(s);
	pq.push(make_pair(0, sll));
	const string goal=".......ABCDABCDABCDABCD";
	ll goalll=pack(goal);

	//	cout << s << endl << goal << endl;
	unordered_map<ll, int> highest;
#ifdef ORIGIN
	unordered_map<ll, ll> origin;
#endif
	highest[sll]=0;
	int v[5]={0,1,10,100,1000};
	int printlog=1;
	for (;;) {
		assert(!pq.empty());
		auto st=pq.top();
		pq.pop();
		int high=highest[st.second];
		assert(sll==st.second || high < 0);
		int odist=st.first;
		if (odist < high) continue;
		assert(odist==high);
		if (st.second==goalll) {
			cout << -odist << endl;
			break;
		}
		for (int i=0;i<vss;++i) {
			int from=vs[i].from;
			int to=vs[i].to;
			if (from<7 && to<7) continue;
			char fromc=geti(st.second,from);
			if (fromc && !geti(st.second,to) &&
					all_of(vs[i].is.begin(),vs[i].is.end(),[&st](int o){ return !geti(st.second,o); } ))
				{
					if (to>=7 && char((to-7)%4+1)!=fromc) continue;
					ll nsp=st.second+p5[to]*ll(fromc)-p5[from]*ll(fromc);
					auto it=highest.find(nsp);
					int ndist=odist-vs[i].dist*v[fromc];
					if (it==highest.end()) {
						highest[nsp]=ndist;
#ifdef ORIGIN
						origin[nsp]=st.second;
#endif
						pq.emplace(make_pair(ndist,nsp));
					} else if (it->second < ndist) {
						it->second=ndist;
#ifdef ORIGIN
						origin[nsp]=st.second;
#endif
						pq.emplace(make_pair(ndist,nsp));
					}
				}
		}
		if (--printlog==0) { printlog=100000;
			cout<<pq.size()<<endl;
		}
	}

#ifdef ORIGIN
	cout << goal;
	string dbg = goal;
	for (;;) {
		dbg = origin[dbg];
		assert(!dbg.empty());
		cout << " <- " << dbg;
		if (dbg==s) break;
	}
	cout << endl;
#endif
	return 0;
}
