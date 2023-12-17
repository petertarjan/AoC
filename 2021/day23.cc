#include <iostream>
#include <string>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <cassert>
#include "day23.h"

//#define ORIGIN

using namespace std;

int main() {
	string s;
	cin >> s;
	priority_queue<pair<int, string> > pq;
	pq.push(make_pair(0, s));
	const string goal=".......ABCDABCD";
	unordered_map<string, int> highest;
#ifdef ORIGIN
	unordered_map<string, string> origin;
#endif
	highest[s]=0;
	int v[256]={};
	v['A']=1;
	v['B']=10;
	v['C']=100;
	v['D']=1000;
	for (;;) {
		assert(!pq.empty());
		auto st=pq.top();
		pq.pop();
		int high=highest[st.second];
		assert(s==st.second || high < 0);
		int odist=st.first;
		if (odist < high) continue;
		assert(odist==high);
		if (st.second==goal) {
			cout << -odist << endl;
			break;
		}
		for (int i=0;i<vss;++i) {
			int from=vs[i].from;
			int to=vs[i].to;
			char fromc=st.second[from];
			if (fromc!='.' &&	st.second[to]=='.' &&
					all_of(vs[i].is.begin(),vs[i].is.end(),[&st](char o){ return st.second[o]=='.';}))
				{
					if (to>=7 && 'A'+char((to-7)%4)!=fromc) continue;
					string ns=st.second;
					ns[to]=fromc;
					ns[from]='.';
					auto it=highest.find(ns);
					int ndist=odist-vs[i].dist*v[fromc];
					if (it==highest.end()) {
						highest[ns]=ndist;
#ifdef ORIGIN
						origin[ns]=st.second;
#endif
						pq.emplace(make_pair(ndist,move(ns)));
					} else if (it->second < ndist) {
						it->second=ndist;
#ifdef ORIGIN
						origin[ns]=st.second;
#endif
						pq.emplace(make_pair(ndist,move(ns)));
					}
				}
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
