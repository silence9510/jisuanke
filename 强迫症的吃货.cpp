#include<iostream>
#include<queue>
#include<cstring>
#include<cstdio>
using namespace std;
const int M = 25+5;

struct food{
    int id;
    int val[M];
}f[20];

struct node{
    vector<int> id;
    int val[M];
};

int Val[M];
int n, m;

bool isOk(node now){
    for(int i=0; i<n; i++){
        if(now.val[i] < Val[i])
            return false;
    }
    return true;
}

node eat(){
    queue<node> q;
    node hd, ans;
    hd.id.clear();
    for(int i=0; i<n; i++)
        hd.val[i] = 0;
    q.push(hd);
    while(!q.empty()){
        node pre = q.front();
        q.pop();
        int len = pre.id.size();
        int nowid = (len == 0) ? 0 : pre.id[len-1];
        for(int i=nowid; i<m; i++){
            node now;
            now = pre;
            now.id.push_back(f[i].id);
            for(int j=0; j<n; j++){
                now.val[j] += f[i].val[j];
            }
            if(isOk(now))
                return now;
            else
                q.push(now);
        }
    }
    return ans;
}

int main(){

    cin >> n;
    for(int i=0; i<n; i++){
        cin >> Val[i];
    }
    cin >> m;
    for(int i=0; i<m; i++){
        f[i].id = i+1;
        for(int j=0; j<n; j++){
            cin >> f[i].val[j];
        }
    }

    node ans = eat();

    cout << ans.id.size();
    for(int i=0; i<ans.id.size(); i++){

        cout  << " " << ans.id[i];
    }
    return 0;
}
