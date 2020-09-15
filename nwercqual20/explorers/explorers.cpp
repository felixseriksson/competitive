#include <bits/stdc++.h>
using namespace std;
int n,a[200005];
int main()
{
    int cases;
    cin>>cases;
    while(cases--)
    {
        cin>>n;
        int i;
        for(i=1;i<=n;i++)scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        int ans=0;
        int cnt=0;
        a[n+1]=0x3f3f3f3f;
        for(i=1;i<=n+1;i++)
        {
            cnt++;
            if(a[i]==cnt)
            {
                ans++;
                cnt=0;
            }
        }   
        cout<<ans<<endl;
    }
    
}