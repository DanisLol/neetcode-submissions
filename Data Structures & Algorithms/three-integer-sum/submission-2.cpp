class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::unordered_map<int, int> s;
        vector<vector<int>> v;
        int l = 0;
        int r = nums.size() - 1;
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++){
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            l = i + 1;
            r = nums.size() - 1;
            while (l < r){
                if (nums[i] + nums[l] + nums[r] == 0){
                    v.push_back({nums[i], nums[l], nums[r]});
                    l += 1;
                    while (l < r && nums[l] == nums[l - 1]){
                        l += 1;
                    }
                }
                else if (nums[i] + nums[l] + nums[r] < 0){
                    l += 1;
                }
                else if(nums[i] + nums[l] + nums[r] > 0){
                    r -=1;
                }
                
                        
                
            }
        }


        return v;


    }
};
