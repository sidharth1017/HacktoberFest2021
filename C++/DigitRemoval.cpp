#include<bits/stdc++.h>
using namespace std;
 
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define endl "\n"
#define w(t) ll t;cin>>t;while(t--)
#define sd(val) scanf("%d",&val)
#define ss(val) scanf("%s",&val)
#define sl(val) scanf("%lld",&val)
#define debug(val) printf("check%d\n",val)
#define all(v) v.begin(),v.end()
#define PB push_back
#define MP make_pair
#define FF first
#define SS second
#define ll long long
#define MOD 1000000007
#define clr(val) memset(val,0,sizeof(val))
#define what_is(x) cerr << #x << " is " << x << endl; 
#define OJ \
    freopen("input.txt", "r", stdin); \
    freopen("output.txt", "w", stdout);
#define FIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
 
ll isDigPres(ll n, int d) {
    ll ret = 0;
    ll a = 1;

    while(n>0) {
        if(n%10==d) {
            ret = a;
        }
        a*=10 ;
        n/=10;
    }

    return ret;
}

ll solve(ll n, int d, bool &flag) {
    ll pos = isDigPres(n,d) ;

    //cout<<pos<<endl;

    if(pos==0) {
        flag = false;
        return 0;
    }


    else {
        ll a = n%pos;
        return pos-a ;
    }
}
 
int main() 
{
    //OJ
    w(t)
    {
        ll n;
        int d;

        cin>>n>>d;

        bool flag = true ;

        ll ans = 0;

        while(flag) {
            ll b = solve(n,d,flag) ;
            ans += b;
            n += b;
        }

        cout<<ans<<endl ;
    }
 
 
 
 
 
return 0;
   
}