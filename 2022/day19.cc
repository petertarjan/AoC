#include <iostream>
#include <string>
#include <cassert>
using namespace std;

int bp=0,aa,ba,ca,cb,da,dc,mma;

int globalbest;

int calc(int T, int a, int b, int c, int ar, int br, int cr) {
	if (c>dc+2) return 0;
	int best=0,delta;
	//	if (a>25 || b>25 || c>2*dc) return 0;
	//	if (a>25 || b>25 || c>dc+2) return 0;

	if (cr) {
		delta=max((da-a+ar-1)/ar+1,(dc-c+cr-1)/cr+1);
		if (T+delta<24) {
			best=max(best,24-T-delta+calc(T+delta,a+ar*delta-da,b+br*delta,c+cr*delta-dc,
																		ar,br,cr));
		}
	}
	if (ar>=da && cr>=dc) return best;

	if (br && cr<dc) {
		delta=max((ca-a+ar-1)/ar+1,(cb-b+br-1)/br+1);
		if (T+delta<22) {
			best=max(best,calc(T+delta,a+ar*delta-ca,b+br*delta-cb,c+cr*delta,
												 ar,br,cr+1));
		}
	}

	delta=(ba-a+ar-1)/ar+1;
	if (T+delta<20 && br<cb) {
		best=max(best,calc(T+delta,a+ar*delta-ba,b+br*delta,c+cr*delta,
											 ar,br+1,cr));
	}

	delta=(aa-a+ar-1)/ar+1;
	if (T+delta<22-aa && ar<mma && max(22-T,0)*mma>a) {
		best=max(best,calc(T+delta,a+ar*delta-aa,b+br*delta,c+cr*delta,
											 ar+1,br,cr));
	}

	if (best>globalbest) {
		//		cout<<(globalbest=best)<<endl;
	}
	return best;
}

int calc2(int T, int a, int b, int c, int ar, int br, int cr) {
	if (c>dc+2) return 0;
	int best=0,delta;
	//	if (a>40 || b>30 || c>dc+5) return 0;
	if (cr) {
		delta=max((da-a+ar-1)/ar+1,(dc-c+cr-1)/cr+1);
		if (T+delta<32) {
			best=max(best,32-T-delta+calc2(T+delta,a+ar*delta-da,b+br*delta,c+cr*delta-dc,
																		ar,br,cr));
		}
	}
	if (ar>=da && cr>=dc) return best;

	if (br && cr<dc) {
		delta=max((ca-a+ar-1)/ar+1,(cb-b+br-1)/br+1);
		if (T+delta<30) {
			best=max(best,calc2(T+delta,a+ar*delta-ca,b+br*delta-cb,c+cr*delta,
												 ar,br,cr+1));
		}
	}

	delta=(ba-a+ar-1)/ar+1;
	if (T+delta<28 && br<cb) {
		best=max(best,calc2(T+delta,a+ar*delta-ba,b+br*delta,c+cr*delta,
											 ar,br+1,cr));
	}

	delta=(aa-a+ar-1)/ar+1;
	if (T+delta<30-aa && ar<mma && max(22-T,0)*mma>a) {
		best=max(best,calc2(T+delta,a+ar*delta-aa,b+br*delta,c+cr*delta,
											 ar+1,br,cr));
	}

	if (best>globalbest) {
		//		cout<<(globalbest=best)<<endl;
	}
	return best;
}


int main() {
	string s;
	int sol=0,sol2=1;
	while (cin>>s) {
		assert(s=="Blueprint");
		cin>>s;
		assert(s.back()==':');
		++bp;
		assert(atoi(s.c_str())==bp);
		cin>>s; assert(s=="Each"); cin>>s; assert(s=="ore"); cin>>s; assert(s=="robot"); cin>>s; assert(s=="costs");
		cin>>s;
		aa=atoi(s.c_str());
		cin>>s;
		assert(s=="ore.");
		cin>>s; assert(s=="Each"); cin>>s; assert(s=="clay"); cin>>s; assert(s=="robot"); cin>>s; assert(s=="costs");
		cin>>s;
		ba=atoi(s.c_str());
		cin>>s;
		assert(s=="ore.");
		cin>>s; assert(s=="Each"); cin>>s; assert(s=="obsidian"); cin>>s; assert(s=="robot"); cin>>s; assert(s=="costs");
		cin>>s;
		ca=atoi(s.c_str());
		cin>>s;	assert(s=="ore"); cin>>s;	assert(s=="and");
		cin>>s;
		cb=atoi(s.c_str());
		cin>>s;
		assert(s=="clay.");
		cin>>s; assert(s=="Each"); cin>>s; assert(s=="geode"); cin>>s; assert(s=="robot"); cin>>s; assert(s=="costs");
		cin>>s;
		da=atoi(s.c_str());
		cin>>s;	assert(s=="ore"); cin>>s;	assert(s=="and");
		cin>>s;
		dc=atoi(s.c_str());
		cin>>s;
		assert(s=="obsidian.");
		//		cout<<aa<<' '<<ba<<' '<<ca<<' '<<cb<<' '<<da<<' '<<dc<<endl;
		//		cout<<builda(0,0,0,0,1,0,0,0)<<endl;

		mma=max(max(ba,ca),da);
		
		globalbest=0;
		int c=calc(0,0,0,0,1,0,0);
		cout<<"part1 -> "<<c<<endl;
		sol+=bp*c;
		//		cout<<ba+cb+dc<<endl;
		if (bp<=3) {
			int c2=calc2(0,0,0,0,1,0,0);
			sol2*=c2;
			cout<<"part2 -> "<<c2<<endl;
		}
	}
	cout<<"Part1: "<<sol<<endl;
	cout<<"Part2: "<<sol2<<endl;

	return 0;
}
