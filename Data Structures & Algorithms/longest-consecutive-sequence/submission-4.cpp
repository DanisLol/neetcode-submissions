class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::set<int> s(nums.begin(), nums.end());
        int longest = 0;
        for(int i : nums){
            int length = 0;
            if (!s.contains(i-1)){
                while (s.contains(i + length)){
                    length +=1;
                }
                longest = max(longest, length);
            }
            
        }
        return longest;
    }
};
