#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <cassert>

//#define PART1

using namespace std;
using ll=long long;

struct rec {
	int c,x0,x1,y0,y1,z0,z1;
};

int main() {
	vector<rec> cmd;
	set<int> xs,ys,zs;
	cmd.emplace_back();
	while (scanf("%d%d%d%d%d%d%d",&cmd.back().c,
							 &cmd.back().x0,&cmd.back().x1,
							 &cmd.back().y0,&cmd.back().y1,
							 &cmd.back().z0,&cmd.back().z1)==7) {

		++cmd.back().x1; ++cmd.back().y1;	++cmd.back().z1;

#ifdef PART1
		cmd.back().x0=max(cmd.back().x0, -50);
		cmd.back().y0=max(cmd.back().y0, -50);
		cmd.back().z0=max(cmd.back().z0, -50);

		cmd.back().x1=min(cmd.back().x1, 51);
		cmd.back().y1=min(cmd.back().y1, 51);
		cmd.back().z1=min(cmd.back().z1, 51);
#endif

		xs.insert(cmd.back().x0);
		xs.insert(cmd.back().x1);
		ys.insert(cmd.back().y0);
		ys.insert(cmd.back().y1);
		zs.insert(cmd.back().z0);
		zs.insert(cmd.back().z1);
		cmd.emplace_back();
	}
	cmd.pop_back();

	vector<int> xsv(xs.begin(),xs.end());
	vector<int> ysv(ys.begin(),ys.end());
	vector<int> zsv(zs.begin(),zs.end());

	int xsl=int(xsv.size()), ysl=int(ysv.size()), zsl=int(zsv.size());
	vector<vector<vector<bool> > > grid(xsl-1,vector<vector<bool> >(ysl-1,vector<bool>(zsl-1,false)));
	
	for (const auto& c : cmd) {
		int xi0=lower_bound(xsv.begin(),xsv.end(),c.x0)-xsv.begin();
		int xi1=lower_bound(xsv.begin(),xsv.end(),c.x1)-xsv.begin();
		int yi0=lower_bound(ysv.begin(),ysv.end(),c.y0)-ysv.begin();
		int yi1=lower_bound(ysv.begin(),ysv.end(),c.y1)-ysv.begin();
		int zi0=lower_bound(zsv.begin(),zsv.end(),c.z0)-zsv.begin();
		int zi1=lower_bound(zsv.begin(),zsv.end(),c.z1)-zsv.begin();

#ifndef PART1
		assert(xi0<xi1);
		assert(yi0<yi1);
		assert(zi0<zi1);
#endif
		for (int xi=xi0;xi<xi1;++xi) {
			for (int yi=yi0;yi<yi1;++yi) {
				fill(grid[xi][yi].begin()+zi0,grid[xi][yi].begin()+zi1,bool(c.c));
			}
		}
	}
	ll sol=0ll;
	for (int xi=0;xi<xsl-1;++xi) {
		const ll xa=xsv[xi+1]-xsv[xi];
		for (int yi=0;yi<ysl-1;++yi) {
			const ll xya=xa*(ysv[yi+1]-ysv[yi]);
			for (int zi=0;zi<zsl-1;++zi) {
				sol+=(zsv[zi+1]-zsv[zi])*xya*ll(grid[xi][yi][zi]);
			}
		}
	}
	printf("%lld\n",sol);
	return 0;
}
