
---

## 目录

1. 数组与二分查找
2. 双指针技巧
3. 滑动窗口
4. 深度优先搜索 (DFS)
5. 广度优先搜索 (BFS)
6. 回溯 (Backtracking)
7. 动态规划 (DP)
8. 贪心 (Greedy)
9. 并查集 (Union-Find)
10. Trie 前缀树
11. 树遍历模板
12. 堆 (Heap)
13. 单调栈 & 单调双端队列
14. 拓扑排序 (Topological Sort)
15. 前缀和 & 差分数组
16. 附录补充模板

---

### 1  数组与二分查找

```cpp
#include <bits/stdc++.h>
int binary_search(const std::vector<int>& nums, int target) {
    int l = 0, r = (int)nums.size() - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] == target) return mid;
        (nums[mid] < target) ? l = mid + 1 : r = mid - 1;
    }
    return -1;
}
```

---

### 2  双指针技巧

#### 2.1  已排序数组 Two-Sum

```cpp
std::pair<int,int> two_sum_sorted(const std::vector<int>& a, int target) {
    int l = 0, r = (int)a.size() - 1;
    while (l < r) {
        int s = a[l] + a[r];
        if (s == target) return {l, r};
        (s < target) ? ++l : --r;
    }
    return {-1, -1};
}
```

#### 2.2  快慢指针判环（数组映射为索引）

```cpp
bool has_cycle(const std::vector<int>& nxt) {
    int slow = 0, fast = 0;
    while (fast < nxt.size() && nxt[fast] < nxt.size()) {
        slow = nxt[slow];
        fast = nxt[nxt[fast]];
        if (slow == fast) return true;
    }
    return false;
}
```

---

### 3  滑动窗口

#### 3.1  固定窗口最大和

```cpp
long long max_sum_subarray(const std::vector<int>& a, int k) {
    long long window = std::accumulate(a.begin(), a.begin()+k, 0LL);
    long long best = window;
    for (int i = k; i < a.size(); ++i) {
        window += a[i] - a[i-k];
        best = std::max(best, window);
    }
    return best;
}
```

#### 3.2  Sliding-Window Maximum（单调队列）

```cpp
std::vector<int> sliding_window_max(const std::vector<int>& nums, int k) {
    std::deque<int> dq;                // 存索引
    std::vector<int> res;
    for (int i = 0; i < nums.size(); ++i) {
        while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k-1) res.push_back(nums[dq.front()]);
    }
    return res;
}
```

---

### 4  深度优先搜索 (DFS)

```cpp
void dfs_graph(int u, const std::vector<std::vector<int>>& g, std::vector<int>& vis) {
    if (vis[u]) return;
    vis[u] = 1;
    for (int v : g[u]) dfs_graph(v, g, vis);
}
```

二维网格 DFS（4 方向）：

```cpp
void dfs_grid(int x,int y,const std::vector<std::vector<int>>& g,
              std::vector<std::vector<int>>& vis) {
    int R=g.size(), C=g[0].size();
    if (x<0||x>=R||y<0||y>=C||vis[x][y]||g[x][y]==0) return;
    vis[x][y]=1;
    int dx[4]={1,-1,0,0}, dy[4]={0,0,1,-1};
    for(int k=0;k<4;++k) dfs_grid(x+dx[k],y+dy[k],g,vis);
}
```

---

### 5  广度优先搜索 (BFS)

```cpp
std::vector<int> bfs_graph(int s,const std::vector<std::vector<int>>& g){
    std::vector<int> vis(g.size(),0), order;
    std::queue<int> q; q.push(s); vis[s]=1;
    while(!q.empty()){
        int u=q.front(); q.pop(); order.push_back(u);
        for(int v:g[u]) if(!vis[v]){ vis[v]=1; q.push(v); }
    }
    return order;
}
```

---

### 6  回溯 (Backtracking) — 全排列

```cpp
void permute_dfs(std::vector<int>& nums, std::vector<int>& path,
                 std::vector<int>& used, std::vector<std::vector<int>>& res) {
    if (path.size() == nums.size()) { res.push_back(path); return; }
    for (int i = 0; i < nums.size(); ++i) {
        if (used[i]) continue;
        used[i] = 1; path.push_back(nums[i]);
        permute_dfs(nums, path, used, res);
        path.pop_back(); used[i] = 0;
    }
}

std::vector<std::vector<int>> permute(std::vector<int> nums) {
    std::vector<std::vector<int>> res;
    std::vector<int> path, used(nums.size(), 0);
    permute_dfs(nums, path, used, res);
    return res;
}
```

---

### 7  动态规划 (DP)

#### 7.1  斐波那契

```cpp
long long fib(int n){
    if(n<=1) return n;
    long long a=0,b=1;
    for(int i=2;i<=n;++i){
        long long c=a+b; a=b; b=c;
    }
    return b;
}
```

#### 7.2  0-1 背包

```cpp
int knapsack(const std::vector<int>& w,const std::vector<int>& v,int cap){
    int n=w.size();
    std::vector<std::vector<int>> dp(n+1,std::vector<int>(cap+1,0));
    for(int i=1;i<=n;++i){
        for(int c=0;c<=cap;++c){
            dp[i][c]=dp[i-1][c];
            if(w[i-1]<=c)
                dp[i][c]=std::max(dp[i][c], dp[i-1][c-w[i-1]]+v[i-1]);
        }
    }
    return dp[n][cap];
}
```

---

### 8  贪心 (Greedy) — 区间调度

```cpp
int max_meetings(std::vector<std::pair<int,int>>& iv){
    std::sort(iv.begin(), iv.end(), [](auto& a,auto& b){ return a.second<b.second; });
    int cnt=0, end=-1e9;
    for(auto& [s,e]:iv){
        if(s>=end){ ++cnt; end=e; }
    }
    return cnt;
}
```

---

### 9  并查集 (Union-Find)

```cpp
struct DSU{
    std::vector<int> p;
    DSU(int n):p(n){ std::iota(p.begin(),p.end(),0); }
    int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
    void unite(int a,int b){ p[find(a)]=find(b); }
};
```

---

### 10  Trie 前缀树

```cpp
struct TrieNode{
    TrieNode* child[26]{};
    bool end=false;
};
struct Trie{
    TrieNode* root=new TrieNode();
    void insert(const std::string& s){
        TrieNode* node=root;
        for(char c:s){
            int idx=c-'a';
            if(!node->child[idx]) node->child[idx]=new TrieNode();
            node=node->child[idx];
        }
        node->end=true;
    }
    bool search(const std::string& s){
        TrieNode* node=root;
        for(char c:s){
            int idx=c-'a';
            if(!node->child[idx]) return false;
            node=node->child[idx];
        }
        return node->end;
    }
};
```

---

### 11  树遍历模板

```cpp
struct Node{ int val; Node* left,*right; };

// 递归先序
void preorder(Node* root,std::vector<int>& out){
    if(!root) return;
    out.push_back(root->val);
    preorder(root->left,out); preorder(root->right,out);
}

// 迭代先序
std::vector<int> preorder_iter(Node* root){
    if(!root) return {};
    std::vector<int> res; std::stack<Node*> st; st.push(root);
    while(!st.empty()){
        Node* cur=st.top(); st.pop();
        res.push_back(cur->val);
        if(cur->right) st.push(cur->right);
        if(cur->left)  st.push(cur->left);
    }
    return res;
}

// 迭代中序
std::vector<int> inorder_iter(Node* root){
    std::vector<int> res; std::stack<Node*> st; Node* cur=root;
    while(cur || !st.empty()){
        while(cur){ st.push(cur); cur=cur->left; }
        cur=st.top(); st.pop(); res.push_back(cur->val); cur=cur->right;
    }
    return res;
}

// 层序
std::vector<int> level_order(Node* root){
    if(!root) return {};
    std::vector<int> res; std::queue<Node*> q; q.push(root);
    while(!q.empty()){
        Node* cur=q.front(); q.pop(); res.push_back(cur->val);
        if(cur->left) q.push(cur->left);
        if(cur->right) q.push(cur->right);
    }
    return res;
}
```

---

### 12  堆 (Heap) — `std::priority_queue`

```cpp
// 最大堆默认比较器
std::priority_queue<int> maxh;

// 最小堆
std::priority_queue<int, std::vector<int>, std::greater<int>> minh;

// 自定义结构
struct Node{ int cnt, task; };
struct Cmp{ bool operator()(const Node& a,const Node& b) const{
               return a.cnt < b.cnt; } };   // 大顶堆
std::priority_queue<Node, std::vector<Node>, Cmp> pq;
```

---

### 13  单调栈 & 单调双端队列

#### 13.1  左侧第一个更小值

```cpp
std::vector<int> first_smaller_left(const std::vector<int>& a){
    std::vector<int> res(a.size(), -1), st;
    for(int i=0;i<a.size();++i){
        while(!st.empty() && a[st.back()] >= a[i]) st.pop_back();
        if(!st.empty()) res[i]=st.back();
        st.push_back(i);
    }
    return res;
}
```

#### 13.2  Sliding-Window Maximum 见 §3.2

---

### 14  拓扑排序 (Kahn)

```cpp
std::vector<int> topo_sort(const std::vector<std::vector<int>>& g){
    int n=g.size(); std::vector<int> indeg(n), order;
    for(int u=0;u<n;++u) for(int v:g[u]) ++indeg[v];
    std::queue<int> q; 
    for(int i=0;i<n;++i) if(!indeg[i]) q.push(i);
    while(!q.empty()){
        int u=q.front(); q.pop(); order.push_back(u);
        for(int v:g[u]) if(--indeg[v]==0) q.push(v);
    }
    return order.size()==n ? order : std::vector<int>{};  // 空表示有环
}
```

---

### 15  前缀和 & 差分数组

```cpp
// 前缀和
std::vector<long long> prefix(const std::vector<int>& a){
    std::vector<long long> pre(a.size()+1,0);
    for(int i=0;i<a.size();++i) pre[i+1]=pre[i]+a[i];
    return pre;                         // 区间 [l,r] = pre[r+1]-pre[l]
}

// 差分
void range_add(std::vector<long long>& diff,int l,int r,long long delta){
    diff[l]+=delta;
    if(r+1<diff.size()) diff[r+1]-=delta;
}
```

---

### 16  附录补充模板

| 主题                 | 关键代码                                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **快速幂**            | `long long qpow(long long a,long long n,long long mod){ long long res=1; while(n){ if(n&1) res=res*a%mod; a=a*a%mod; n>>=1;} return res; }` |
| **Fenwick (树状数组)** | `for(int i=x;i<=n;i+=i&-i) bit[i]+=v;` / `for(int s=0;i;i-=i&-i) s+=bit[i];`                                                                |
| **KMP**            | 先构 `nxt` 数组，再匹配；逻辑与 Python 版一致                                                                                                              |

---

> **小贴士**
>
> * STL 容器+lambda 可大幅减少模板行数。
> * C++17 起 `#include <bits/stdc++.h>` 与 `std::gcd`, `std::optional`、`if constexpr` 等语法糖能进一步精简实现。
