#include<iostream>
#include<cstring>
#include<queue>
using namespace std;

struct node
{
    int x, y;
    int step;
};
char chessBoard[100][100];
int state[100][100];
int direction[8][2] =
{
    1,2,2,1,2,-1,1,-2,-1,-2,-2,-1,-2,1,-1,2
};
int m, n, sx, sy, ex, ey;
int flag;

void bfs(){
    queue<node> q;
    //��ʼ��
    node hn;
    hn.x = sx;
    hn.y = sy;
    hn.step = 0;
    state[sx][sy] = 1;
    q.push(hn);

    while(!q.empty()){
        node pn = q.front();
        //�ߵ��յ�
        if(pn.x == ex && pn.y == ey){
            //���Ϊ�յ㣻
            if(pn.step == 0){
                break;
            }
            cout << pn.step << endl;
            flag = 1;
            break;
        }
        node nn;
        //�����ӽ��
        for(int i=0; i<8; i++){
            nn.x = pn.x + direction[i][0];
            nn.y = pn.y + direction[i][1];
            //���ȣ�
            int bx = pn.x + direction[i][0]/2;
            int by = pn.y + direction[i][1]/2;
            if(chessBoard[bx][by] == '#'){
                continue;
            }
            //�Ƿ��߳��磿
            if(nn.x>=0 && nn.x<m && nn.y>=0 && nn.y<n && chessBoard[nn.x][nn.y]!='#' && state[nn.x][nn.y]==0){
                nn.step = pn.step+1;
                q.push(nn);
                state[nn.x][nn.y] = 1;
            }
        }
        q.pop();
    }
    if(flag == 0){
        cout << -1 << endl;
    }
}

int main()
{

    while(cin>>m>>n){
        memset(chessBoard, 0, sizeof(chessBoard));
        memset(state, 0, sizeof(state));
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                cin >> chessBoard[i][j];
                if(chessBoard[i][j] == 's')
                {
                    sx = i;
                    sy = j;
                }
                if(chessBoard[i][j] == 'e')
                {
                    ex = i;
                    ey = j;
               }
            }
        }
        flag = 0;
        bfs();
    }
    return 0;
}
