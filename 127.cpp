// time: s.size() * L * L
// space: s.size() * wordList.size()

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // hit -> cog
        // *it -> no
        // h*t -> hot? -> ds:{"h*t": "hot";} -> create map
        //  hot -> *ot -> dot -> introduce visited for element
        // hi*
        // map: {hot, dot, dog}
        unordered_map<string, vector<string>> word_map;

        for (string word : wordList) {
            for (int i = 0; i < (int)word.size(); ++i) {
                string tmp = word.substr(0,i) + '*' + word.substr(i+1);//不能用python的这个写法: string tmp = word[:i] + '*' + word[i+1:];
                word_map[tmp].push_back(word);
            } // 如何检查这个map创建的质量呢? 
        }
        
        //BFS
        queue<string> q;
        q.push(beginWord);
        int count = 0;
        while (!q.empty()) {
            int sz = (int)q.size();
            count += 1;
            for (int j = 0; j < sz; ++j) {
                string curr = q.front(); q.pop();
                if (curr == endWord) {
                    return count;
                }
                for (int i = 0; i < (int)curr.size(); ++i) {
                    string tmp = curr.substr(0,i) + '*' + curr.substr(i+1);
                    if (word_map.count(tmp)) {
                        cout << tmp << word_map[tmp][0] << "\n";
                        for (string word : word_map[tmp]) {
                            q.push(word);
                        } 
                        word_map.erase(tmp); //delete keys and values in map?
                    }
                }
            }
        }
        return 0;
        }
};