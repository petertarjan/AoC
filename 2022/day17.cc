#include <iostream>
#include <string>
#include <vector>
using namespace std;
using ll=long long;

int main() {
	string jet;
	getline(cin, jet);
	int jp=0;
	vector<string> stack;
	ll sol=0ll;
	vector<vector<pair<int,int> > > elements = {
		{ {0,0},{0,1},{0,2},{0,3} }, // -
		{ {0,1},{1,0},{1,1},{1,2},{2,1} }, // +
		{ {0,0},{0,1},{0,2},{1,2},{2,2} },
		{ {0,0},{1,0},{2,0},{3,0} },
		{ {0,0},{1,0},{0,1},{1,1} } };
	//	for (int i=0;i<2022;++i) {
	
	vector<pair<int,int> > pr;
	vector<int> ss;
	bool findperiod=true;
	for (ll i=0ll;;++i) {		
		/*
		if (i%ll(elements.size())==0 && jp==6) {
			while (!stack.empty() && stack.back()==".......") stack.pop_back();
			cout<<i<<' '<<jp<<' '<<ll(stack.size())+sol<<endl;
		}
		*/

		//for (int i=0;i<2;++i) {
		while (stack.size()<3u || stack[stack.size()-1u]!="......."  || stack[stack.size()-2u]!="......."  || stack[stack.size()-3u]!=".......")
			stack.emplace_back(".......");
		const vector<pair<int,int> >& e=elements[i%int(elements.size())];
		int o_c=2,o_r=int(stack.size());
		for (;;) {
			char jt=jet[jp];
			jp=(jp+1)%int(jet.size());
			int n_o_c=(jt=='<')?o_c-1:o_c+1;
			bool OK=true;
			for (auto rc : e) {
				int r=o_r+rc.first;
				int c=n_o_c+rc.second;
				if (c<0 || c>=7) { OK=false; break; }
				if (r<int(stack.size()) && stack[r][c]!='.') { OK=false; break; }
			}
			if (OK) o_c=n_o_c;
			OK=true;
			int n_o_r=o_r-1;
			for (auto rc : e) {
				int r=n_o_r+rc.first;
				int c=o_c+rc.second;
				if (r<0) { OK=false; break; }
				if (r<int(stack.size()) && stack[r][c]!='.') { OK=false; break; }
			}
			if (!OK) break;
			o_r=n_o_r;
		}
		
		for (auto rc : e) {
			int r=o_r+rc.first;
			int c=o_c+rc.second;
			while (int(stack.size())<=r) stack.emplace_back(".......");
			stack[r][c]='#';
		}
		//		for (auto it=stack.crbegin();it!=stack.crend();++it) cout<<(*it)<<endl;
		//		cout<<endl;
		/*
		if (stack.size()>1000010) {
			sol+=1000000ll;
			stack.erase(stack.begin(),stack.begin()+1000000);
			}*/
		if (findperiod) {
			int imod=i%ll(elements.size());
			pr.emplace_back(jp,imod);
			while (stack.back()==".......") stack.pop_back();
			ss.push_back(int(stack.size()));
			if (i>=2022ll && i%2ll==0ll) {
				ll i2=i/2ll;
				if (jp==pr[i2].first && imod==pr[i2].second) {
					findperiod=false;
					ll left=1000000000000ll-i;
					left-=left%i2;
					i+=left;
					sol=(left/i2)*ll(ss.back()-ss[i2]);
				}
			}
		}

		if (i==2021) {
				while (stack.back()==".......") stack.pop_back();
				cout<<"Part1: "<<stack.size()<<endl;
		}
		if (i==1000000000000ll-1ll) {
				while (stack.back()==".......") stack.pop_back();
				cout<<"Part2: "<<stack.size()+sol<<endl;
				break;
		}
	}
	return  0;
}
