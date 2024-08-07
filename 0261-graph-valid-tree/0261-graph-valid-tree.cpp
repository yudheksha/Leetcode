class Solution {
public:
    vector <int> ve[2001];
    int vis[2001];
    bool dfs(int s, int p){
        vis[s] = 1;
        bool res = true;
        for(auto x: ve[s]){
            if(x!=p){
                if(vis[x])return false;
                else {
                    res &= dfs(x,s);
                }
            }
        }
        return res;
    }
    bool validTree(int n, vector<vector<int>>& edges) {

        for(auto e: edges){
            ve[e[0]].push_back(e[1]);
            ve[e[1]].push_back(e[0]);
        }
        bool ok = dfs(0,-1);
        for(int i=0;i<n;i++){
            if(!vis[i])ok=false;
        }
        return ok;
    }
};