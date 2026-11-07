class Solution {
public:
    int maxArea(vector<int>& heights) {
        int a = 0;
        int b = heights.size() - 1;
        int maximum = (b-a) * min(heights[a], heights[b]);
        while(a < b){
            if(heights[a] < heights[b]){
                a += 1;
            }
            else{
                b -= 1;
            }
            
            maximum = max(maximum, (b-a) * min(heights[a], heights[b]));

        }
        return maximum;
    }
};
