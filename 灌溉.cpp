#include<iostream>
#include<vector>
using namespace std;

const int inf = 888888888;
int main(){

    int n;
    cin >> n;
    vector<vector<int>> mp(n, vector<int>(n, 0));
    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j)
            cin >> mp[i][j];
    }
    vector<int> dis(n, inf);
    dis[0] = 0;
    int pos=0, res=0, min_d=0, num=1, next_pos=0;
    while(num < n){
        min_d = inf;
        for(int i=0; i<n; i++){
            if(dis[i]){
                dis[i] = min(min_d, mp[pos][i]);
                if(min_d > dis[i]){
                    min_d = dis[i];
                    next_pos = i;
                }
            }
        }
        res += min_d;
        pos = next_pos;
        dis[pos] = 0;
        ++num;
    }
    cout << res << endl;

    return 0;
}
